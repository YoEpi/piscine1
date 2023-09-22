import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import os
import requests

# Fonction pour obtenir un mot aléatoire à partir d'une liste ou d'une API
def get_random_word():
    if os.path.exists("mots.txt"):
        with open("mots.txt", "r") as file:
            mots = file.read().splitlines()
        return random.choice(mots).lower()
    else:
        try:
            # Essayez d'obtenir un mot aléatoire depuis l'API Random Word API
            response = requests.get("https://random-word-api.herokuapp.com/word")
            response.raise_for_status()  # Vérifiez si la requête a réussi
            word = response.json()[0]  # Obtenez le premier mot de la réponse JSON
            return word.lower()
        except Exception as e:
            print("Erreur lors de la récupération du mot depuis l'API:", e)
            # Si une erreur se produit, utilisez une liste de mots de secours
            words = ["pomme", "banane", "cerise", "orange", "raisin"]
            return random.choice(words)

# Initialisation des variables de jeu
mot_a_deviner = get_random_word()
mot_masque = "_" * len(mot_a_deviner)
essais = 0
essais_max = 10  # Nombre d'essais maximum

# Initialisation des statistiques de jeu
nombre_victoires = 0
nombre_defaites = 0

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du Pendu")

# Créer un canvas pour dessiner le pendu
canvas = tk.Canvas(fenetre, width=200, height=200)
canvas.pack()

# Fonction pour dessiner le pendu (Remplacez par votre propre logique de dessin)
def dessiner_pendu():
    # Votre logique de dessin pour le pendu ici
    if essais >= 1:
        # Dessiner la base
        canvas.create_line(50, 180, 150, 180, width=3)
    if essais >= 2:
        # Dessiner le poteau
        canvas.create_line(100, 180, 100, 20, width=3)
    if essais >= 3:
        # Dessiner la poutre supérieure
        canvas.create_line(100, 20, 150, 20, width=3)
    if essais >= 4:
        # Dessiner la corde
        canvas.create_line(150, 20, 150, 40, width=3)
    if essais >= 5:
        # Dessiner la tête
        canvas.create_oval(135, 40, 165, 70, width=3)
    if essais >= 6:
        # Dessiner le corps
        canvas.create_line(150, 70, 150, 120, width=3)
    if essais >= 7:
        # Dessiner le bras gauche
        canvas.create_line(150, 80, 130, 100, width=3)
    if essais >= 8:
        # Dessiner le bras droit
        canvas.create_line(150, 80, 170, 100, width=3)
    if essais >= 9:
        # Dessiner la jambe gauche
        canvas.create_line(150, 120, 130, 140, width=3)
    if essais >= essais_max:
        # Dessiner la jambe droite
        canvas.create_line(150, 120, 170, 140, width=3)

# Fonction pour vérifier si une lettre fait partie du mot
def verifier_lettre(lettre):
    global mot_masque, essais
    if lettre in mot_a_deviner:
        mot_masque = "".join([lettre if c == lettre else m for c, m in zip(mot_a_deviner, mot_masque)])
        maj_affichage()
        verifier_victoire()
    else:
        essais += 1
        maj_affichage()
        dessiner_pendu()
        verifier_defaite()

# Fonction pour mettre à jour l'affichage
def maj_affichage():
    mot_label.config(text=mot_masque)
    essais_label.config(text=f"Essais: {essais}/{essais_max}")

# Fonction pour vérifier si le joueur a gagné
def verifier_victoire():
    global nombre_victoires
    nombre_victoires += 1
    maj_stats()
    if "_" not in mot_masque:
        temps_ecoule = (datetime.now() - debut_chrono).total_seconds()
        messagebox.showinfo("Victoire", f"Vous avez deviné le mot \"{mot_a_deviner}\" en {essais} essais en {temps_ecoule:.2f} secondes!")
        enregistrer_best_score(temps_ecoule)
        rejouer_partie()  # Commencer une nouvelle partie après la victoire

# Fonction pour vérifier si le joueur a perdu
def verifier_defaite():
    global nombre_defaites
    nombre_defaites += 1
    maj_stats()
    if essais >= essais_max:
        messagebox.showinfo("Défaite", f"Vous avez épuisé tous vos essais. Le mot était \"{mot_a_deviner}\".")
        rejouer_partie()  # Commencer une nouvelle partie après la défaite

