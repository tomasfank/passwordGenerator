import random

def crearPassword(destino, password):
    try:
        #abrir archivo
        archivo = open("passwords.txt", "at")
        #escribir en el archivo
        archivo.write(destino + ';' + password + '\n')
    finally:
        try:
            #cerrar archivo
            archivo.close()
        except NameError:
            pass     

destino_de_password = input("¿Para que requiere la contraseña?")       
nro = str(random.randint(1000,9999))
