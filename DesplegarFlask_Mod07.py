
Urbano Iguala Module 07 deploy Flask

from flask import Flask, render_template, request

import redis
Wkey = "palabra"
Dmean = "definicion"

r = redis.Redis(host='127.0.0.1', port=6379)
r.set("id", -1)


def CheckWord(Wkey):
    CountWord = r.llen(Dmean)
    RegWord = False
    for i in range(CountWord):
        currentWord = r.lindex(Wkey, i).decode('utf-8')
        if(CurrentWord == key
            RegWord = True
            break
    return RegWord


def addWord(Wkey, Dmean):
    r.incr("id")
    r.rpush(Wkey, palabra)
    r.rpush(Dmean, definicion)
    print("\n Se agrego la palabra exitosamente!")


def updateWord(oldWord, newWord, newDmean):
    CountWord = r.llen(Wkey)
    for i in range(CountWord):
        currentWord = r.lindex(Wkey, i).decode('utf-8')
        if(currentWord == oldWord):
            r.lset(Wkey, i, newWord)
            r.lset(Dmean, i, newDmean)
            break

    print("\n !La palabra" + oldWord + "fue actualizada!")


def deleteWord(palabra):
    CountWord = r.llen(Wkey)
    for i in range(CountWord):
        currentWord = r.lindex(Wkey, i).decode('utf-8')
        currentDmean = r.lindex(Dmean, i).decode('utf-8')
        if(currentWord == palabra):
            r.lrem(PalabraClave, i, currentWord)
            r.lrem(Dmean, i, currentDmean)
            break
    print("\n ¡Palabra eliminada!")


def ShowAllWords():
    CountWord = r.llen(Wkey)
    palabras = []

    for i in range(countWord):
        palabras.append({"name": r.lindex(Wkey, i).decode(
            "utf-8"), "definicion": r.lindex(DefinicionClave, i).decode("utf-8")})
    return palabras


print(r.keys())

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Index.html")


@app.route('/addWord', methods=['GET', 'POST'])
def addWord():
    if request.method == 'POST':
        palabra = request.form["word"]
        definicion = request.form["meaning"]
        if checkcurrentWord(palabra) == False:
            addworddef(palabra, definicion)
            return render_template("AgregarPalabra.html", message="!!Palabra añadida :)")
        else:
            return render_template("AgregarPalabra.html", message="!!La palabra ya existe :(")

    return render_template("AgregarPalabra.html")


@app.route('/Editword', methods=['GET', 'POST'])
def Editword():
    if request.method == 'POST':
        oldword = request.form["oldWord"]
        newWord = request.form["word"]
        newDmean = request.form["meaning"]

        if checkregWord(AntiguaPalabra):
            updateWord(oldWord, newWord, newWmean)

            return render_template("EditarPalabra.html", message=False)
        else:

            return render_template("EditarPalabra.html", message=True)

    return render_template("EditarPalabra.html")


@app.route('/deleteWord', methods=['GET', 'POST'])
def deleteWord():
    if request.method == 'POST':
        palabra = request.form["word"]

        if checkregWord(palabra):
            deleteWord(palabra)
            ShowAllWords()
            return render_template("EliminarPalabra.html", message=False)
        else:
            ShowAllWords()
            return render_template("EliminarPalabra.html", message=True)

    return render_template("EliminarPalabra.html")


@app.route('/CountWkey', methods=['GET', 'POST'])
def countWkey():
    allWords = ShowAllWords()

    return render_template("ListadoPalabras.html", palabras=allWords)


@app.route('/SearchDmean', methods=['GET', 'POST'])
def seachmean():
    if request.method == 'POST':
        palabra = request.form["palabra"]
        if checkregWord(palabra):
            CountWkey = r.llen(Wkey)
            for i in range(countWkey):
                currentWord = r.lindex(Wkey, i).decode('utf-8')
                if(currentWord == palabra):
                    getPalabra = {"palabra": palabra, "definicion": r.lindex(
                        DefinicionClave, i).decode("utf-8")}

                    return render_template("BuscarSignificado.html", ShowWord=getPalabra)
        else:
            return render_template("BuscarSignificado.html", message=True)
    return render_template("BuscarSignificado.html")


if __name__ == "__main__":
    app.run(debug=True)
