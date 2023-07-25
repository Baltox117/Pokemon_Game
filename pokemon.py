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
my_pokemon_life = None
my_pokemon_attacks = None
my_pokemon_damages = None

enemy_pokemon_life = None
enemy_pokemon_attacks = None
enemy_pokemon_damages = None


SIZE_LIFE = 10

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
attacks_magikarp = ["Salpicadura", "Placaje", "Salpicadura", "Placaje"]
magikarp_damages = [0, 35, 0, 35]

opponent_messages = ["Preparate para un desafio.....",
                     "Parece que eres nuevo en esto, no tendre problemas en derrotarte", "No creo que puedas vencerme",
                     "Si quieres pasar por aqui, tendras que pelear conmigo...",
                     "Que mal pasaste enfrente de mi, vamos a pelear....", "Ey me miraste gracioso, vamos a pelear..."]

combats = 0

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
print("Te aventuraras en un pequeño mapa en donde tendras que derrotar\n"
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
my_pokemon = pokemons[pokemon_selected]
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
my_pokemon_life_copy = my_pokemon_life
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

                if trainer_in_cell:  # comienzo del combate pokemon
                    combat = True
                    pokemon_trainers.remove(trainer_in_cell)

            if map_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("{}".format(combat))

    if combat:
        os.system("cls")
        message = random.randint(0, len(opponent_messages) - 1)
        print("{}".format(opponent_messages[message]))
        opponent = random.randint(0, len(enable_pokemons) - 1)
        enemy = enable_pokemons[opponent]
        print("Tu rival es {}".format(enemy))
        input("                         Presione enter para continuar\n")
        if enemy == "Bulbasaur":
            enemy_pokemon_life = life_bulbasaur - 10
            enemy_pokemon_attacks = attacks_bulbasaur
            enemy_pokemon_damages = bulbasaur_damages
        elif enemy == "Squirtle":
            enemy_pokemon_life = life_squirtle - 10
            enemy_pokemon_attacks = attacks_squirtle
            enemy_pokemon_damages = squirtle_damages
        elif enemy == "Charmander":
            enemy_pokemon_life = life_charmander - 10
            enemy_pokemon_attacks = attacks_charmander
            enemy_pokemon_damages = charmander_damages
        elif enemy == "Pikachu":
            enemy_pokemon_life = life_pikachu - 10
            enemy_pokemon_attacks = attacks_pikachu
            enemy_pokemon_damages = pikachu_damages
        elif enemy == "Eevee":
            enemy_pokemon_life = life_eevee - 10 
            enemy_pokemon_attacks = attacks_eevee
            enemy_pokemon_damages = eevee_damages
        elif enemy == "Magikarp":
            enemy_pokemon_life = life_magikarp - 10
            enemy_pokemon_attacks = attacks_magikarp
            enemy_pokemon_damages = magikarp_damages
        print(enemy)
        print(enemy_pokemon_life)
        print(enemy_pokemon_attacks)
        print(enemy_pokemon_damages)
        
        my_life = my_pokemon_life
        my_combat_life = float
        my_attack = None
        enemy_life = enemy_pokemon_life
        enemy_combat_life = float
        enemy_attack = None
        # start pokemon battle 
        while my_pokemon_life > 0 and enemy_pokemon_life > 0:
            #enemy turn
            print("Turno de {}".format(enemy))
            enemy_attack = random.randint(0, len(enemy_pokemon_attacks))
            if enemy_attack == 1:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[0]))
                my_pokemon_life -= enemy_pokemon_damages[0]
            elif enemy_attack == 2:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[1]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            elif enemy_attack == 3:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[2]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            elif enemy_attack == 4:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[3]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            else: 
                print("{} no ha atacado".format(enemy))
            if my_pokemon_life < 0:
                my_pokemon_life = 0
            my_combat_life = int((my_pokemon_life * SIZE_LIFE)/my_life)
            print("{} [{}{}] {}/{}".format(my_pokemon, "#" * my_combat_life, " " * (SIZE_LIFE - my_combat_life), my_pokemon_life, my_life))
            enemy_combat_life = int((enemy_pokemon_life * SIZE_LIFE)/enemy_life)
            print("{} [{}{}] {}/{}".format(enemy, "#" * enemy_combat_life, " " * (SIZE_LIFE - enemy_combat_life), enemy_pokemon_life, enemy_life))
            input("                         Presione enter para continuar\n")
            os.system("cls")

            #player turn
            print("Turno de {}".format(my_pokemon))
            my_attack = None
            while my_attack not in [1, 2, 3, 4, 5]:
                my_attack = int(input("Que deberia hacer {}\n"
                                      "1.- {}\n"
                                      "2.- {}\n"
                                      "3.- {}\n"
                                      "4.- {}\n"
                                      "5.- No atacar \n"
                                      ": ".format(my_pokemon, my_pokemon_attacks[0], my_pokemon_attacks[1], my_pokemon_attacks[2], my_pokemon_attacks[3])))
            if my_attack == 1:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[0]))
                enemy_pokemon_life -= my_pokemon_damages[0]
            elif my_attack == 2:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[1]))
                enemy_pokemon_life -= my_pokemon_damages[1]
            elif my_attack == 3:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[2]))
                enemy_pokemon_life -= my_pokemon_damages[2]
            elif my_attack == 4:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[3]))
                enemy_pokemon_life -= my_pokemon_damages[3]
            else:
                print("{} no ha atacado".format(my_pokemon))
            if enemy_pokemon_life < 0:
                enemy_pokemon_life = 0
            my_combat_life = int((my_pokemon_life * SIZE_LIFE)/my_life)
            print("{} [{}{}] {}/{}".format(my_pokemon, "#" * my_combat_life, " " * (SIZE_LIFE - my_combat_life), my_pokemon_life, my_life))
            enemy_combat_life = int((enemy_pokemon_life * SIZE_LIFE)/enemy_life)
            print("{} [{}{}] {}/{}".format(enemy, "#" * enemy_combat_life, " " * (SIZE_LIFE - enemy_combat_life), enemy_pokemon_life, enemy_life))
            input("                         Presione enter para continuar\n")
            os.system("cls")
            
        if my_pokemon_life > enemy_pokemon_life:
            print("{} gana".format(my_pokemon))
            enable_pokemons.remove(enemy)
            combats += 1
            my_pokemon_life = my_pokemon_life_copy
        else:
            print("{} gana".format(enemy))
            my_pokemon_life = my_pokemon_life_copy
        
        combat = False

    if combat:
        os.system("cls")
        message = random.randint(0, len(opponent_messages) - 1)
        print("{}".format(opponent_messages[message]))
        opponent = random.randint(0, len(enable_pokemons) - 1)
        enemy = enable_pokemons[opponent]
        print("Tu rival es {}".format(enemy))
        input("                         Presione enter para continuar\n")
        if enemy == "Bulbasaur":
            enemy_pokemon_life = life_bulbasaur - 10
            enemy_pokemon_attacks = attacks_bulbasaur
            enemy_pokemon_damages = bulbasaur_damages
        elif enemy == "Squirtle":
            enemy_pokemon_life = life_squirtle - 10
            enemy_pokemon_attacks = attacks_squirtle
            enemy_pokemon_damages = squirtle_damages
        elif enemy == "Charmander":
            enemy_pokemon_life = life_charmander - 10
            enemy_pokemon_attacks = attacks_charmander
            enemy_pokemon_damages = charmander_damages
        elif enemy == "Pikachu":
            enemy_pokemon_life = life_pikachu - 10
            enemy_pokemon_attacks = attacks_pikachu
            enemy_pokemon_damages = pikachu_damages
        elif enemy == "Eevee":
            enemy_pokemon_life = life_eevee - 10 
            enemy_pokemon_attacks = attacks_eevee
            enemy_pokemon_damages = eevee_damages
        elif enemy == "Magikarp":
            enemy_pokemon_life = life_magikarp - 10
            enemy_pokemon_attacks = attacks_magikarp
            enemy_pokemon_damages = magikarp_damages
        
        my_life = my_pokemon_life
        my_combat_life = float
        my_attack = None
        enemy_life = enemy_pokemon_life
        enemy_combat_life = float
        enemy_attack = None
        # start pokemon battle 
        while my_pokemon_life > 0 and enemy_pokemon_life > 0:
            #enemy turn
            print("Turno de {}".format(enemy))
            enemy_attack = random.randint(0, len(enemy_pokemon_attacks))
            if enemy_attack == 1:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[0]))
                my_pokemon_life -= enemy_pokemon_damages[0]
            elif enemy_attack == 2:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[1]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            elif enemy_attack == 3:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[2]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            elif enemy_attack == 4:
                print("{} ha utilizado {}".format(enemy, enemy_pokemon_attacks[3]))
                my_pokemon_life -= enemy_pokemon_damages[1]
            else: 
                print("{} no ha atacado".format(enemy))
            if my_pokemon_life < 0:
                my_pokemon_life = 0
            my_combat_life = int((my_pokemon_life * SIZE_LIFE)/my_life)
            print("{} [{}{}] {}/{}".format(my_pokemon, "#" * my_combat_life, " " * (SIZE_LIFE - my_combat_life), my_pokemon_life, my_life))
            enemy_combat_life = int((enemy_pokemon_life * SIZE_LIFE)/enemy_life)
            print("{} [{}{}] {}/{}".format(enemy, "#" * enemy_combat_life, " " * (SIZE_LIFE - enemy_combat_life), enemy_pokemon_life, enemy_life))
            input("                         Presione enter para continuar\n")
            os.system("cls")

            #player turn
            print("Turno de {}".format(my_pokemon))
            my_attack = None
            while my_attack not in [1, 2, 3, 4, 5]:
                my_attack = int(input("Que deberia hacer {}\n"
                                      "1.- {}\n"
                                      "2.- {}\n"
                                      "3.- {}\n"
                                      "4.- {}\n"
                                      "5.- No atacar \n"
                                      ": ".format(my_pokemon, my_pokemon_attacks[0], my_pokemon_attacks[1], my_pokemon_attacks[2], my_pokemon_attacks[3])))
            if my_attack == 1:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[0]))
                enemy_pokemon_life -= my_pokemon_damages[0]
            elif my_attack == 2:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[1]))
                enemy_pokemon_life -= my_pokemon_damages[1]
            elif my_attack == 3:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[2]))
                enemy_pokemon_life -= my_pokemon_damages[2]
            elif my_attack == 4:
                print("{} ha utilizado {}".format(my_pokemon, my_pokemon_attacks[3]))
                enemy_pokemon_life -= my_pokemon_damages[3]
            else:
                print("{} no ha atacado".format(my_pokemon))
            if enemy_pokemon_life < 0:
                enemy_pokemon_life = 0
            my_combat_life = int((my_pokemon_life * SIZE_LIFE)/my_life)
            print("{} [{}{}] {}/{}".format(my_pokemon, "#" * my_combat_life, " " * (SIZE_LIFE - my_combat_life), my_pokemon_life, my_life))
            enemy_combat_life = int((enemy_pokemon_life * SIZE_LIFE)/enemy_life)
            print("{} [{}{}] {}/{}".format(enemy, "#" * enemy_combat_life, " " * (SIZE_LIFE - enemy_combat_life), enemy_pokemon_life, enemy_life))
            input("                         Presione enter para continuar\n")
            os.system("cls")
            
        if my_pokemon_life > enemy_pokemon_life:
            print("{} gana".format(my_pokemon))
            enable_pokemons.remove(enemy)
            combats += 1
            my_pokemon_life = my_pokemon_life_copy
        else:
            print("{} gana".format(enemy))
            my_pokemon_life = my_pokemon_life_copy
        
        combat = False

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
    
    if pokemon_trainers == []:
        break

    os.system("cls")
print("Fin del juego, gracias por jugar")
print("Has ganado {} combates".format(combats))