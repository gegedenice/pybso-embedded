# Une simple page html générée avec le microframework Flask et basée sur le package [pybso](https://pypi.org/project/pybso/) pour visualiser son baromètre Science ouverte

Le fichier de données se trouve dans /static/data/ et a été produit en amont avec le [module core du package Python pybso](https://github.com/gegedenice/pybso) à partir d'une liste de DOI. Il comprend les métadonnées issues de l'API d'Unpaywall.

Cette mini app montre comment intégrer en frontend dans une page web des graphiques générés dans un backend Python avec la librairie graphique Plotly.

## Voir une démo en ligne

[https://ggeoffroy.com/apps/pybso-embedded](https://ggeoffroy.com/apps/pybso-embedded)

## Installation en local

La version de Python doit être python3

Cloner ou exporter ce dépôt, se placer à la racine du dossier puis :

1. Sans virtualenv

       pip install -r requirements.txt

       python app.py

2. Avec virtualenv

* Créer son environnement :

        virtualenv <votre_virtualenv>

  * Pour l'activer sous Windows : 

        cd <votre_virtualenv>/Scripts && activate

  * Pour l'activer sous Linux : 

        source <votre_virtualenv>/bin/activate && cd virtualenv_name/bin/

*      pip install -r requirements.txt

*      python app.py

L'application tourne sur le port 3000 et est accessible localement à l'adresse http://localhost:3000



