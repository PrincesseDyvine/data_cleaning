import pandas as pd

# Charger le fichier Excel
fichier_excel = 'C:/Users/princ/Desktop/data/merges.xlsx'
df = pd.read_excel(fichier_excel)


# Parcourir la colonne BAC et effectuer les remplacements
for i in range(len(df)):
    if df.at[i, 'lib_nature_bac'] == 'Bac Economie-gestion':
        df.at[i, 'lib_nature_bac'] = 'Bac Economie'
    elif df.at[i, 'lib_nature_bac'] == 'Scientifique':
        df.at[i, 'lib_nature_bac'] = 'Bac Math'
    elif df.at[i, 'lib_nature_bac'] == 'Maths Technique':
        df.at[i, 'lib_nature_bac'] = 'Bac Technique'
    elif df.at[i, 'lib_nature_bac'] == 'SERIE D Sciences Naturelles':
        df.at[i, 'lib_nature_bac'] = 'Bac Sciences expérimentales'
    elif df.at[i, 'lib_nature_bac'] == 'MATH GENIE CEVIL':
        df.at[i, 'lib_nature_bac'] = 'Bac Math'
    elif df.at[i, 'lib_nature_bac'] == "Série D (Côte d'Ivoire)":
        df.at[i, 'lib_nature_bac'] = 'Bac Sciences expérimentales'
    elif df.at[i, 'lib_nature_bac'] == "Série D Cameroun":
        df.at[i, 'lib_nature_bac'] = 'Bac Sciences expérimentales'
    elif df.at[i, 'lib_nature_bac'] == "Série D (NIGER)":
        df.at[i, 'lib_nature_bac'] = 'Bac Sciences expérimentales'
    elif df.at[i, 'lib_nature_bac'] == "Bac téchnique":
        df.at[i, 'lib_nature_bac'] = 'Bac Technique'

# Enregistrer le DataFrame modifié dans le même fichier Excel
df.to_excel(fichier_excel, index=False)
