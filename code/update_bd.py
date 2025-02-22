from app import app, db
from models import db, Admin, AgentSante, CentreSante, Patient, ResultatAnalyse, RapportPDF

# Créer un contexte d'application
with app.app_context():
    db.create_all()
    print("Tables mises à jour avec succès.")
