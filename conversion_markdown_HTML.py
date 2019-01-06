# Programme de conversion de code markdown en HTML

import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Programme de conversion de code markdown en HTML"
)
parser.add_argument(
    "-i",
    "--input-directory",
    help="Dossier source contenant les fichiers markdowns qui seront convertis",
)
parser.add_argument(
    "-o",
    "--output-directory",
    help="Dossier destinataire qui va contenir les fichiers HTML qui seront générés",
)
args = parser.parse_args()

dossier_markdown = args.input_directory
dossier_html = args.output_directory

fichiers_markdown = Path(dossier_markdown).glob("**/*.markdown")
fichiers_html = {}


for fichier_markdown in fichiers_markdown:
    with open(fichier_markdown, "r", encoding="utf-8") as mon_fichier_markdown:
        old_ligne = ""
        contenu_html = ""
        for ligne in mon_fichier_markdown:
            # Titre
            if "#" in ligne:
                compteur_diese = ligne.count("#")
                ligne = ligne.replace("#", "<h{}>".format(compteur_diese), 1)
                ligne = ligne.replace("#", "")[:-1] + "</h{}>\n".format(compteur_diese)

            # URLs
            if "http" in ligne:
                index_debut_url = ligne.find("http")
                index_fin_url = ligne[index_debut_url:].find(" ")
                if index_fin_url != -1:
                    index_fin_url += index_debut_url
                adresse_url = ligne[index_debut_url:index_fin_url]
                expression_url = "<a href=" + adresse_url + ">" + adresse_url + "</a>"
                ligne = ligne[:index_debut_url] + expression_url + ligne[index_fin_url:]
                print(
                    "EXPRESSION URL :",
                    adresse_url,
                    "INDEX FIN URL :",
                    index_fin_url,
                    "LAST CARAC :",
                    ligne[index_fin_url],
                )

            if "*" in ligne:
                # Liste
                if ligne[0] == "*" and ligne.count("*") == 1:
                    if old_ligne == "" or "<li>" not in old_ligne:
                        contenu_html += "<ul>\n"
                    ligne = "<li>" + ligne[2:-1] + "</li>\n"
                # Mot important
                etat_balise = (
                    False
                )  # Booléen qui représentera l'état de la balise à mettre (False : ouvrante - True : fermante)
                while "*" in ligne:
                    index_balise = ligne.find("*")
                    if etat_balise:
                        balise = "</em>"
                        etat_balise = False
                    else:
                        balise = "<em>"
                        etat_balise = True
                    ligne = ligne[:index_balise] + balise + ligne[index_balise + 1 :]
            # Fermeture de liste
            if ligne.count("<li>") == 0 and old_ligne != "" and "<li>" in old_ligne:
                contenu_html += "</ul>\n"

            contenu_html += ligne
            old_ligne = ligne
    fichiers_html[fichier_markdown] = contenu_html

dossier_html = os.path.abspath(dossier_html)
os.chdir(dossier_html)
print("Dossier markdown :", str(dossier_html))
for nom_fichier, contenu_fichier in fichiers_html.items():
    nom_fichier = (
        str(nom_fichier)[str(nom_fichier).find("/") + 1 : str(nom_fichier).find(".")]
        + ".html"
    )

    with open(nom_fichier, "w", encoding="utf-8") as fichier_html:
        fichier_html.write(contenu_fichier)
        print("Génération du fichier", nom_fichier)