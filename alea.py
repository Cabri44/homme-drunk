from random import *
from math import *
import numpy as np
from time import *
import matplotlib.pyplot as plt
import os
plt.style.use("fivethirtyeight")

def testn(n, d_0):
    compteur = 0
    simulations = 10000
    
    for _ in range(simulations):
        position = d_0
        i = 0
        
        while position != 0 and i < n:
            # Utiliser getrandbits pour un pas aléatoire plus rapide
            position += 1 if getrandbits(1) else -1
            i += 1

        if position != 0:
            compteur += 1

    return compteur / simulations


def test(n, d_0):           #compte qui revient quand on est en 1D
    compteur = 0
    for _ in range(10000):
        position = d_0
        i = 0
        while position != 0 and i < n:
            b = random( )
            if b>0.5:
                position += 1
            else:
                position -= 1
            i += 1
        if position != 0:
            compteur += 1
    return compteur / 10000



def test2(n, x, y):     #compte qui revient en 2D
    compteur = 0
    for _ in range(10000):
        position_x = x
        position_y = y
        i = 0
        while position_x != 0 and position_y != 0 and i < n:
            b = randint(0, 3)
            if b == 0:
                position_x += 1
            if b == 1:
                position_x -= 1
            if b == 2:
                position_y += 1
            else:
                position_y -= 1
            i += 1
        if position_x != 0 or position_y != 0:
            compteur += 1
    return compteur / 10000


def retour_1(n): # moyenne du premier temps de retour en 1D
    resultat = []
    for i in range(n):
        position = 0
        compteur = 0
        while position != 0 and compteur < 1000000 or compteur == 0:
            b = random()
            if b>0.5:
                position += 1
            else:
                position -= 1
            compteur += 1
        if compteur == 1000000:
            resultat.append(1000000)
        else:
            resultat.append(compteur)
    return resultat

def retour_1n(n):
    somme_retours = 0
    seuil = 1000000  # Limite maximale pour éviter des boucles infinies
    
    for _ in range(n):
        position = 0
        compteur = 0
        
        while True:
            # Générer un pas aléatoire (-1 ou +1)
            position += 1 if getrandbits(1) else -1
            compteur += 1
            
            # Conditions de sortie
            if position == 0 or compteur >= seuil:
                break
        
        # Ajouter le temps de retour ou la limite au total
        somme_retours += compteur if compteur < seuil else seuil

    # Retourner la moyenne des temps
    return somme_retours / n

