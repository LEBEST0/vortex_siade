CREATE DATABASE IF NOT EXISTS SanteDB;
USE SanteDB;

-- Table Admin
CREATE TABLE Admin (
    id_admin INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table CentreSante
CREATE TABLE CentreSante (
    id_centre INT PRIMARY KEY AUTO_INCREMENT,
    nom_centre VARCHAR(150) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    logo_centre VARCHAR(255) NOT NULL
);

-- Table AgentSante
CREATE TABLE AgentSante (
    id_agent INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    specialite VARCHAR(100) NOT NULL,
    id_centre INT NOT NULL,
    id_admin INT NOT NULL,
    FOREIGN KEY (id_centre) REFERENCES CentreSante(id_centre) ON DELETE CASCADE,
    FOREIGN KEY (id_admin) REFERENCES Admin(id_admin) ON DELETE CASCADE
);

-- Table Patient
CREATE TABLE Patient (
    id_patient INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    sexe ENUM('H', 'F') NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    id_agent INT NOT NULL,
    image_frottis TEXT NOT NULL,
    date_envoi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_agent) REFERENCES AgentSante(id_agent) ON DELETE CASCADE
);

-- Table ResultatAnalyse
CREATE TABLE ResultatAnalyse (
    id_analyse INT PRIMARY KEY AUTO_INCREMENT,
    id_patient INT NOT NULL,
    resultat VARCHAR(255) NOT NULL,
    confiance DECIMAL(5,2) NOT NULL CHECK (confiance BETWEEN 0 AND 100),
    date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_patient) REFERENCES Patient(id_patient) ON DELETE CASCADE
);

-- Table RapportPDF
CREATE TABLE RapportPDF (
    id_rapport INT PRIMARY KEY AUTO_INCREMENT,
    id_analyse INT NOT NULL,
    fichier_rapport TEXT NOT NULL,
    date_generation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_analyse) REFERENCES ResultatAnalyse(id_analyse) ON DELETE CASCADE
);
