#Imports
import random
from les_meves_funcions.datos import *
from les_meves_funcions.funcions_consultesDB import *
from les_meves_funcions.funcions_menu import *


def new_name():
    while True:
        print("*" * 95 + "\n" +
                      figlet_format(" " * 24 + "New Human Player", font="doom") +
                      "*" * 95 + "\n")
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
    return name
def new_nif(human):
    # Comprobación del número del DNI al crear un nuevo jugador
    resultado = SelectBBDD("Select player_id from player")
    exist_id = []
    for i in range(len(resultado)):
        exist_id.append(resultado[i][0])
    while True:
        print("*" * 95 + "\n" +
                      figlet_format(" " * 24 + "New Human Player", font="doom") +
                      "*" * 95 + "\n")
        if human:
            dni = input("Enter NIF: ")
            # Comprobamos que introduce 9 caracteres.
            try:
                if not len(dni) == 9:
                    raise ValueError("Incorrect lenght.")
            # Debe estar compuesto de 8 números y 1 letra.
                elif not dni[:8].isdigit() or not dni[8].isalpha():
                    raise ValueError("Incorrect format.")
            # Comprobación de que ha introducido la letra correspondiente.
                elif not letrasDni[int(dni[:8]) % 23] == dni[8].upper():
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
        else:
            dni = ""
            for i in range(1,9):
                dni += str(random.randint(1,9))
            dni += letrasDni[random.randint(len(0,letrasDni))]
    return dni.upper()


def player_profile():
    profile = menu06()
    return profile

def save_player(name, dni, profile, human_bool):
    if profile == 30:
        name_prof = "Cautious"
    elif profile == 40:
        name_prof = "Moderated"
    elif profile == 50:
        name_prof = "Bold"
    print("*" * 95 + "\n" + figlet_format(" " * 24 + "New Human Player", font="doom") + "*" * 95 + "\n\n"+
          "Name: " + name + "\n" + "DNI: " + dni + "\n" + "Profile: " + name_prof + "\n")
    save = input("Save player? Y/N: ")
    while True:
        if save.upper() == "Y":
            print("Player saved")
            break
        elif save.upper() == "N":
            print("Player discarded.")
            break
        else:
            print("Incorrec option.")
    return

def menu06():
    while True:
        opt = getOpt(menus["06"]["header"],
                     menus["06"]["textOpts"],
                     menus["06"]["inputOptText"],
                     menus["06"]["rangeList"], {}, [])
        if opt == 1:
            profile = 30
            return profile
        if opt == 2:
            profile = 40
            return profile
        if opt == 3:
            profile = 50
            return profile
        else:
            break
def newPlayer_human():
    name = new_name()
    dni = new_nif(1)
    profile = player_profile()
    save_player(name, dni, profile, 1)
    print("aaaaaaaaaAAAAAAAAAAAAAAaaaaaaaaaaaa")

def newPlayer_boot():
    name = new_name()
    dni = new_nif(0)
    profile = player_profile()
    save_player(name, dni, profile, 0)

newPlayer_boot()
#90631839V