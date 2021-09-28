import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_DE_VIES = 4


nombre = 0
vies = NOMBRE_DE_VIES


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0 :
        nombre_str = input(f"Devine quel est le nombre magique. Il est situé entre {nb_min} et {nb_max} : ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR : Vous devez entrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR : Le nombre doit être entre {nb_min} et {nb_max} ! Réessayez.")
                nombre_int = 0
    return nombre_int




while not nombre ==  NOMBRE_MAGIQUE and vies > 0 :
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo ! Vous avez trouvé le nombre magique")
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre est plus petit")
        vies -= 1
        print(f"Il vous reste {vies} vies")
    else:
        print("le nombre est plus grand")
        vies -= 1
        print(f"Il vous reste {vies} vies")

if vies == 0 :
    print(f"Vous avez perdu. Le nombre magique était : {NOMBRE_MAGIQUE}")


