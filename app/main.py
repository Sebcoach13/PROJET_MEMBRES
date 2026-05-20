from flask import Flask, render_template, request, jsonify
from models import create_member

app = Flask(__name__)
list_of_members = []

# 1. Cette route affiche le formulaire quand on va sur le site
@app.route('/')
def home():
    return render_template('formulaire.html')

# 2. Cette route reçoit les données du formulaire quand on clique sur le bouton
@app.route('/inscription', methods=['POST'])
def inscription():
    # On récupère ce que l'utilisateur a tapé dans les cases HTML
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    age = int(request.form.get('age'))
    taille = float(request.form.get('taille'))
    
    # On utilise ton moule dans models.py !
    membre = create_member(nom, prenom, age, taille)
    list_of_members.append(membre)
    
    # On affiche la liste des membres en format JSON (texte propre) à l'écran
    return jsonify({"message": "Membre inscrit avec succès !", "liste_actuelle": list_of_members})

if __name__ == "__main__":
    # Lance le serveur web local
    app.run(debug=True)