from flask import Flask, render_template, request
from models import create_member

# création de l'application Flask
app = Flask(__name__)

list_of_members = []

# 1. affichage du formulaire quand on va sur le site
@app.route('/')
def home():
    return render_template('formulaire.html')

# 2. Cette route reçoit les données du formulaire quand on clique sur le bouton
@app.route('/inscription', methods=['POST'])
def inscription():
    # récuperation du texte tapé dans les cases HTML
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    age = int(request.form.get('age'))
    taille = float(request.form.get('taille'))
    
    # utilisation du modèle dans models.py !
    membre = create_member(nom, prenom, age, taille)
    list_of_members.append(membre)
    
    # affichage de la page  succès HTML !
    return render_template('succes.html', nom=nom, prenom=prenom)

if __name__ == "__main__":
    # Lance le serveur web local
    app.run(debug=True)