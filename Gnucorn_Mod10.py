#Urbano Iguala, Modulo 10
from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
import json


def application(environ,start_response):
    headers = [('Content-type','text/html')]
    start_response('200 OK', headers)

    response = {
        "payload ": "Response Gunicorn Server"
    }

    return [bytes(json.dumps(response),'utf-8')]

app = Flask(__name__)
#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'diccionarioSQL'
mysql = MySQL(app)
app.secret_key = 'mysecretkey'
#Settings


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Diccionario')
    data = cur.fetchall()
    return render_template('index.html',Diccionario = data)

@app.route('/add_word',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO diccionario(palabra,significado) VALUES(%s,%s)',(palabra,significado))
        mysql.connection.commit()
        flash('Palabra agregada')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM diccionario WHERE palabra_id = (%s)',(id))
    data = cur.fetchall()
    return render_template('editar.html',diccionario = data[0])

@app.route('/update/<string:id>',methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE diccionario
            SET palabra = %s,
                significado = %s
            WHERE´palabra_id = %s
            """,(palabra,significado,id))
        flash('Palabra actualizada')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM diccionario WHERE palabra_id=(%s)',(id))
    mysql.connection.commit()
    flash('Palabra eliminada')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)