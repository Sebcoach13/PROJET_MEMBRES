from models import create_member
from validators import get_valid_name 

list_of_members = []

if __name__ == "__main__":
    print("--- Inscription des membres ---")
    
    #  fonction get_valid_name pour demander le nom et le prénom
    nom = get_valid_name("Entrez le nom : ")
    prenom = get_valid_name("Entrez le prénom : ")
    
    
    membre = create_member(nom, prenom, 30, 1.80)
    
    list_of_members.append(membre)
    
    print("\nListe des membres enregistrés :")
    print(list_of_members)
