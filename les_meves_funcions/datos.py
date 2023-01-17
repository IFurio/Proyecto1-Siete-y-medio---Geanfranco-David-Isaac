# Imports
from pyfiglet import figlet_format


cartas = {
    "baraja_esp": {
        "O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
        "O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
        "O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
        "O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
        "O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
        "O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
        "O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
        "O10": {"literal": "Sota de Oros", "value": 10, "priority": 4, "realValue": 0.5},
        "O11": {"literal": "Caballo de Oros", "value": 11, "priority": 4, "realValue": 0.5},
        "O12": {"literal": "Rey de Oros", "value": 12, "priority": 4, "realValue": 0.5},

        "C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
        "C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
        "C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
        "C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
        "C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
        "C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
        "C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
        "C10": {"literal": "Sota de Copas", "value": 10, "priority": 3, "realValue": 0.5},
        "C11": {"literal": "Caballo de Copas", "value": 11, "priority": 3, "realValue": 0.5},
        "C12": {"literal": "Rey de Copas", "value": 12, "priority": 3, "realValue": 0.5},

        "E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
        "E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
        "E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
        "E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
        "E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
        "E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
        "E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
        "E10": {"literal": "Sota de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
        "E11": {"literal": "Caballo de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
        "E12": {"literal": "Rey de Espadas", "value": 12, "priority": 2, "realValue": 0.5},

        "B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
        "B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
        "B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
        "B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
        "B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
        "B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
        "B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
        "B10": {"literal": "Sota de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
        "B11": {"literal": "Caballo de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
        "B12": {"literal": "Rey de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
    },

    "baraja_poker": {
        "T01": {"literal": "As de Trebol", "value": 1, "priority": 1, "realValue": 1},
        "T02": {"literal": "Dos de Trebol", "value": 2, "priority": 1, "realValue": 2},
        "T03": {"literal": "Tres de Trebol", "value": 3, "priority": 1, "realValue": 3},
        "T04": {"literal": "Cuatro de Trebol", "value": 4, "priority": 1, "realValue": 4},
        "T05": {"literal": "Cinco de Trebol", "value": 5, "priority": 1, "realValue": 5},
        "T06": {"literal": "Seis de Trebol", "value": 6, "priority": 1, "realValue": 6},
        "T07": {"literal": "Siete de Trebol", "value": 7, "priority": 1, "realValue": 7},
        "T08": {"literal": "Ocho de Trebol", "value": 8, "priority": 1, "realValue": 0.5},
        "T09": {"literal": "Nueve de Trebol", "value": 9, "priority": 1, "realValue": 0.5},
        "T0J": {"literal": "Jota de Trebol", "value": 10, "priority": 1, "realValue": 0.5},
        "T0Q": {"literal": "Dama de Trebol", "value": 11, "priority": 1, "realValue": 0.5},
        "T0K": {"literal": "Rey de Trebol", "value": 12, "priority": 1, "realValue": 0.5},

        "P01": {"literal": "As de Picas", "value": 1, "priority": 2, "realValue": 1},
        "P02": {"literal": "Dos de Picas", "value": 2, "priority": 2, "realValue": 2},
        "P03": {"literal": "Tres de Picas", "value": 3, "priority": 2, "realValue": 3},
        "P04": {"literal": "Cuatro de Picas", "value": 4, "priority": 2, "realValue": 4},
        "P05": {"literal": "Cinco de Picas", "value": 5, "priority": 2, "realValue": 5},
        "P06": {"literal": "Seis de Picas", "value": 6, "priority": 2, "realValue": 6},
        "P07": {"literal": "Siete de Picas", "value": 7, "priority": 2, "realValue": 7},
        "P08": {"literal": "Ocho de Picas", "value": 8, "priority": 1, "realValue": 0.5},
        "P09": {"literal": "Nueve de Picas", "value": 9, "priority": 1, "realValue": 0.5},
        "P0J": {"literal": "Jota de Picas", "value": 10, "priority": 2, "realValue": 0.5},
        "P0Q": {"literal": "Dama de Picas", "value": 11, "priority": 2, "realValue": 0.5},
        "P0K": {"literal": "Rey de Picas", "value": 12, "priority": 2, "realValue": 0.5},

        "H01": {"literal": "As de Corazones", "value": 1, "priority": 3, "realValue": 1},
        "H02": {"literal": "Dos de Corazones", "value": 2, "priority": 3, "realValue": 2},
        "H03": {"literal": "Tres de Corazones", "value": 3, "priority": 3, "realValue": 3},
        "H04": {"literal": "Cuatro de Corazones", "value": 4, "priority": 3, "realValue": 4},
        "H05": {"literal": "Cinco de Corazones", "value": 5, "priority": 3, "realValue": 5},
        "H06": {"literal": "Seis de Corazones", "value": 6, "priority": 3, "realValue": 6},
        "H07": {"literal": "Siete de Corazones", "value": 7, "priority": 3, "realValue": 7},
        "H08": {"literal": "Ocho de Corazones", "value": 8, "priority": 3, "realValue": 0.5},
        "H09": {"literal": "Nueve de Corazones", "value": 9, "priority": 3, "realValue": 0.5},
        "H0J": {"literal": "Jota de Corazones", "value": 10, "priority": 3, "realValue": 0.5},
        "H0Q": {"literal": "Dama de Corazones", "value": 11, "priority": 3, "realValue": 0.5},
        "H0K": {"literal": "Rey de Corazones", "value": 12, "priority": 3, "realValue": 0.5},

        "D01": {"literal": "As de Diamantes", "value": 1, "priority": 4, "realValue": 1},
        "D02": {"literal": "Dos de Diamantes", "value": 2, "priority": 4, "realValue": 2},
        "D03": {"literal": "Tres de Diamantes", "value": 3, "priority": 4, "realValue": 3},
        "D04": {"literal": "Cuatro de Diamantes", "value": 4, "priority": 4, "realValue": 4},
        "D05": {"literal": "Cinco de Diamantes", "value": 5, "priority": 4, "realValue": 5},
        "D06": {"literal": "Seis de Diamantes", "value": 6, "priority": 4, "realValue": 6},
        "D07": {"literal": "Siete de Diamantes", "value": 7, "priority": 4, "realValue": 7},
        "D08": {"literal": "Ocho de Diamantes", "value": 8, "priority": 4, "realValue": 0.5},
        "D09": {"literal": "Nueve de Diamantes", "value": 9, "priority": 4, "realValue": 0.5},
        "D0J": {"literal": "Jota de Diamantes", "value": 10, "priority": 4, "realValue": 0.5},
        "D0Q": {"literal": "Dama de Diamantes", "value": 11, "priority": 4, "realValue": 0.5},
        "D0K": {"literal": "Rey de Diamantes", "value": 12, "priority": 4, "realValue": 0.5}
    }
}

contextGame = {"players": [], "round": 0, "maxRounds": 0, "deck": "baraja_esp", "bank": ""}

players = {
    "32324323A": {
        "name": "Pepe", "human": False, "bank": False, "initial_card": "", "priority": 0,
        "type": 30, "bet": 3, "points": 0, "cards": [], "round_points": 0},
    "11233455B": {
        "name": "Juan", "human": False, "bank": False, "initial_card": "", "priority": 0,
        "type": 40, "bet": 4, "points": 0, "cards": [], "round_points": 0},
    "99877654C": {
        "name": "David", "human": False, "bank": False, "initial_card": "", "priority": 0,
        "type": 50, "bet": 5, "points": 0, "cards": [], "round_points": 0}
}

menus = {
    "00": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 11 + "Seven and half", font="doom").center(100) +
                  "*" * 95 + "\n\n",
        "textOpts": "1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit",
        "inputOptText": "\nChoose an option:\n",
        "rangeList": [1, 2, 3, 4, 5, 6],
        "dict": {},
        "excep": []
    },
    "01": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 11 + "Players DB", font="doom").center(100) +
                  "*" * 95 + "\n\n",
        "textOpts": "1)New Human Player\n2)New Boot\n3)Show/Remove Players\n4)Go Back",
        "inputOptText": "\nOption:",
        "rangeList": [1, 2, 3, 4],
        "dict": {},
        "excep": []
    },
    "02": {
        "header": "",
        "textOpts": "",
        "inputOptText": "",
        "rangeList": [],
        "dict": {},
        "excep": []
    }
}
