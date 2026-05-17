import re

# On garde ton pattern (il est très bien !)
regex_pattern = r"^[a-zA-Zà-ÿÀ-ß\s\-]+$"

def get_valid_name(prompt):
    """
    Demande un nom à l'utilisateur et recommence tant que ce n'est pas valide.
    """
    while True:
        saisie = input(prompt).strip()
        # On teste la saisie avec ta logique
        if re.fullmatch(regex_pattern, saisie) and len(saisie) > 0:
            return saisie.capitalize() # On renvoie le nom propre
        
        print("❌ Erreur : Le nom ne doit contenir que des lettres et ne pas être vide.")
    