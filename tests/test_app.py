import sys
import os

# Trouver le dossier 'app' depuis le dossier 'tests'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from models import create_member

def test_creation_membre():
    # simuler la création
    resultat = create_member("DA COSTA", "Sébastien", 53, 1.80)
    
    # vérification dictionnaire
    assert type(resultat) is dict
    # vérification du nom
    assert resultat["nom"] == "DA COSTA"
    
    print("✅ TEST REUSSI : Le moule 'models.py' fabrique des membres corrects.")

if __name__ == "__main__":
    test_creation_membre()