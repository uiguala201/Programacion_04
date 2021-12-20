Urbano Iguala Modulo 03

from pymongo import MongoClient



cliente= MongoClient("localhost")
db= cliente["diccionarioMongoDB"]
basedatos = db['diccionario']


def Insert():
    Answ1 = "SI"
    i= 1
    while Answ1 == "SI":
        Answ1 = input("Deseas agregar una palabra nueva (Escribe 'SI' o 'NO'): ")
        if Answ1== "SI":
            f1 = input("Palabra en Español : ")
            f2 = input("Significado : ")
            basedatos.insert_one(({"id": i ,
                                   'palabra':f1,
                        'significado':f2}))
            print("Has agregado la palabra", f1, "Exitosamente)
            i+=1
        else:
            Answ1= "NO"
  
            
def Delete(f3):
    basedatos.delete_one({'palabra': f3})

def ShowData():
    for datos in basedatos.find({}):
        print(datos)
        
def Mean(f4):
    for palabras in basedatos.find({'palabra':f4}):
        print (palabras)

def Edit(f5,f6):
    basedatos.update_one({'': f5},
                         {"$set": {"significado":f6}})



while True:
    
    Insert()
    Answ2 = input("Deseas modificar alguna palabra (Escribe 'SI' o 'NO') : ")
    if Answ2 == "Si":
        f5 = input("Palabra Español: ")
        f6 = input("Significado : ")
        Edit(f5,f6)
                
    Answ3 = input("Consultar el significado de una palabra (Escribe 'SI' o 'No') : ")
    if Answ3 == "SI":
        f4= input("Palabra Español : ")
        Mean(f4)
        
    Answ4 = input("Quieres eliminar una palabra (Escribe 'SI' o 'NO') : ")
    if Answ4 == "SI":
        f3 = input("Palabra : ")
        Delete(f3)
    
    AnswData = input("Quieres ver todos los registros (Escribe 'SI' o 'NO') : ")
    if AnswData == "SI":
        ShowData()
            
    AnswF = input("Deseas Salir del programa (Escribe 'SI' o 'NO') : ")
    if AnswF == "SI":
        break
