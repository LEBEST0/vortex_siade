from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import db, Admin

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la base de données MySQL sous WampServer
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/malaria_vision_ai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Clé pour gérer les sessions

# Initialisation de SQLAlchemy (sans passer `app`)
# db = SQLAlchemy()

# Association de `db` avec `app`
db.init_app(app)

# Importation des modèles après l'initialisation
from models import Admin, CentreSante, AgentSante, Patient, ResultatAnalyse, RapportPDF

#agent sante
@app.route('/')
def acceuil():
    return render_template('index.html')  
@app.route('/dashboardAgent')
def dashboardAgent():
    return render_template('dashboard.html')  
@app.route('/connexion')
def connexion():
    return render_template('connexion.html')


#admin
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        admin = Admin.query.filter_by(email=email).first()

        if admin and admin.mot_de_passe == password:  # Vérification mot de passe sans hashage
            session['admin_id'] = admin.id_admin  # Stocke l'admin en session
            return redirect(url_for('dashboard'))

        return render_template('login.html', error="Email ou mot de passe incorrect")

    return render_template('login-admin.html')

@app.route('/dashboard')
def dashboard():
    if 'admin_id' in session:  # Vérifie si l'admin est connecté
        return render_template('dashboard-admin.html')  
    return redirect(url_for('login'))  # Redirige vers login s'il n'est pas connecté

@app.route('/logout')
def logout():
    session.pop('admin_id', None)  # Déconnecte l'admin
    return redirect(url_for('login'))

# Point d'entrée
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Créer les tables si elles n'existent pas
    app.run(debug=True)
