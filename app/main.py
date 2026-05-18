from models import create_member
from validators import get_valid_name, get_valid_number 

list_of_members = []

if __name__ == "__main__":
    print("--- Inscription des membres ---")
    
    # 1. On récupère les infos (les fonctions sont dans validators.py)
    nom = get_valid_name("Entrez le nom : ")
    prenom = get_valid_name("Entrez le prénom : ")
    age = get_valid_number("Entrez l'âge : ", int)
    taille = get_valid_number("Entrez la taille (ex: 1.75) : ", float)
    
    # 2. On crée le membre avec les VRAIES variables qu'on vient de saisir
    # (On ne laisse pas 30 et 1.80 écrits en dur !)
    membre = create_member(nom, prenom, age, taille)
    
    # 3. On ajoute à la liste
    list_of_members.append(membre)
    
    print("\n✅ Liste des membres enregistrés :")
    print(list_of_members)