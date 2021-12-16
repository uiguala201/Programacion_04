## Importamos las librerias que utilizaremos en el proyecto

from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
from flask_mysqldb import MySQL


#Iniciamos la aplicación en Flask
app = Flask(__name__)
#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'Consultorio'
mysql = MySQL(app)
#Settings
app.secret_key = 'mysecretkey'

#Creamos las rutas de la aplicación
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Informacion')
    data = cur.fetchall()
    return render_template('index.html',Info = data)

@app.route('/add_info',methods=['POST'])
def add_info():
    if request.method == 'POST':
        Nombre = request.form['NombrePaciente']
        Apellido = request.form['ApellidoPaciente']
        Telefono = request.form['Telefono']
        Doctor = request.form['Doctor']
        Fecha = request.form['Fecha']
        Observacion = request.form['Observaciones']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Informacion (NombrePaciente,ApellidoPaciente,Telefono,Doctor,Fecha,Observaciones) VALUES(%s,%s,%s,%s,%s,%s)',(Nombre,Apellido,Telefono,Doctor,Fecha,Observacion))
        mysql.connection.commit()
        flash('Información Añadida Correctamente')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_info(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Informacion WHERE id = (%s)',(id))
    Info = cur.fetchall()
    return render_template('edit-contact.html',Info = Info[0])

@app.route('/update/<string:id>',methods = ['POST'])
def update_contact(id):
     if request.method == 'POST':
        Nombre = request.form['NombrePaciente']
        Apellido = request.form['ApellidoPaciente']
        Telefono = request.form['Telefono']
        Doctor = request.form['Doctor']
        Fecha = request.form['Fecha']
        Observacion = request.form['Observaciones']
        cur = mysql.connection.cursor()
        cur.execute("""
                    UPDATE Informacion
                    SET NombrePaciente = %s,
                    ApellidoPaciente = %s,
                    Telefono=%s,
                    Doctor=%s,
                    Fecha=%s,
                    Observaciones=%s
                    WHERE id = %s
                    """,(Nombre,Apellido,Telefono,Doctor,Fecha,Observacion,id))
        flash('Informacion actualizada satisfactoriamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Informacion WHERE id=(%s)',(id))
    mysql.connection.commit()
    return redirect(url_for('Index'))

#Creación de la Api Rest

## Entrega de datos

@app.route('/Api')
def obtenerinfo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Informacion')
    data = cur.fetchall()
    Datos_Finales = []
    for element in data:
        dicc = {}
        dicc['Id'] = element[0]
        dicc['NombrePaciente'] = element[1]
        dicc['ApellidoPaciente'] = element[2]
        dicc['Telefono'] = element[3]
        dicc['Doctor'] = element[4]
        dicc['Fecha'] = element[5]
        dicc['Observaciones'] = element[6]
        Datos_Finales.append(dicc)
    return jsonify(Datos_Finales)

@app.route('/Api/<string:id>',methods =['GET'])
def getinfo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Informacion WHERE id = (%s)',(id))
    Info = cur.fetchall()
    Datos_Finales = []
    for element in Info:
        dicc = {}
        dicc['Id'] = element[0]
        dicc['NombrePaciente'] = element[1]
        dicc['ApellidoPaciente'] = element[2]
        dicc['Telefono'] = element[3]
        dicc['Doctor'] = element[4]
        dicc['Fecha'] = element[5]
        dicc['Observaciones'] = element[6]
        Datos_Finales.append(dicc)
    if Datos_Finales!=None and Datos_Finales!=[]:
        return jsonify(Datos_Finales)
    else:
        return jsonify({"message":'Contacto No encontrado'})

@app.route('/Api',methods=['POST'])
def addinfo():
    Nombre=request.json['NombrePaciente']
    Apellido = request.json["ApellidoPaciente"]
    Telefono= request.json["Telefono"]
    Doctor=request.json["Doctor"]
    Fecha = request.json["Fecha"]
    Observaciones = request.json["Observaciones"]
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Informacion (NombrePaciente,ApellidoPaciente,Telefono,Doctor,Fecha,Observaciones) VALUES(%s,%s,%s,%s,%s,%s)',(Nombre,Apellido,Telefono,Doctor,Fecha,Observaciones))
    mysql.connection.commit()
    return jsonify({'message ':'Información añadida correctamente'})

@app.route('/Api/<string:Id>',methods =['PUT'])
def editinfo(Id):
    Nombre=request.json['NombrePaciente']
    Apellido = request.json["ApellidoPaciente"]
    Telefono= request.json["Telefono"]
    Doctor=request.json["Doctor"]
    Fecha = request.json["Fecha"]
    Observaciones = request.json["Observaciones"]
    cur = mysql.connection.cursor()
    cur.execute("""
                    UPDATE Informacion
                    SET NombrePaciente = %s,
                    ApellidoPaciente = %s,
                    Telefono=%s,
                    Doctor=%s,
                    Fecha=%s,
                    Observaciones=%s
                    WHERE id = %s
                    """,(Nombre,Apellido,Telefono,Doctor,Fecha,Observaciones,Id))
    mysql.connection.commit()
    return jsonify({"message":'Información Modificada Correctamente'})

@app.route('/Api/<string:Id>',methods=['DELETE'])
def deleteinfo(Id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Informacion WHERE id=(%s)',(Id))
    mysql.connection.commit()
    return jsonify({"message":'Informacion Eliminada Correctamente'})




















if __name__ == '__main__':
    app.run(port = 5000, debug = True)