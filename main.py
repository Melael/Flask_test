from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def accueil():
    return 'Page Accueil'

@app.route('/recette')
def recette():
    return 'Page des recettes'

@app.route('/ingrédients')
def ingrédient():
    return 'Page des ingrédients pour les courses'