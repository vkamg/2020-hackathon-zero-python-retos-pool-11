from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
ai = options[randint(0,2)]

def quienGana(player, ai):

    player_lower = player.lower()
    ai_lower = ai.lower()

    if player_lower == "piedra":
        if ai_lower == "piedra":
            return "Empate!"
        elif ai_lower == "papel":
            return "Perdiste!"
        else:
            return "Ganaste!"

    elif player_lower == "papel":
        if ai_lower == "piedra":
            return "Ganaste!"
        elif ai_lower == "papel":
            return "Empate!"
        else:
            return "Perdiste!"
    
    else:
        if ai_lower == "piedra":
            return "Perdiste!"
        elif ai_lower == "papel":
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

