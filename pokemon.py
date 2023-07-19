import os
import readchar
import random
from random import randint

# variables mapa
POS_X = 0
POS_Y = 1
NUM_OF_POKEMON_TRAINERS = 5
my_position = [3, 1]
pokemon_trainers = []

end_game = False

map_definition = """\
#######           #######
#######           #######
####                 ####
           #####         
          #######        
####        ###        ##
####                  ###
####                 ####
            ####         
          ########       
####        ####      ###
#######             #####
#######           #######\
"""

# variables pokemon

life_pikachu = 100
life_charmander = 100
life_squirtle = 100
life_bulbasaur = 100
life_eevee = 100
life_magikarp = 100

pokemons = ["Bulbasaur", "Squirtle", "Charmander", "Pikachu", "Eevee", "Magikarp"]
enable_pokemons = []  # pokemons disponibles para los entrenadores en el mapa
opponent = None
combat = False

attacks_pikachu = ["Impactrueno", "Rayo", "Trueno", "Rapidez"]
pikachu_damages = [25, 15, 20, 10]
attacks_charmander = ["Ascuas", "Lanzallamas", "Arañazo", "Cuchillada"]
charmander_damages = [25, 15, 10, 20]
attacks_squirtle = ["Burbuja", "Pistola Agua", "Cabezazo", "Placaje"]
squirtle_damages = [15, 25, 10, 20]
attacks_bulbasaur = ["Drenadoras", "Latigo Cepa", "Hoja Afilada", "Placaje"]
bulbasaur_damages = [15, 15, 20, 20]
attacks_eevee = ["Placaje", "Latigo", "Gruñido", "Ataque Rapido"]
eevee_damages = [20, 15, 15, 20]
attacks_magikarp = ["Salpicadura", "Placaje"]
magikarp_damages = [0, 35]

opponent_messages = ["Preparate para un desafio.....",
                     "Parece que eres nuevo en esto, no tendre problemas en derrotarte", "No creo que puedas vencerme",
                     "Si quieres pasar por aqui, tendras que pelear conmigo...",
                     "Que mal pasaste enfrente de mi, vamos a pelear....", "Ey me miraste gracioso, vamos a pelear..."]

vida_pikachu = 80
vida_squirtle = 90
vida_inicial_pikachu = vida_pikachu
vida_inicial_squirtle = vida_squirtle
vida_combate_pikachu = float
vida_combate_squirtle = float
tam_vida = 10

# Game Start
print("""\n
########      ######    ##      ##  ###########	 ##         ##    ######    ##      ##
##      ##  ##      ##  ##    ##    ##           ####     ####  ##      ##  ###     ##
##      ##  ##      ##  ##  ##      ##           ##  ## ##  ##  ##      ##  ## #    ##
########    ##      ##  ####        #########    ##    #    ##  ##      ##  ##  #   ##
##          ##      ##  ##  ##      ##           ##         ##  ##      ##  ##   #  ##
##          ##      ##  ##    ##    ##           ##         ##  ##      ##  ##    ####
##            ######    ##      ##  ###########	 ##         ##    ######    ##      ##
""")
input("                         Presione enter para continuar\n")
os.system("cls")

print("Hola soy Baltox y he creado esta pequeña aventura pokemon\n")
input("Te aventuraras en un pequeño mapa en donde tendras que derrotar\n"
      "a 5 entrenadores pokemon los cuales estan representados como *\n"
      "por el mapa,¿Podras demostrar que eres el mejor entrenador pokemon?\n")

print("Para comenzar tu aventura tendras que elegir a tu pokemon con el cual\n"
      "combatiras.")
pokemon_selected = int(input("Selecciona el numero del pokemon que deseas utilizar\n"
                             "1.-Bulbasaur\n"
                             "2.-Squirtle\n"
                             "3.-Charmander\n"
                             "4.-Pikachu\n"
                             "5.-Eevee\n"
                             "6.-Magikarp\n"
                             ": "))
pokemon_selected = pokemon_selected - 1
print("Bien has seleccionado a {} como tu pokemon, suerte en tu aventura y que te diviertas".format(pokemons[pokemon_selected]))
if pokemons[pokemon_selected] == "Bulbasaur":
    my_pokemon_life = life_bulbasaur + 10
    my_pokemon_attacks = attacks_bulbasaur
    my_pokemon_damages = bulbasaur_damages
elif pokemons[pokemon_selected] == "Squirtle":
    my_pokemon_life = life_squirtle + 10
    my_pokemon_attacks = attacks_squirtle
    my_pokemon_damages = squirtle_damages
elif pokemons[pokemon_selected] == "Charmander":
    my_pokemon_life = life_charmander + 10
    my_pokemon_attacks = attacks_charmander
    my_pokemon_damages = charmander_damages
elif pokemons[pokemon_selected] == "Pikachu":
    my_pokemon_life = life_pikachu + 10
    my_pokemon_attacks = attacks_pikachu
    my_pokemon_damages = pikachu_damages
elif pokemons[pokemon_selected] == "Eevee":
    my_pokemon_life = life_eevee + 10
    my_pokemon_attacks = attacks_eevee
    my_pokemon_damages = eevee_damages
elif pokemons[pokemon_selected] == "Magikarp":
    my_pokemon_life = life_magikarp + 10
    my_pokemon_attacks = attacks_magikarp
    my_pokemon_damages = magikarp_damages

for pokemon in pokemons:
    if pokemon != pokemons[pokemon_selected]:
        enable_pokemons.append(pokemon)

print(enable_pokemons)
print(my_pokemon_life)
print(my_pokemon_attacks)
print(my_pokemon_damages)


input("                         Presione enter para continuar\n")

os.system("cls")
# """
# Create map
map_definition = [list(row) for row in map_definition.split("\n")]
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

# Genererate my position
while True:
    my_new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if map_definition[my_new_position[POS_Y]][my_new_position[POS_X]] != "#":
        my_position = my_new_position
        break

# Generate random pokemon trainers on the map
while len(pokemon_trainers) < NUM_OF_POKEMON_TRAINERS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if new_position not in pokemon_trainers and new_position != my_position and map_definition[new_position[POS_Y]][
        new_position[POS_X]] != "#":
        pokemon_trainers.append(new_position)

# Main Loop
while not end_game:
    os.system("cls")
    # Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            trainer_in_cell = None

            for trainer in pokemon_trainers:
                if trainer[POS_X] == cordinate_x and trainer[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    trainer_in_cell = trainer

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

                if trainer_in_cell:  # comienzo del combate pokemonq
                    os.system("cls")
                    combat = True
                    pokemon_trainers.remove(trainer_in_cell)

            if map_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if map_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    if combat == True:
        os.system("cls")
        message = random.randint(0, len(opponent_messages))
        print("{}".format(opponent_messages[message]))
        opponent = random.randint(0, len(enable_pokemons))
        enemy = enable_pokemons[opponent]
        print("Tu rival es {}".format(enemy))
        combat = False

    os.system("cls")