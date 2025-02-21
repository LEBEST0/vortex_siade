from app import db, app
from models import Admin, CentreSante, AgentSante, Patient, ResultatAnalyse, RapportPDF
from datetime import date
import random

# Fonction pour insérer des données
def seed_database():
    with app.app_context():
        db.session.begin()

        # Ajouter un administrateur
        admin = Admin(nom="Super Admin", email="admin@example.com", mot_de_passe="admin123")
        db.session.add(admin)
        db.session.commit()

        # Ajouter un centre de santé
        centre = CentreSante(nom_centre="Centre de Santé Espoir",
                             adresse="123 Rue de la Santé",
                             ville="Abidjan",
                             email="centre@example.com",
                             telephone="0102030405",
                             logo_centre="logo.png")
        db.session.add(centre)
        db.session.commit()

        # Ajouter un agent de santé
        agent = AgentSante(nom="Doe", prenom="John",
                           email="john.doe@example.com",
                           mot_de_passe="password123",
                           specialite="Généraliste",
                           id_centre=centre.id_centre,
                           id_admin=admin.id_admin)
        db.session.add(agent)
        db.session.commit()

        # Ajouter un patient
        patient = Patient(nom="Koné", prenom="Fatou",
                          date_naissance=date(1995, 6, 12),
                          sexe="F",
                          telephone="0708091011",
                          id_agent=agent.id_agent,
                          image_frottis="image_frottis.png")
        db.session.add(patient)
        db.session.commit()

        # Ajouter un résultat d'analyse
        resultat = ResultatAnalyse(id_patient=patient.id_patient,
                                   resultat="Positif",
                                   confiance=random.uniform(85, 99))
        db.session.add(resultat)
        db.session.commit()

        # Ajouter un rapport PDF
        rapport = RapportPDF(id_analyse=resultat.id_analyse,
                             fichier_rapport="rapport_fatou.pdf")
        db.session.add(rapport)
        db.session.commit()

        db.session.commit()
        print("Données insérées avec succès !")

if __name__ == "__main__":
    seed_database()
