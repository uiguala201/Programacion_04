#*Urbano Iguala, 9-744-1120*
#*Diccionario Slang Panameño Sustitucion de SQLLITE X SQLALQUEMI


import sqlalchemy as db
engine = db.create_engine('sqlite3:///DiccionarioSlang.sqlite3')

def obtener_Conexion():
    conexion = engine.connect()
    metadata = db.MetaData()
    DiccionarioSlang = db.Table('DiccionarioSlang', metadata, autoload=True, autoload_with=engine)
    query = db.select([DiccionarioSlang]) 
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()


#*Se crea una tabla*
def crear_tablas():
    dictPan = db.Table('dictPan', metadata,
              db.Column('palabra', db.String(255), nullable=False),
              db.Column('significado', db.String(255), nullable=False),
              )
    metadata.create_all(engine)
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)

#*Vamos a Crear el menu que mostrara nuestro diccionario*
def principal():
    crear_tablas()
    menu = """
Diccionario Slang Panameño

a) Agregar nueva palabra
b) Editar palabra existente
c) Eliminar palabra existente
d) Ver listado de palabras
e) Buscar significado de palabra
f) Salir
Elige: """
    elegido = ""
    while elegido != "f":
        eleccion = input(menu)
        if elegido == "a":
            palabra = input("Ingrese la nueva palabra: ")
            #*Verificamos si la palabra ya ha sido agregada antes*
            pos_signif = bus_signif_palabra(palabra)
            if pos_signif:
                print(f"La palabra '{palabra}' ingresada ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agr_palabra(palabra, significado)
                print("Palabra agregada")
        if elegido == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            new_signif = input("Ingresa el nuevo significado: ")
            ed_palabra(palabra, new_significado)
            print("Se actualizo la palabra")
        if elegido == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if elegido == "d":
            palabras = obt_palabras()
            print("=== Lista de palabras ===")
            for palabra in palabras:
                print(palabra[0])
        if elegido == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            significado = bus_signif_palabra(palabra)
            if significado:
                print(f"El significado de '{palabra}' es:\n{significado[0]}")
            else:
                print(f"Palabra '{palabra}' no encontrada")


def agr_palabra(palabra, significado):
    query = db.insert(dictPan).values(palabra=, significado=) 
    ResultProxy = connection.execute(query)
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO diccionario(palabra, significado) VALUES (?, ?)"
    cursor.execute(sentencia, [palabra, significado])
    query = db.insert(dictPan).values(palabra=(palabra), significado=(significado)) 
    ResultProxy = connection.execute(query)
    conexion.commit()


def ed_palabra(palabra, nuevo_significado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
    cursor.execute(sentencia, [nuevo_signf, palabra])
    query = db.update(dictPan).values(significado = new_Signif)
    query = query.where(emp.columns.palabra == palabra)
    results = connection.execute(query)
    conexion.commit()


def eliminar_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM diccionario WHERE palabra = ?"
    cursor.execute(sentencia, [palabra])
    query = db.delete(dictPan)
    query = query.where(dictPan.columns.palabra == palabra)
    results = connection.execute(query)
    conexion.commit()


def obt_palabras():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT palabra FROM diccionario"
    query = db.select([dictPan]) 
    ResultProxy = connection.execute(query)
    print(repr(metadata.tables['dictPan']))
    cursor.execute(consulta)
    return cursor.fetchall()


def bus_signif_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT significado FROM diccionario WHERE palabra = ?"
    cursor.execute(consulta, [palabra])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    ResultSet[palabra:]
    return cursor.fetchone()


if __name__ == '__main__':
    principal()
