from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la base de données MySQL sous WampServer
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/malaria_vision_ai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db = SQLAlchemy(app)

# Importer les modèles après l'initialisation de db
from models import Admin, CentreSante, AgentSante, Patient, ResultatAnalyse, RapportPDF

# Point d'entrée
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Créer les tables si elles n'existent pas
    app.run(debug=True)
