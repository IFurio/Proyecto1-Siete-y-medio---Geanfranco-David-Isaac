# Imports
from pyfiglet import figlet_format

players = {}

cardgame = {}

player_game = {}

player_game_round = {}

contextGame = {"players": [], "round": 1, "maxRounds": 2, "deck": "", "bank": ""}

letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
             "N", " J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

menus = {
    "00": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 11 + "Seven and half", font="doom") +
                  "*" * 95 + "\n\n",
        "textOpts": "1)Add/Remove/Show Players\n"
                    "2)Settings\n"
                    "3)Play Game\n"
                    "4)Ranking\n"
                    "5)Reports\n"
                    "6)Exit",
        "inputOptText": "\nChoose an option:\n",
        "rangeList": [1, 2, 3, 4, 5, 6],
        "dict": {},
        "excep": []
    },
    "01": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 12 + "P l a y e r s  D B", font="doom") +
                  "*" * 95 + "\n\n",
        "textOpts": "1)New Human Player\n"
                    "2)New Boot\n"
                    "3)Show/Remove Players\n"
                    "4)Go Back",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4],
        "dict": {},
        "excep": []
    },
    "02": {
        "header": "*" * 87 + "\n" +
                  figlet_format(" " + "S e tt i n g s", font="colossal") +
                  "*" * 87 + "\n\n",
        "textOpts": "1)Set Game Players\n"
                    "2)Set Card's Deck\n"
                    "3)Set Max Rounds (Default 5 Rounds)\n"
                    "4)Go Back",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4],
        "dict": {},
        "excep": []
    },
    "04": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 24 + "Ra n k i ng", font="doom") +
                  "*" * 95 + "\n\n",
        "textOpts": "1)Players With More Earnings\n"
                    "2)Players With More Games Played\n"
                    "3)Players With More Minutes Played\n"
                    "4)Go Back",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4],
        "dict": {},
        "excep": []
    },
    "05": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 24 + "R e p o r t s", font="doom") +
                  "*" * 95 + "\n\n",
        "textOpts": "1)  Initial card more repeated by each user,\n"                                                      
                    "only users who have played a minimum of 3 games.\n"
                    "2)  Player who makes the highest bet per game,\n"                                                    
                    "find the round with the highest bet.\n"
                    "3)  Player who makes the lowest bet per game.\n"
                    "4)  Percentage of rounds won per player in each game\n"                                              
                    "(%), as well as their average bet for the game.\n"
                    "5)  List of games won by Bots.\n"
                    "6)  Rounds won by the bank in each game.\n"
                    "7)  Number of users have been the bank in each game.\n"
                    "8)  Average bet per game.\n"
                    "9)  Average bet of the first round of each game.\n"
                    "10) Average bet of the last round of each game.\n"
                    "11)Go Back",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "dict": {},
        "excep": []
    },
    "06": {
        "header": "",
        "textOpts": "Select your profile:\n"
                    "1)Cautious\n"
                    "2)Moderated\n"
                    "3)Bold",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4],
        "dict": {},
        "excep": []
        },
    "game": {
        "header": "*" * 95 + "\n" +
                  figlet_format(" " * 11 + "Seven and half", font="doom") +
                  "*" * 95 + "\n\n",
        "textOpts": "1)Draw a card\n2)View your profile\n3)View the game stats\n4)Automatic play\n5)Give up your turn",
        "inputOptText": "Option: ",
        "rangeList": [1, 2, 3, 4, 5],
        "dict": {},
        "excep": []
    }
}
