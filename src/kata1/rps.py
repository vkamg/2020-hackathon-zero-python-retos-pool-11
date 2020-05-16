from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
ai = options[randint(0,2)]
player = input("Piedra, Papel o Tijera? ")

def quienGana(player, ai):

    if player == "Piedra":
        if ai == "Piedra":
            return "Empate!"
        elif ai == "Papel":
            return "Perdiste!"
        else:
            return "Ganaste!"

    elif player == "Papel":
        if ai == "Piedra":
            return "Ganaste!"
        elif ai == "Papel":
            return "Empate!"
        else:
            return "Perdiste!"
    
    else:
        if ai == "Piedra":
            return "Perdiste!"
        elif ai == "Papel":
            return "Ganaste!"
        else:
            return "Empate!"


# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

