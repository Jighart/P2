# Projet 2: Books To Scrape

Ce script permet de récupérer les informations de tout les produits sur le site http://books.toscrape.com/.
Ces informations sont les suivantes:
 - URL du livre
 - Universal Product Code (upc)
 - Titre du livre
 - Prix, taxe incluse
 - Prix, taxe exclue
 - Quantité disponible
 - Description du produit
 - Catégorie
 - Rating
 - URL de l'image

Ces informations sont enregistrées dans le dossier data, avec un fichier .csv par catégorie.
Les images sont également téléchargées dans le dossier images.

# Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Jighart/P2-BookToScrape.git
```
Placez vous dans le dossier OC_P2_BooksToScrape, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```
