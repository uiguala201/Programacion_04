Urbano Iguala Modulo 04

import redis
r= redis.Redis()
r.flushall()


def Insert():
    Answ1 = "SI"
    i= 1
    while Answer1 == "SI":
        Answer1 = input("Deseas agregar una palabra nueva (Escribe 'SI' o 'NO'): ")
        if Answer1== "SI":
            f1 = input("Palabra en Español : ")
            f2 = input("Significado : ")
            r.set(f1,f2)
            print("La palabra", f1, "fue agregada correctamente")
        else:
            Answer1= "NO"
  
            
def Delete(f3):
    r.delete(f3)
    print("Se borro la palabra", f3, "eitosamente")

def ShowData():
    Datos_Filas = r.keys()
    for Datos in Datos_Filas:
        Registros = r.get(Datos)
        print("Palabra: ",Datos, "Slang : ", Registros)
        
def Mean(f4):
    print("La palabra", f4, " Significa : ", r.get(f4))

def Edit(f5,f6):
    r.set(f5,f6)



while True:
    
    Insert()
    Answer2 = input("Deseas modificar alguna palabra (Escribe 'SI' o 'NO') : ")
    if Answer2 == "Si":
        f5 = input("Palabra Español: ")
        f6 = input("Significado : ")
        Edit(f5,f6)
                
    Answer3 = input("Consultar el significado de una palabra (Escribe 'SI' o 'No') : ")
    if Answer3 == "SI":
        f4= input("Palabra Español : ")
        Mean(f4)
        
    Answer4 = input("Quieres eliminar una palabra (Escribe 'SI' o 'NO') : ")
    if Answer4 == "SI":
        f3 = input("Palabra : ")
        Delete(f3)
    
    AnswData = input("Quieres ver todos los registros (Escribe 'SI' o 'NO') : ")
    if AnswData == "SI":
        ShowData()
            
    AnswF = input("Deseas Salir del programa (Escribe 'SI' o 'NO') : ")
    if AnswF == "SI":
        break