import re

# Ton pattern pour les lettres
regex_pattern = r"^[a-zA-Zà-ÿÀ-ß\s\-]+$"

def get_valid_name(prompt):
    """
    Demande un nom à l'utilisateur et recommence tant que ce n'est pas valide.
    """
    while True:
        saisie = input(prompt).strip()
        if re.fullmatch(regex_pattern, saisie) and len(saisie) > 0:
            return saisie.capitalize()
        
        print("❌ Erreur : Le nom ne doit contenir que des lettres.")

def get_valid_number(prompt, type_func):
    """
    Demande un nombre (int ou float) et gère les erreurs de saisie.
    """
    while True:
        saisie = input(prompt).strip()
        try:
            # On tente la conversion (int ou float)
            valeur = type_func(saisie)
            if valeur > 0:
                return valeur
            print("❌ Erreur : Le nombre doit être supérieur à 0.")
        except ValueError:
            # Si l'utilisateur tape des lettres au lieu d'un nombre
            print(f"❌ Erreur : Veuillez entrer un nombre valide (type: {type_func.__name__}).")