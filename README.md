# Markdown HTML converter
## Le projet
Ce programme est un exercice pour apprendre le langage python.
Il permet de convertir des fichiers écrits en markdown en html.
Il prend en compte 3 paramètres:
    > -h ou --help 
  * pour afficher l'aide pour expliquer les paramètres de la commande.
  
    > -i ou --input-directory 
  * commande à la suite de laquelle on entre le chemin du dossier source contenant les fichiers markdowns qui seront convertis.
  
    > -o ou --output-directory 
  * commande à la suite de laquelle on rentre le chemin du dossier destinatire qui va contenir les fichiers HTML qui seront générés.

## Conversion Markdown vers HTML

Ce programme prend en compte:
  * Les titres de niveau 1
    * exemple:
      > \#  en \<h1>
  * Les titres de niveau 2
     * exemple:
       > \##  en \<h2>
  * Les titres de niveau 2
     * exemple:
       > \###  en \<h3>
       
Convertir les listes non ordonnées en **\<ul>** et **\<li>**

Convertir les URL (http://quelquechose.com) en \<a href="http://quelquechose.com">http://quelquechose.com \</a>

Convertir \*un texte*, en un texte important \<em>un texte\</em>
