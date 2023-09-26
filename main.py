"""CREDITS :
Maël
Mathieu
"""
# UTF-8

# LIBS IMPORTS
import os
import random

# FONCTIONS
def afficher_bâtons(nb_bâtons: int):
  """
  Affiche les btons sous forme graphique.

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons

            Returns:
                    Rien
  """
  print(f"Il reste {nb_bâtons} bâtons.\n" + nb_bâtons * "|")


def message_de_fin(nom_perdant: str):
  """
  Affiche le perdant.

            Parameters:
                    nom_perdant (str): Le nom du perdant

            Returns:
                    Rien
  """
  print(f"Le joueur {nom_perdant} à perdu, il a pris le dernier bâton.")
  input("Appuyez sur une touche pour continuer.")
  os.system("clear")


def bâtons_initialisation():
  """
  Initialise le jeu.

            Parameters:
                    Rien

            Returns:
                    nb_bâtons (int) : Le nombre de bâtons dans le jeu
                    bâtons_max (int) : Le nombre de bâtons retirabless par tour
  """
  nb_bâtons = int(
    input("Combien de bâtons voulez-vous mettre dans le jeu ? (minimum 1) : "))
  os.system("clear")

  while nb_bâtons < 1:
    nb_bâtons = int(input(f"{nb_bâtons} est inférieur à 1, réessayez. : "))
    os.system("clear")

  bâtons_max = int(
    input(
      "Combien de bâtons voulez-vous autoriser à récupérer ? (minimum 1) : "))
  os.system("clear")
  while bâtons_max < 1:
    bâtons_max = int(input(f"{bâtons_max} est inférieur à 1, réessayez. : "))
    os.system("clear")

  os.system("clear")
  return nb_bâtons, bâtons_max


def choisir_nom() -> str:
  """
  Permets à un joueur de choisir un nom.

            Parameters:
                    Rien

            Returns:
                    nom (str) : Le nom choisi
  """
  nom = input("Quel est le nom du joueur ? : ")
  while nom == "IA":
    nom = input(
      'Vous ne pouvez pas choisir "IA" comme nom de joueur, réessayez. : ')
  return nom


def player_versus_player_initialisation(nb_joueurs: int) -> list:
  """
  Initialise le mode de jeu pvp.

  Demande les noms de tous les joueurs.

            Parameters:
                    nb_joueurs (int): Le nombre de joueurs

            Returns:
                    nom_joueurs (list): Le nom des joueurs
  """
  nom_joueurs = []  # Liste de pseudos / noms

  for i in range(int(input("Combien il y aura-t-il de joueurs ? : "))):

    nom = input(f"Veuillez entrer un nom pour le joueur n°{i} : ")
    os.system("clear")

    while nom in nom_joueurs:
      nom = input(
        f"Le nom est déjà utilisé, entrez un autre nom pour le joueur n°{i} : "
      )
      os.system("clear")

    nom_joueurs.append(nom)

  return nom_joueurs


def tour_joueur(nom_joueur: str, nb_bâtons: int) -> int:
  """
  Lance le tour d'un joueur

            Parameters:
                    nom_joueur (str): Le nom du joueur
                    nb_bâtons (int): Le nombre de bâtons

            Returns:
                    bâtons (int): Le nombre de bâtons retirés
  """
  print(f"C'est au tour du joueur {nom_joueur}")

  bâtons_pris = int(
    input(f"Combien voulez-vous en prendre ? (entre 1 et {bâtons_max}) : "))
  os.system("clear")

  while bâtons_pris < 1 or bâtons_pris > bâtons_max:
    bâtons_pris = int(
      input(
        f"Le nombre que vous avez choisi n'est pas compris entre 1 et {bâtons_max}, réessayez. : "
      ))
    os.system("clear")

  return bâtons_pris


def tour_ia_facile(nb_bâtons: int, bâton_max: int) -> int:
  """
  Lance le tour de l'IA en mode facile

  Prends un nombre de bâtons random

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    bâtons (int): Le nombre de bâtons retirés
  """
  bâtons_pris = random.randint(1, bâton_max)
  return bâtons_pris


def tour_ia_difficile(nb_bâtons: int, nb_bâtons_max: int) -> int:
  """
  Lance le tour de l'IA en mode moyen et difficile.

  Fais la meilleure action possible. À l'aide d'un calcul super-mathématique (300iq)

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    bâtons (int): Le nombre de bâtons retirés
  """
  if nb_bâtons <= nb_bâtons_max:
    a_retirer = nb_bâtons - 1
    if a_retirer == 0:
      return 1
    else:
      return nb_bâtons - 1  # pour qu'il ne reste qu'un bâton
  else:
    reste = nb_bâtons % (
      nb_bâtons_max + 1
    )  # vérifie si le nombre de bâtons est un multiple de nb_bâtons_max
    if reste == 0:  # True
      return nb_bâtons_max
    elif reste == 1:  # False
      return 1
    elif reste <= nb_bâtons_max - 1:
      return reste - 1
    else:
      return nb_bâtons_max - 1  # DONE


