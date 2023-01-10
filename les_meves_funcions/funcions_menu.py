from les_meves_funcions.funcions_generals import *
# Funciones de menus
def getOpt(header, textOpts, inputOptText, rangeList, dictionary, exceptions):
    while True:
        # Imprime la cabecera
        print(header)
        # Imprime las opciones
        print(textOpts)
        # Le pide al usuario la opcion
        opt = input(inputOptText)
        # Intenta pasar la opcion del usuario a int, si puede comprueba si la opt esta en alguno de los parametros
        try:
            opt = int(opt)
            if opt in rangeList:
                return opt

            elif opt in dictionary:
                return opt

            elif opt in exceptions:
                return opt

            # Si la opt no esta en ningun parametro anterior envia un mensaje de error
            else:
                print("Invalid option".center(100, "="))
                input("Enter to continue".center(100))

        # Si no puede pasar la opt a int, captura el error y comprueba si la opt esta en alguno de los parametros pero
        # Esta vez como str
        except ValueError:
            if opt in exceptions:
                return opt

            elif opt in dictionary:
                return opt

            # Si no encuentra la opt en ninguno de los parametros anteriores imprime un mensaje de error
            else:
                logToFile("The introduced value were wrong")
                print("Invalid option".center(100, "="))
                input("Enter to continue".center(100))
