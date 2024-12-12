# Générateur de Texte à Trous

## Description

Le Générateur de Texte à Trous est une application de bureau développée en Python utilisant la bibliothèque Tkinter pour l'interface graphique et spaCy pour le traitement du langage naturel. Cette application permet de générer des textes à trous en supprimant certains types de mots spécifiés par l'utilisateur. Les textes générés peuvent ensuite être sauvegardés au format RTF.

## Fonctionnalités

- **Entrée de Texte** : L'utilisateur peut entrer un texte dans une zone de texte dédiée.
- **Sélection des Mots à Supprimer** : L'utilisateur peut spécifier le nombre de mots à supprimer et sélectionner les types de mots (noms, verbes, adjectifs, pronoms personnels, articles/déterminants, prépositions) à supprimer.
- **Génération de Texte à Trous** : L'application génère un texte à trous en remplaçant les mots sélectionnés par des underscores (`______`).
- **Sauvegarde en RTF** : Le texte à trous généré peut être sauvegardé au format RTF avec des options de police et de taille de caractères.

## Prérequis

Pour exécuter cette application, vous devez avoir Python installé sur votre machine. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/).

## Installation

1. Clonez ce dépôt sur votre machine locale :
    ```sh
    git clone https://github.com/votre-utilisateur/generateur-texte-a-trous.git
    ```
2. Accédez au répertoire du projet :
    ```sh
    cd generateur-texte-a-trous
    ```
3. Installez les dépendances nécessaires :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script principal :
    ```sh
    python main.py
    ```
2. Une fenêtre d'interface graphique s'ouvrira. Suivez les instructions à l'écran pour entrer votre texte, sélectionner les mots à supprimer, et générer le texte à trous.
3. Vous pouvez sauvegarder le texte à trous généré en cliquant sur le bouton "Sauvegarder en RTF" et en choisissant l'emplacement de sauvegarde.


## Contributions

Les contributions sont les bienvenues ! Pour contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/votre-fonctionnalite`).
3. Commitez vos modifications (`git commit -m 'Ajout de votre fonctionnalité'`).
4. Poussez vers la branche (`git push origin feature/votre-fonctionnalite`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Pour toute question ou suggestion, veuillez contacter [jdemageaux@gmail.com](mailto:jdemageaux@gmail.com).

---

N'hésitez pas à personnaliser ce README en fonction de vos besoins spécifiques et des informations supplémentaires que vous souhaitez inclure.
