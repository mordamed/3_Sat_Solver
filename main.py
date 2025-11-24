from las_vegas_max_3sat import las_vegas_max_3sat
from Reading import parse_dimacs_line, load_dimacs_file
import time 

filepath = "uf20-0284.cnf" 

if __name__ == "__main__":
    # # Exemple simple : 4 variables, 5 clauses
    # # Format interne : liste de listes d'entiers
    # clauses_exemple = [
    #     [1, 2, 1, -3],    # x1 ou x2 ou non-x3
    #     [-1, -2, 3],
    #     [2, -3, 4],
    #     [-2, 3, -4],
    #     [1, 3, 4]
    # ]
    # nb_variables = 4

    # print("Recherche d'une solution satisfaisant >= 7/8 des clauses...")
    # solution, score, nb_essais = las_vegas_max_3sat(nb_variables, clauses_exemple)

    # print(f"Succès en {nb_essais} essai(s) !")
    # print(f"Clauses satisfaites : {score}/{len(clauses_exemple)}")
    # print(f"Assignation finale : {solution[1:]}") # On ignore l'index 0


    fichier_test = filepath

    try:
        # Chargement
        print(f"Lecture du fichier : {fichier_test}...")
        n, clauses = load_dimacs_file(fichier_test)
        print(f"Variables: {n}, Clauses: {len(clauses)}")
        
        # Chronométrage
        start_time = time.time()
        
        # Résolution
        sol, score, essais = las_vegas_max_3sat(n, clauses)
        
        end_time = time.time()
        duree = end_time - start_time
        
        # Résultats
        ratio = score / len(clauses)
        print("-" * 30)
        print(f"Résultat trouvé en {duree:.6f} secondes")
        print(f"Nombre d'essais (itérations) : {essais}")
        print(f"Clauses satisfaites : {score}/{len(clauses)} ({ratio:.2%})")
        print(f"Le ratio est-il >= 7/8 (87.5%) ? {'OUI' if ratio >= 0.875 else 'NON'}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_test}' est introuvable. Télécharge un fichier .cnf d'abord.")
# %%