# Fonction pour enregistrer le meilleur score
def enregistrer_best_score(temps_ecoule):
    best_scores_file = "best_scores.txt"
    if mot_a_deviner not in best_scores or essais < best_scores[mot_a_deviner][1] or (essais == best_scores[mot_a_deviner][1] and temps_ecoule < best_scores[mot_a_deviner][2]):
        best_scores[mot_a_deviner] = (datetime.now(), essais, temps_ecoule)
        with open(best_scores_file, "a") as file:
            file.write(f"{datetime.now()}, {mot_a_deviner}, {essais}, {temps_ecoule}\n")
            print("Meilleur score enregistré!")

# Fonction pour recommencer une nouvelle partie
def rejouer_partie():
    global mot_a_deviner, mot_masque, essais, debut_chrono
    mot_a_deviner = get_random_word()
    mot_masque = "_" * len(mot_a_deviner)
    essais = 0
    maj_affichage()
    dessiner_pendu()
    debut_chrono = datetime.now()

# Liste des lettres de l'alphabet
lettres_alphabet = [chr(i) for i in range(97, 123)]

# Fonction pour mettre à jour le clavier de l'alphabet
def maj_clavier_alphabet():
    for lettre in lettres_alphabet:
        lettre_btn = tk.Button(alphabet_frame, text=lettre, font=("Arial", 16),
                               command=lambda l=lettre: lettre_selectionnee(l))
        lettre_btn.grid(row=lettres_alphabet.index(lettre) // 6, column=lettres_alphabet.index(lettre) % 6, padx=5, pady=5)

# Fonction appelée lorsque le joueur sélectionne une lettre depuis le clavier
def lettre_selectionnee(lettre):
    verifier_lettre(lettre)
    lettres_alphabet.remove(lettre)
    maj_clavier_alphabet()

# Création des widgets Tkinter
mot_label = tk.Label(fenetre, text=mot_masque, font=("Arial", 24))
mot_label.pack(pady=20)

essais_label = tk.Label(fenetre, text=f"Essais: {essais}/{essais_max}", font=("Arial", 16))
essais_label.pack()

# Création d'un cadre pour le clavier de l'alphabet
alphabet_frame = tk.Frame(fenetre)
alphabet_frame.pack()

# Bouton pour recommencer une nouvelle partie
rejouer_button = tk.Button(fenetre, text="Rejouer", command=rejouer_partie, font=("Arial", 16))
rejouer_button.pack(pady=10)

# Initialisation du chronomètre
debut_chrono = datetime.now()

# Créer un cadre pour afficher les statistiques de jeu
stats_frame = tk.Frame(fenetre)
stats_frame.pack(pady=10)

victoires_label = tk.Label(stats_frame, text="Victoires: 0", font=("Arial", 16))
victoires_label.grid(row=0, column=0, padx=10)

defaites_label = tk.Label(stats_frame, text="Défaites: 0", font=("Arial", 16))
defaites_label.grid(row=0, column=1, padx=10)

pourcentage_victoires_label = tk.Label(stats_frame, text="Pourcentage de victoires: 0%", font=("Arial", 16))
pourcentage_victoires_label.grid(row=0, column=2, padx=10)

# Fonction pour mettre à jour les statistiques
def maj_stats():
    victoires_label.config(text=f"Victoires: {nombre_victoires}")
    defaites_label.config(text=f"Défaites: {nombre_defaites}")
    if nombre_victoires + nombre_defaites > 0:
        pourcentage_victoires = (nombre_victoires / (nombre_victoires + nombre_defaites)) * 100
        pourcentage_victoires_label.config(text=f"Pourcentage de victoires: {pourcentage_victoires:.2f}%")

# Charger les meilleurs scores depuis un fichier s'il existe
best_scores = {}
best_scores_file = "best_scores.txt"

if os.path.exists(best_scores_file):
    with open(best_scores_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 4:
                date_str, word, attempts_str, time_str = parts[:4]
                try:
                    date_str = date_str.split(".")[0]
                    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    attempts = int(attempts_str)
                    time = float(time_str)
                    best_scores[word] = (date, attempts, time)
                except (ValueError, IndexError):
                    continue

# Fonction pour mettre à jour le chronomètre
def maj_chrono():
    temps_actuel = datetime.now()
    duree = temps_actuel - debut_chrono
    chrono_label.config(text=f"Temps écoulé: {duree.seconds} secondes")
    if "_" not in mot_masque or essais >= essais_max:
        fenetre.quit()
    else:
        fenetre.after(1000, maj_chrono)

chrono_label = tk.Label(fenetre, text="Temps écoulé: 0 secondes", font=("Arial", 16))
chrono_label.pack()
maj_chrono()

# Démarrer le jeu
maj_affichage()
dessiner_pendu()
maj_clavier_alphabet()
maj_stats()  # Mettre à jour les statistiques au début du jeu

# Boucle principale Tkinter
fenetre.mainloop()
