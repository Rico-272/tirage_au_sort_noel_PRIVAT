from flask import Flask, request, Response
from flask_cors import CORS
import os
import requests
import base64

app = Flask(__name__)
CORS(app)

GITHUB_TOKEN = os.environ.get("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")
GITHUB_REPO = os.environ.get("Rico-272/tirage_au_sort_noel_PRIVAT")      
GITHUB_FILENAME = "sauvgardeTirageNoel.txt"                # Le nom du fichier dans le repo

userListe = ["marie-anne", "aurelie", "gregory", "jean-pierre", "marie", "pascal", "remi"]

API_URL = f"https://github.com{GITHUB_REPO}/contents/{GITHUB_FILENAME}"

def sauvegarder_sur_github(nouveau_texte):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 1. Récupérer le fichier actuel pour obtenir son contenu et son identifiant unique ("sha")
    reponse = requests.get(API_URL, headers=headers)
    
    if reponse.status_code == 200:
        donnees_fichier = reponse.json()
        sha = donnees_fichier["sha"]
        contenu_actuel = base64.b64decode(donnees_fichier["content"]).decode("utf-8")
    else:
        sha = None
        contenu_actuel = ""

    contenu_mis_a_jour = contenu_actuel + nouveau_texte + "\n"
    
    contenu_base64 = base64.b64encode(contenu_mis_a_jour.encode("utf-8")).decode("utf-8")

    payload = {
        "message": "Mise à jour automatique du serveur",
        "content": contenu_base64
    }
    if sha:
        payload["sha"] = sha  # Obligatoire pour modifier un fichier existant

    requests.put(API_URL, headers=headers, json=payload)

def lire_sur_github():
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    reponse = requests.get(API_URL, headers=headers)

    if reponse.status_code == 200:
        donnees_fichier = reponse.json()
        sha = donnees_fichier["sha"]
        contenu_actuel = base64.b64decode(donnees_fichier["content"]).decode("utf-8")
    else:
        sha = None
        contenu_actuel = ""

    return contenu_actuel


def VerificationLogin(nom, mot_de_passe):
    if nom in userListe : 
        numeroUtilisateur = userListe.index(nom)
        sauvgardePassword = lire_sur_github()
        
        
        
    else :
        return "error 4610"


def TirageAuSort():
    anne = ["2","3","5","6","7"]
    aurelie = ["1","3","4","5","7"]
    gregory = ["1","2","4","6","7"]
    jeanPierre = ["2","3","5","6","7"]
    marie = ["1","2","4","6","7"]
    pascal = ["1","3","4","5","7"]
    remi = ["1","2","3","4","5","6"]

    lire_sur_github()
    lignes = contenu_variable.splitlines()

    
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Flask va automatiquement chercher dans le dossier 'templates'
    return render_template('index.html') 

    
@app.route('/login', methods=['POST'])
def login():
    donnees = request.get_json()
    if not donnees:
        return Response("Erreur", status=400, mimetype='text/plain')

    nom_utilisateur = donnees.get('username')
    mot_de_passe = donnees.get('password')

#    resultat_texte = VerificationLogin(nom_utilisateur, mot_de_passe)
#    return Response(resultat_texte, mimetype='text/plain')

    test = lire_sur_github()
    return test



@app.route('/admin', methods=['POST'])
def admin():
    donnees = request.get_json()
    if not donnees:
        return Response("Erreur", status=400, mimetype='text/plain')


@app.route('/idee', methods=['POST'])
def idee():
    donnees = request.get_json()
    if not donnees:
        return Response("Erreur", status=400, mimetype='text/plain')
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