def jeu(nom_joueurs: list,
        nb_bâtons: int,
        bâtons_max: int,
        ia: bool,
        difficulty=0):
  """
  Lance le jeu.

  Regroupe toutes les difficultés du joueur contre ia ainsi que le joueur contre joueur

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    bâtons (int): Le nombre de bâtons retirés
  """
  joueur_position = 0

  while nb_bâtons > 0:  # lancement du jeu
    afficher_bâtons(nb_bâtons)

    bâtons_a_retirer = 0
    if ia:
      if nom_joueurs[joueur_position] == "IA":
        if difficulty == 1:
          bâtons_a_retirer = tour_ia_facile(nb_bâtons, bâtons_max)
        elif difficulty == 3 or difficulty == 2:
          bâtons_a_retirer = tour_ia_difficile(nb_bâtons, bâtons_max)
      else:
        bâtons_a_retirer = tour_joueur(nom_joueurs[joueur_position], nb_bâtons)
    else:
      bâtons_a_retirer = tour_joueur(nom_joueurs[joueur_position], nb_bâtons)
    nb_bâtons = nb_bâtons - bâtons_a_retirer
    print(
      f"{nom_joueurs[joueur_position]} viens de retirer {bâtons_a_retirer}.")
    if nb_bâtons > 0:
      if joueur_position == len(nom_joueurs) - 1:
        joueur_position = 0
      else:
        joueur_position += 1

  message_de_fin(nom_joueurs[joueur_position])


def choix_difficultés(nb_bâtons: int, bâtons_max: int):
  """
  Choisis la difficulté de l'IA.

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    Rien
  """
  difficulté = 0
  while difficulté != 1 or difficulté != 2 or difficulté != 3:
    difficulté = int(
      input(
        """\t\tChoisissez la difficulté\n\n\t-1 Facile \n\t-2 Moyen \n\t-3 Difficile\n> """
      ))
    if difficulté == 1:
      os.system("clear")
      player_versus_ia_facile(nb_bâtons, bâtons_max)
      break
    elif difficulté == 2:
      os.system("clear")
      player_versus_ia_moyen(nb_bâtons, bâtons_max)
      break
    elif difficulté == 3:
      os.system("clear")
      player_versus_ia_difficile(nb_bâtons, bâtons_max)
      break


def player_versus_ia_facile(nb_bâtons: int, bâtons_max: int):  # random sur tout sans algo
  """
  Initialise et lance le jeu contre l'IA en mode FACILE.

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    Rien
  """
  nom = choisir_nom()
  liste_noms = [nom, "IA"]
  qui_commence = int(
    input("Choisissez qui commence :\n\n1 - Vous\n2 - IA\n> "))
  os.system("clear")
  while qui_commence != 1 and qui_commence != 2:
    qui_commence = int(input("Voulez-vous commencer (1 = oui, 2 = non) ? : "))
  if qui_commence == 2:
    liste_noms.reverse()

  jeu(liste_noms, nb_bâtons, bâtons_max, ia=True, difficulty=1)


def player_versus_ia_moyen(nb_bâtons: int, bâtons_max: int):
  """
  Initialise et lance le jeu contre l'IA en mode MOYEN.

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    Rien
  """
  nom = choisir_nom()
  liste_noms = [nom, "IA"]
  qui_commence = random.randint(0, 1)

  if qui_commence == 1:
    liste_noms.reverse()

  jeu(liste_noms, nb_bâtons, bâtons_max, ia=True, difficulty=2)


def player_versus_ia_difficile(nb_bâtons: int, bâtons_max: int):
  """
  Initialise et lance le jeu contre l'IA en mode DIFFICILE.

            Parameters:
                    nb_bâtons (int): Le nombre de bâtons dans le jeu
                    bâton_max (int): Le nombre de bâtons maximal retirable

            Returns:
                    Rien
  """
  # voir si l'IA commence
  qui_commence = nb_bâtons % (bâtons_max + 1) != 1
  liste_noms = [choisir_nom(), "IA"]
  if qui_commence == True:
    liste_noms.reverse()
  jeu(liste_noms, nb_bâtons, bâtons_max, True, 3)


# programme principal
# menu
while True:
  print("Regles: plusieurs personnes s'affrontent en récupérant des bâtons. La personne qui prend le dernier bâton perd.")
  print()
  choix = input("""\t\t---MENU---
  \t-1 Joueur contre joueur
  \n\t-2 Joueur contre ordinateur\n> """)
  os.system("clear")

  if choix == "1" or choix == "un":
    nb_bâtons, bâtons_max = bâtons_initialisation()
    nb_joueurs = int()
    jeu(player_versus_player_initialisation(nb_joueurs), nb_bâtons, bâtons_max, False)
  elif choix == "2" or choix == "de" or choix == "deux":
    nb_bâtons, bâtons_max = bâtons_initialisation()
    choix_difficultés(nb_bâtons, bâtons_max)



"""
Ce que nous voulions faire mais par manque de temps et d'argent nous n'avont pas pu faire : 
  - Une meilleure interface
    - Interactive par exemple
  - Un mode multijoueur
  - Un mode classé
  - Un système de points

"""
