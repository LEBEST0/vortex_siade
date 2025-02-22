import pymysql
pymysql.install_as_MySQLdb()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/malaria_vision_ai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Définition des modèles
class Admin(db.Model):
    id_admin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    date_creation = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Ajoute les autres modèles ici...
class CentreSante(db.Model):
    id_centre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_centre = db.Column(db.String(150), nullable=False)
    adresse = db.Column(db.String(255), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    logo_centre = db.Column(db.String(255), nullable=False)

# Modèle AgentSante
class AgentSante(db.Model):
    id_agent = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    specialite = db.Column(db.String(100), nullable=False)
    id_centre = db.Column(db.Integer, db.ForeignKey('centre_sante.id_centre', ondelete="CASCADE"), nullable=False)
    id_admin = db.Column(db.Integer, db.ForeignKey('admin.id_admin', ondelete="CASCADE"), nullable=False)

    #Relation avec patient
    patients = db.relationship('Patient', backref='agent', lazy=True)

# Modèle Patient
class Patient(db.Model):
    id_patient = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    sexe = db.Column(db.Enum('H', 'F'), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    id_agent = db.Column(db.Integer, db.ForeignKey('agent_sante.id_agent', ondelete="CASCADE"), nullable=False)
    image_frottis = db.Column(db.Text, nullable=False)
    date_envoi = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    # Relation avec ResultatAnalyse
    analyses = db.relationship('ResultatAnalyse', backref='patient', lazy=True)

# Modèle ResultatAnalyse
class ResultatAnalyse(db.Model):
    id_analyse = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_patient = db.Column(db.Integer, db.ForeignKey('patient.id_patient', ondelete="CASCADE"), nullable=False)
    resultat = db.Column(db.String(255), nullable=False)
    confiance = db.Column(db.Numeric(5,2), nullable=False)
    date_analyse = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Modèle RapportPDF
class RapportPDF(db.Model):
    id_rapport = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_analyse = db.Column(db.Integer, db.ForeignKey('resultat_analyse.id_analyse', ondelete="CASCADE"), nullable=False)
    fichier_rapport = db.Column(db.Text, nullable=False)
    date_generation = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())


# Création de la base de données
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Base de données créée avec succès !")


