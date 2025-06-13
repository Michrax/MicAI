# Pour publier le site, me renseigner sur les possibilités : Render.com (le + recommandé), Railway.app, Fly.io, PythonAnywhere (bon pour débuter), etc...
# L'idée est de push le code sur un dépôt GitHub et de le déployer automatiquement sur l'hébergeur choisi.
# Pour le déploiement, il faudra aussi un fichier requirements.txt pour les dépendances.
# Quand je vais vouloir rendre le site marchand, je pense utiliser Stripe pour les paiements.
# Il ne faudra pas oublier tout le côté de sécurité et RGPD, cookies, etc...
# Dans un premier temps, je me concentre sur la partie vitrine du site sans venir chercher de données ou autre, juste l'aspect visuel.
# Mon site / entreprise s'appelle "MicAI", je vais utiliser ce site pour présenter mes services dans l'IA (freelance), mes compétences et mes projets.
# En bref, qui je suis et ce que je fais, ce sera mon portfolio.
# Pour le développement, j'utilise Flask comme framework web en Python.
# Pour le design, je vais utiliser Bootstrap pour la mise en forme et rendre le site responsive.

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'micai-secret-key'  # requis pour flash() si besoin

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Page à propos
@app.route('/about')
def about():
    return render_template('about.html')

# Page services
@app.route('/services')
def services():
    return render_template('services.html')

# Page portfolio
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Page contact avec formulaire
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"[CONTACT] De: {name} <{email}> - Message: {message}")
        flash("Message bien envoyé. Merci pour votre contact !", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}


if __name__ == '__main__':
    app.run(debug=True)
