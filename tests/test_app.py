import sys
import os

# On aide Python à trouver le dossier 'app' depuis le dossier 'tests'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from models import create_member

def test_creation_membre():
    # On simule la création
    resultat = create_member("DA COSTA", "Sébastien", 53, 1.80)
    
    # On vérifie que c'est bien un dictionnaire
    assert type(resultat) is dict
    # On vérifie que le nom est correct
    assert resultat["nom"] == "DA COSTA"
    
    print("✅ TEST REUSSI : Le moule 'models.py' fabrique des membres corrects.")

if __name__ == "__main__":
    test_creation_membre()