#Imports
import les_meves_funcions.datos
from les_meves_funcions.funcions_consultesDB import *
import les_meves_funcions


def logToFile(text):
    f = open("./logfileSevenAndHalf.txt", "a")
    f.write(text + "\n")
    f.close()


def new_nif():
    # Comprobación del número del DNI al crear un nuevo jugador
    resultado = SelectBBDD("Select player_id from player")
    exist_id = []
    for i in range(len(resultado)):
        exist_id.append(resultado[i][0])
    while True:
        dni = input("Enter NIF: ")
        # Comprobamos que introduce 9 caracteres.
        try:
            if not len(dni) == 9:
                raise ValueError("Incorrect lenght.")
        # Debe estar compuesto de 8 números y 1 letra.
            elif not dni[:8].isdigit() or not dni[8].isalpha():
                raise ValueError("Incorrect format.")
        # Comprobación de que ha introducido la letra correspondiente.
            elif not les_meves_funcions.datos.letrasDni[int(dni[:8]) % 23] == dni[8].upper():
                raise ValueError("Incorrect letter.")
        # Miramos si el DNI ya esta registrado en otro cliente.
            elif dni.upper() in exist_id:
                raise ValueError("ID: {} already exists".format(dni))
            else:
                break
        except ValueError as error:
            print(error)
        except IndexError:
            print("Incorrect format.")
    return dni.upper()


def newPlayer():
    while True:
        name = input("Name:")
        try:
            if name == "":
                raise ValueError("Name cannot be empty")
            elif not name.isalnum():
                raise ValueError("Name must be letters or numbers only")
        except ValueError as error:
            print(error)
        else:
            break
        NIF = input("")
    dni = new_nif()
    return
