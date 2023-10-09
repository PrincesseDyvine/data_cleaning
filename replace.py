import pandas as pd

# Charger le fichier Excel
fichier_excel = 'C:/Users/princ/Desktop/data/merges.xlsx'
df = pd.read_excel(fichier_excel)

# Parcourir la colonne FILIERE et effectuer les remplacements
for i in range(len(df)):
    if df.at[i, 'lib_specialite_esp_et'] == 'Licence Business Computing':
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Business Computing'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence Fondamentale en Informatique de Gestion':
        df.at[i,'lib_specialite_esp_et'] = 'Licence Business Computing'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence en Business Computing':
        df.at[i,'lib_specialite_esp_et'] = 'Licence Business Computing'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence Business Computing - Parcours Bntelligence (BI)':
        df.at[i,'lib_specialite_esp_et'] = 'Licence Business Computing'
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence en Sciences de Gestion':
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Sciences de Gestion'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence en Sciences de Gestion- Parcours  Management':
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Sciences de Gestion'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence Fondamentale en Sciences de Gestion':
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Sciences de Gestion'
    elif df.at[i, 'lib_specialite_esp_et'] == 'Licence en Sciences de Gestion -Parcours Comptabilité':
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Sciences de Gestion'
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Licence Mathématiques Appliquées à l'Analyse des Données et l' Aide  à la Décision":
        df.at[i, 'lib_specialite_esp_et'] = 'Licence Mathématiques appliquées'
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == 'Master Professionnel en Management  Digital et S.I.':
        df.at[i, 'lib_specialite_esp_et'] = "Master Management Digital & Systemes d'Information"
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel Management Digital et Système d'Information":
        df.at[i, 'lib_specialite_esp_et'] = "Master Management Digital & Systemes d'Information"
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Management Digital et Système d'information":
        df.at[i, 'lib_specialite_esp_et'] = "Master Management Digital & Systemes d'Information"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Marketing Digital":
        df.at[i, 'lib_specialite_esp_et'] = "Master Marketing Digital"
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Marketing Digital":
        df.at[i, 'lib_specialite_esp_et'] = "Master Marketing Digital"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Business Analytics":
        df.at[i, 'lib_specialite_esp_et'] = "Master Business Analytics"
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Business Analytics ":
        df.at[i, 'lib_specialite_esp_et'] = "Master Business Analytics"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Comptabilité, Contrôle,  Audit":
        df.at[i, 'lib_specialite_esp_et'] = "Master Comptabilité Contrôle Audit"
    elif df.at[i, 'lib_specialite_esp_et'] == "Master en Comptabilité Contrôle Audit":
        df.at[i, 'lib_specialite_esp_et'] = "Master Comptabilité Contrôle Audit"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Gestion Actuarielle et Modélisation Mathématique":
        df.at[i, 'lib_specialite_esp_et'] = "Master Gestion Actuarielle & Modélisation Mathématique"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Professionnel en Finance Digitale":
        df.at[i, 'lib_specialite_esp_et'] = "Master Finance Digitale"
    ##
    elif df.at[i, 'lib_specialite_esp_et'] == "Master Alternance Vermeg :Management Digital et Système d'Information":
        df.at[i, 'lib_specialite_esp_et'] = "Master MDSI Alternance"

# Enregistrer le DataFrame modifié dans le même fichier Excel
df.to_excel(fichier_excel, index=False)
