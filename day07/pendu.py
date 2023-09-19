import random

def charger_mots_depuis_fichier(nom_fichier):
    mots = []
    with open(mots, 'r') as file:
        for ligne in file:
            mot = ligne.strip()  # Supprimer les espaces et les sauts de ligne
            mots.append(mot)
    return mots

def choisir_mot(mots):
    return random.choice(mots)

# Charger la liste de mots depuis le fichier
liste_de_mots = charger_mots_depuis_fichier('mots_toFind.txt')

def jouer_pendu():
    mot_a_deviner = choisir_mot(liste_de_mots)
    lettres_trouvees = []

    print("Bienvenue dans le jeu du Pendu !")

    while True:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("\nMot à deviner : " + mot_cache)

        if set(mot_a_deviner) == set(lettres_trouvees):
            print("\nFélicitations, vous avez deviné le mot : " + mot_a_deviner)
            break

        lettre = input("Devinez une lettre : ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_trouvees.append(lettre)

        if lettre in mot_a_deviner:
            print("Bonne devinette !")
        else:
            print("Mauvaise devinette.")

if __name__ == "__main__":
    jouer_pendu()