def moyenne(l): 
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return (sum // len(l)) #partie entière de la moyenne

"""
og = time()
print("le test normal", moyenne(retour_1(100000)))
prem = time()
print(prem -og)
print("le test n:", retour_1n(100000))
deuz = time()
print(deuz - prem)
"""

def retour_2(n): # moyenne du premier temps de retour en 2D
    resultat = []
    for i in range(n):
        position_x = 0
        position_y = 0
        compteur = 0
        while (position_x != 0 or position_y != 0 ) and compteur < 100000 or compteur == 0:
            b = randint(0, 3)
            if b == 0:
                position_x += 1
            if b == 1:
                position_x -= 1
            if b == 2:
                position_y += 1
            else:
                position_y -= 1
            compteur += 1
        if compteur == 100000:
            resultat.append(100000)
        else:
            resultat.append(compteur)
    return resultat



def nombre_cases_visitees(n, pas):
    resultat = 0
    for _ in range(n):
        position = 0
        visited = {0}  # La case 0 est visitée au départ
        
        for _ in range(pas):
            # Générer un pas aléatoire (-1 ou +1)
            position += 1 if getrandbits(1) else -1
            visited.add(position)  # Ajouter la position au set
        
        resultat += len(visited)  # Nombre de cases visitées uniques

    return resultat/n

#resultat1= []
#for i in range(1000):
#   resultat1.append(nombre_cases_visitees(1,100000)[0])
#print(moyenne(resultat1))
#print("la val théorique est ", 1.596 * 316.2)


def collect_data(debut,n_values, simulations=1000, filename="resultat.txt"):
    """
    Collecte les données expérimentales et les compare à la valeur théorique.
    Les résultats sont stockés dans un fichier texte.
    
    - n_values : Liste des longueurs de marche.
    - simulations : Nombre de répétitions par longueur.
    - filename : Nom du fichier de sortie.
    """
    with open(filename, "w") as f:
        f.write("n\tExperimental\tTheoretical\n")
        f.write("-" * 40 + "\n")
        
        for n in range(debut,n_values +1):
            experimental = nombre_cases_visitees(simulations,n)
            theoretical = 2 * sqrt(2) * sqrt(n) / sqrt(pi)
            f.write(f"{n}\t{experimental:.5f}\t{theoretical:.5f}\n")
            print(f"n={n}, Experimental={experimental:.5f}, Theoretical={theoretical:.5f}")

def collect_data2(n_values, simulations=1000, filename="resultat.txt"):
    """
    Continue d'ajouter les résultats expérimentaux dans un fichier texte existant,
    à partir de la valeur `debut + 1` jusqu'à `n_values`.
    
    - debut : Valeur de départ (inclus).
    - n_values : Valeur finale (inclus).
    - simulations : Nombre de répétitions par longueur.
    - filename : Nom du fichier de sortie (par défaut "resultat.txt").
    """
    # Lire le fichier existant pour vérifier où nous en sommes
    with open(filename, "r") as f:
        lines = f.readlines()

    # Récupérer la dernière valeur de n déjà présente dans le fichier
    last_value = 0
    if len(lines) > 2:  # Si le fichier contient des données
        last_line = lines[-1]
        last_value = int(last_line.split("\t")[0])  # Récupère la première valeur de la dernière ligne
    
    
    # Ouvrir le fichier en mode ajout pour ne pas écraser les données existantes
    with open(filename, "a") as f:
        for n in range(last_value, n_values + 1):
            experimental = nombre_cases_visitees(simulations,n)
            theoretical = 2 * sqrt(2) * sqrt(n) / sqrt(pi)
            
            # Écriture des résultats dans le fichier
            f.write(f"{n}\t{experimental:.5f}\t{theoretical:.5f}\n")
            print(f"n={n}, Experimental={experimental:.5f}, Theoretical={theoretical:.5f}")

#collect_data2(20100)

def plot_from_file(filename="resultat.txt",output="cases_parcourues.png"):
    # Initialisation des listes pour stocker les données
    n_values = []
    experimental_data = []
    theoretical_data = []
    
    # Lecture du fichier résultat.txt
    with open(filename, "r") as f:
        # Ignorer l'en-tête
        next(f)
        next(f)
        for line in f:
            # Lire les valeurs pour chaque ligne
            n, experimental, theoretical = line.split('\t')
            n_values.append(int(n))
            experimental_data.append(float(experimental))
            theoretical_data.append(float(theoretical))
    
    # Traçage des courbes
    plt.figure(figsize=(10, 6))
    
    # Courbe expérimentale
    plt.plot(n_values, experimental_data, label="Expérimental", color="blue", linestyle="--")
    
    # Courbe théorique
    plt.plot(n_values, theoretical_data, label="Théorique", color="red", linestyle="-")
    
    # Étiquettes et titre
    plt.xlabel("Longueur de la marche (n)", fontsize=12)
    plt.ylabel("Nombre de cases visitées", fontsize=12)
    plt.title("Nombre de cases visitées : expérimental vs théorique", fontsize=14)
    
    # Légende
    plt.legend()
    
    # Affichage de la courbe
    plt.grid(True)
    plt.savefig(output)
    plt.show()

#plot_from_file("resultat_2D.txt","cases_parcourues_2D.png")
def max_ecart(filename="resultat.txt"):
    """
    Trouve le plus grand écart relatif entre les valeurs théoriques et expérimentales
    dans le fichier donné.

    - filename : Nom du fichier contenant les données.
    Retourne :
    - position (list) : [n, theoretical, experimental] pour le plus grand écart.
    - plus_grand (float) : Valeur de l'écart relatif maximal.
    """
    plus_grand = 0
    position = [0, 0, 0]  # Format : [n, theoretical, experimental]

    with open(filename, "r") as f:
        # Ignorer les 100 premières lignes (on veut un truc asymptotique)
        for i in range(100):
            next(f)
        
        for line in f:
            # Découpe de la ligne et conversion des valeurs
            n, experimental, theoretical = line.split('\t')
            n = int(n)
            experimental = float(experimental)
            theoretical = float(theoretical)
            
            # Calcul de l'écart relatif
            ecart_relatif = abs(theoretical - experimental) / theoretical
            
            # Mise à jour si un écart plus grand est trouvé
            if ecart_relatif > plus_grand:
                position = [n, theoretical, experimental]
                plus_grand = ecart_relatif

    return position, plus_grand
    

def proportion_retour(n, max_p, filename="retour_1D.txt"):
    """
    Calcule la proportion de marches aléatoires revenant en 0 avant chaque pas jusqu'à max_p.
    
    - n : Nombre de marches aléatoires à simuler.
    - max_p : Nombre maximal de pas à considérer.
    - filename : Nom du fichier de sortie.
    """
    # Initialiser un tableau pour compter les retours à 0
    retours = [0] * (max_p + 1)

    for _ in range(n):
        position = 0
        for step in range(1, max_p + 1):
            # Marche aléatoire 1D
            position += 1 if getrandbits(1) else -1
            
            # Si la marche revient à 0
            if position == 0:
                retours[step] += 1
                break  # Arrêter la marche, car elle est déjà revenue à 0

    # Calculer les proportions cumulées
    proportions = [sum(retours[:i+1]) / n for i in range(max_p + 1)]

    # Écrire les résultats dans un fichier
    with open(filename, "w") as f:
        f.write("Pas\tProportion\n")
        for step, proportion in enumerate(proportions):
            f.write(f"{step}\t{proportion:.5f}\n")
    
    print(f"Les résultats ont été enregistrés dans {filename}.")

# Exemple d'utilisation
#proportion_retour(n=10000, max_p=100000, filename="retour_1D.txt")

def proportion_retour_2D(n, max_p, filename="retour_2D_01.txt"):
    """
    Calcule la proportion de marches aléatoires 2D revenant en (0, 0) avant chaque pas jusqu'à max_p.

    - n : Nombre de marches aléatoires à simuler.
    - max_p : Nombre maximal de pas à considérer.
    - filename : Nom du fichier de sortie.
    """
    # Initialiser un tableau pour compter les retours à (0, 0)
    retours = [0] * (max_p + 1)

    for _ in range(n):
        position = [0, 0]
        for step in range(1, max_p + 1):
            # Marche aléatoire 2D : choix entre les 4 directions possibles
            direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            position[0] += direction[0]
            position[1] += direction[1]

            # Si la marche revient à (0, 0)
            if position == [0, 0]:
                retours[step] += 1
                break  # Arrêter la marche, car elle est déjà revenue à (0, 0)

    # Calculer les proportions cumulées
    proportions = [sum(retours[:i+1]) / n for i in range(max_p + 1)]

    # Écrire les résultats dans un fichier
    with open(filename, "w") as f:
        f.write("Pas\tProportion\n")
        for step, proportion in enumerate(proportions):
            f.write(f"{step}\t{proportion:.5f}\n")
    
    print(f"Les résultats ont été enregistrés dans {filename}.")

# Exemple d'utilisation
#proportion_retour_2D(n=500, max_p=1000000)


def proportion_retour_3D(n, max_p, filename="retour_3D.txt"):
    """
    Calcule la proportion de marches aléatoires 3D revenant en (0, 0, 0) avant chaque pas jusqu'à max_p.

    - n : Nombre de marches aléatoires à simuler.
    - max_p : Nombre maximal de pas à considérer.
    - filename : Nom du fichier de sortie.
    """
    # Initialiser un tableau pour compter les retours à (0, 0, 0)
    retours = [0] * (max_p + 1)

    for _ in range(n):
        position = [0, 0, 0]
        for step in range(1, max_p + 1):
            # Marche aléatoire 3D : choix entre les 6 directions possibles
            direction = choice([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
            position[0] += direction[0]
            position[1] += direction[1]
            position[2] += direction[2]

            # Si la marche revient à (0, 0, 0)
            if position == [0, 0, 0]:
                retours[step] += 1
                break  # Arrêter la marche, car elle est déjà revenue à (0, 0, 0)

    # Calculer les proportions cumulées
    proportions = [sum(retours[:i+1]) / n for i in range(max_p + 1)]

    # Écrire les résultats dans un fichier
    with open(filename, "w") as f:
        f.write("Pas\tProportion\n")
        for step, proportion in enumerate(proportions):
            f.write(f"{step}\t{proportion:.5f}\n")
    
    print(f"Les résultats ont été enregistrés dans {filename}.")

# Exemple d'utilisation
# proportion_retour_3D(n=1000, max_p=10000)

def proportion_retour_5D(n, max_p, filename="retour_5D.txt"):
    """
    Calcule la proportion de marches aléatoires 5D revenant en (0, 0, 0, 0, 0) avant chaque pas jusqu'à max_p.

    - n : Nombre de marches aléatoires à simuler.
    - max_p : Nombre maximal de pas à considérer.
    - filename : Nom du fichier de sortie.
    """
    # Initialiser un tableau pour compter les retours à (0, 0, 0, 0, 0)
    retours = [0] * (max_p + 1)

    for _ in range(n):
        position = [0, 0, 0, 0, 0]
        for step in range(1, max_p + 1):
            # Marche aléatoire 5D : choix entre les 10 directions possibles
            direction = choice([
                (1, 0, 0, 0, 0), (-1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0), (0, -1, 0, 0, 0),
                (0, 0, 1, 0, 0), (0, 0, -1, 0, 0),
                (0, 0, 0, 1, 0), (0, 0, 0, -1, 0),
                (0, 0, 0, 0, 1), (0, 0, 0, 0, -1)
            ])
            position[0] += direction[0]
            position[1] += direction[1]
            position[2] += direction[2]
            position[3] += direction[3]
            position[4] += direction[4]

            # Si la marche revient à (0, 0, 0, 0, 0)
            if position == [0, 0, 0, 0, 0]:
                retours[step] += 1
                break  # Arrêter la marche, car elle est déjà revenue à (0, 0, 0, 0, 0)

    # Calculer les proportions cumulées
    proportions = [sum(retours[:i+1]) / n for i in range(max_p + 1)]

    # Écrire les résultats dans un fichier
    with open(filename, "w") as f:
        f.write("Pas\tProportion\n")
        for step, proportion in enumerate(proportions):
            f.write(f"{step}\t{proportion:.5f}\n")
    
    print(f"Les résultats ont été enregistrés dans {filename}.")

def lire_fichier(filename):
    """
    Lit un fichier et retourne une liste des proportions.
    - filename : Nom du fichier à lire.
    """
    proportions = []
    with open(filename, "r") as f:
        next(f)  # Sauter l'en-tête
        for line in f:
            _, proportion = line.strip().split("\t")
            proportions.append(float(proportion))
    return proportions

def lire_fichier(filename):
    """
    Lit un fichier et retourne une liste des proportions.
    - filename : Nom du fichier à lire.
    """
    proportions = []
    with open(filename, "r") as f:
        next(f)  # Sauter l'en-tête
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                _, proportion = parts
                proportions.append(float(proportion))
    return proportions

def tracer_graphique(fichiers, labels, output="comparaison_retours.png"):
    """
    Trace un graphique comparant les proportions cumulées de retour pour plusieurs fichiers.

    - fichiers : Liste des noms des fichiers contenant les données.
    - labels : Liste des labels à afficher dans la légende.
    - output : Nom du fichier de sortie pour le graphique.
    """
    for fichier, label in zip(fichiers, labels):
        proportions = lire_fichier(fichier)
        plt.plot(range(len(proportions)), proportions, label=label)

    plt.xlabel("Nombre de pas")
    plt.ylabel("Proportion de marches revenues")
    plt.title("Comparaison des proportions de retour")
    plt.legend()
    plt.grid(True)
    plt.savefig(output)
    plt.show()

def nombre_cases_visitees_2D(simulations, pas):
    """
    Calcule le nombre moyen de cases uniques visitées dans une marche aléatoire en 2D.

    - simulations : Nombre de marches aléatoires à simuler.
    - pas : Nombre de pas dans chaque marche.

    Retourne la moyenne des cases uniques visitées.
    """
    total_cases = 0

    for _ in range(simulations):
        position = (0, 0)  # Position initiale (x, y)
        visited = {position}  # Ensemble des cases visitées

        for _ in range(pas):
            # Faire un pas aléatoire dans l'une des 4 directions possibles
            direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            position = (position[0] + direction[0], position[1] + direction[1])
            visited.add(position)  # Ajouter la position actuelle

        total_cases += len(visited)  # Accumuler les cases uniques visitées

    return total_cases / simulations


def collect_data_2D(n_values, simulations=1000, filename="resultat_2D.txt"):
    """
    Collecte et enregistre les données sur le nombre moyen de cases visitées en 2D,
    en ajoutant au fichier existant si nécessaire.

    - n_values : Valeur maximale de `pas` (nombre de pas) à simuler.
    - simulations : Nombre de marches à simuler pour chaque valeur de `pas`.
    - filename : Nom du fichier de sortie.
    """
    # Vérifier où commencer à partir du fichier
    last_value = 0
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            if len(lines) > 1:  # Vérifie s'il y a des données existantes
                last_line = lines[-1]
                last_value = int(last_line.split("\t")[0])  # Dernière valeur de `pas` simulée
    except FileNotFoundError:
        # Si le fichier n'existe pas encore, on part de zéro
        pass

    # Ouvrir le fichier en mode ajout
    with open(filename, "a") as f:
        if last_value == 0:  # Ajouter un en-tête si le fichier est vide
            f.write("Pas\tExperimental\tTheoretical\n")
        
        # Calculer et ajouter les nouvelles données
        for pas in range(last_value + 1, n_values + 1):
            experimental = nombre_cases_visitees_2D(simulations, pas)
            theoretical = (2/5) * pas  # Approximation théorique
            f.write(f"{pas}\t{experimental:.5f}\t{theoretical:.5f}\n")
            print(f"Pas={pas}, Experimental={experimental:.5f}, Theoretical={theoretical:.5f}")

#collect_data_2D(n_values=1000, simulations=1000, filename="resultat_2D.txt")
# Exemple d'utilisation
fichiers = ["retour_1D.txt", "retour_2D.txt", "retour_3D.txt", "retour_5D.txt"]
labels = ["1D", "2D", "3D", "5D"]

def marche_aleatoire_1d(n, d):
    """
    Simule une marche aléatoire en 1D de n individus, chacun effectuant d pas.
    
    n : nombre de marches
    d : nombre de pas à faire avant d'arrêter la marche
    """
    # Initialisation d'un tableau pour les positions finales
    positions = np.zeros(n)
    
    for i in range(n):
        # Chaque marcheur fait d pas, avec une chance sur deux de choisir droite ou gauche
        pas = np.random.choice([-1, 1], size=d)  # -1 pour gauche, 1 pour droite
        positions[i] = pas.sum()  # La somme des pas donne la position finale
    
    # Calculer les limites des positions possibles
    min_pos = -d
    max_pos = d
    
    # Créer des bords de bins pour regrouper deux positions consécutives par barre
    bins = np.arange(min_pos - 1, max_pos + 2, 2)  # De -d à d avec un pas de 2
    
    # Affichage de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.hist(positions, bins=bins, edgecolor='black', align='mid')
    plt.title(f'Distribution des positions de {n} marches après {d} pas')
    plt.xlabel('Position finale')
    plt.ylabel('Fréquence')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Ajustement des marges pour que le titre et les labels soient visibles
    plt.tight_layout()
    
    # Sauvegarder l'histogramme dans un fichier PNG
    plt.savefig("histogramme.png")
    plt.close()  # Ferme la figure pour libérer la mémoire

# Exemple d'appel
#marche_aleatoire_1d(n=1000000, d=100)

# Définir les directions de la marche
directions = ['gauche', 'gauche', 'droite', 'gauche', 'droite', 'droite']

def marche_aleatoire_graphique(directions, k):
    """
    Trace un graphique 1D représentant la marche aléatoire avec un point rouge 
    pour la position après le k-ième pas, et une flèche courbée représentant
    le dernier mouvement en rouge.
    """
    # Initialiser la position à 0
    position = 0
    positions = [position]
    
    # Appliquer les mouvements spécifiés jusqu'à l'étape k
    for i in range(k):
        direction = directions[i]
        if direction == 'gauche':
            position -= 1
        elif direction == 'droite':
            position += 1
        positions.append(position)
    
    # Créer un graphique avec des points alignés horizontalement (y = 0)
    plt.figure(figsize=(6, 2))
    
    # Points bleus sur la ligne de -3 à 3 (7 points)
    plt.plot(np.arange(-3, 4), [0]*7, 'bo-', markersize=8, linewidth=2)
    
    # Ajouter un point rouge à la position après k pas
    plt.plot(positions[k], 0, 'ro', markersize=8)
    
    # Ajouter une flèche courbée représentant le dernier mouvement en rouge
    if k > 0:
        # Dernière position avant le mouvement
        start_pos = positions[k - 1]
        end_pos = positions[k]
        
        # Tracer une flèche courbée (avec un arc de cercle entre les deux points)
        plt.annotate('', xy=(end_pos, 0), xytext=(start_pos, 0),
                     arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.3", color='red', lw=2))
    
    # Ajuster les limites de l'axe y pour qu'il soit fixe à 0
    plt.ylim(-1, 1)  # Limite sur l'axe y (la marche reste sur la ligne horizontale)
    
    # Masquer les ticks et les axes
    plt.xticks(np.arange(-3, 4))  # Limites de l'axe x de -3 à 3
    plt.yticks([])  # Masquer les ordonnées
    
    # Enlever les axes et la grille
    plt.axis('off')

    # Sauvegarder le graphique sous le nom "marche1D.k.png"
    plt.savefig(f"marche1D.{k}.png")
    plt.close()  # Fermer la figure pour libérer de la mémoire

def marche_10000(d,max_p = 10000, n = 1000,filename = "marche_10000_13"):
    retours = [0] * (max_p + 1)
    possibilités = []
    for i in range(d):
        a = [0] * d
        b = [0] * d
        a[i] = 1
        b[i] = -1
        possibilités.append(a.copy())
        possibilités.append(b.copy())
    position_0 = [0 for _ in range(d)]
    for _ in range(n):
        position = [0 for _ in range(d)]
        for step in range(1, max_p + 1):
            direction = choice(possibilités)
            position = [position[i] + direction[i] for i in range(d)]
            if position == position_0:
                retours[step] += 1
                break

    proportions = [sum(retours[:i+1]) / n for i in range(max_p + 1)]
    with open(filename, "w") as f:
        f.write("Pas\tProportion\n")
        for step, proportion in enumerate(proportions):
            f.write(f"{step}\t{proportion:.5f}\n")

    print(f"Les résultats ont été enregistrés dans {filename}.")


def retours_10000(n):
    res = []
    for i in range(1, n):
        with open(f"/Users/amo/TIPE/marche_1000/marche_10000_{i}", "r") as f:
            lignes = f.readlines()
        res.append(float(lignes[-1].split()[1]))
  
    x_coords = list(range(1, len(res) + 1)) 

    plt.figure(figsize=(12, 6))  

    plt.plot(x_coords, res, marker='o', markersize=5, linestyle='-', linewidth=2, color='b')

    plt.xlabel("Dimension", fontsize=12)
    plt.ylabel("Taux de retour après 10000 pas", fontsize=12)
    plt.title("Taux de retour après 10000 pas en fonction de la dimension", fontsize=14)

    plt.ylim(-0.1 * max(res), max(res) * 1.2)  # Ajoute plus de place en bas
    plt.xlim(0, len(res) + 1)  # L’axe X commence à 0

    plt.grid(True, linestyle='--', alpha=0.5)  # Quadrillage léger

    # Ajout de traits plus visibles pour les axes
    plt.gca().spines["left"].set_linewidth(1.5)   
    plt.gca().spines["bottom"].set_linewidth(1.5)  

    plt.tight_layout()  # Corrige le problème de texte coupé

    plt.savefig("/Users/amo/TIPE/marche_1000/marche_1000.png", bbox_inches='tight')
    plt.show()

retours_10000(30)


# Générer les 6 graphes correspondant aux 6 étapes de la marche
#for k in range(1, 7):
 #   marche_aleatoire_graphique(directions, k)

#tracer_graphique(fichiers, labels)

# Exemple d'utilisation
# proportion_retour_5D(n=1000, max_p=10000)

#plot_from_file("resultat_2D.txt","cases_parcourues_2D.png")

#position, plus_grand = max_ecart("resultat.txt")
#print(f"Le plus grand écart relatif est {plus_grand:.5f}")
#print(f"Il se produit pour n = {position[0]} :")
#print(f"Theoretical = {position[1]:.5f}, Experimental = {position[2]:.5f}")

#plot_from_file()
#print("le temps retour moyen en 1D est ", moyenne(retour_1(100)))
#print("le temps retour moyen en 2D est ", moyenne(retour_2(100)))


