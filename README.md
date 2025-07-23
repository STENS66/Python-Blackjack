# Python-Blackjack - Version française 1.0

**Copyright © Gaëtan Sencie 2024**

**Tous droits réservés.**




## Description du jeu


**Python-Blackjack** est une implémentation complète du célèbre jeu de casino, le Blackjack, développée en Python avec la bibliothèque Pygame. Ce jeu offre une expérience solo immersive où le joueur affronte un croupier géré par l'ordinateur, en misant de l'argent fictif pour tenter d'atteindre 21 sans le dépasser.

Conçu pour être intuitif et facile à prendre en main, même pour les novices, il intègre toutes les règles classiques du Blackjack, y compris les options de "**Tirer**", "**Rester**", "**Doubler**" et "**Split**". Le jeu gère également les blackjacks naturels, les égalités et les situations de bust.

Une fonctionnalité unique est le **Hall of Fame**, permettant aux joueurs de sauvegarder leurs meilleurs scores et de les comparer avec d'autres.



## Fonctionnalités principales


* Jeu solo contre le Croupier : Affrontez une IA de croupier réaliste.
* Système de mise flexible : Misez le montant de votre choix avec un solde de départ de 1000€.
* Options de jeu complètes : "**Tirer**", "**Rester**", "**Doubler**" et "**Split**" (pour les paires).
* Gestion des Blackjacks naturels : Reconnaissance et traitement des mains initiales de 21.
* Hall of Fame persistant : Enregistrez et consultez les 5 meilleurs scores, sauvegardés localement.
* Interface utilisateur conviviale : Graphismes clairs et navigation simple grâce à Pygame.
* Gestion de solde : Option d'acheter de nouveaux jetons si le solde est épuisé.


## Prévisualisation

![Capture d'écran du jeu Python-Blackjack](https://github.com/STENS66/Python-Blackjack/blob/main/images/gameplay.png?raw=true)


### Compatibilité


Application de bureau conçue pour Windows 10 et 11 (64 bits).



## Règles du jeu


Le but est d'obtenir une main dont la valeur totale est la plus proche possible de 21 sans la dépasser.

Les cartes numérotées (2 à 10) ont leur valeur nominale.

Les figures (Valet, Dame, Roi) valent 10.

Les As peuvent valoir 1 ou 11, selon ce qui est le plus avantageux pour la main.

Le joueur commence avec un solde de 1000 euros et peut miser une partie de ce solde au début de chaque manche. Après avoir reçu deux cartes, le joueur peut choisir de :

**Tirer** : Recevoir une carte supplémentaire.

**Rester** : Conserver sa main actuelle.

**Doubler** : Doubler la mise et recevoir une dernière carte.

**Split** : Si les deux premières cartes ont la même valeur, diviser la main en deux mains distinctes (nécessite une mise supplémentaire égale à la mise initiale).

Le croupier tire des cartes jusqu'à ce que sa main atteigne au moins 17.

Si le joueur dépasse 21 (bust), il perd immédiatement sa mise.

Si le croupier dépasse 21, le joueur gagne la manche.

Sinon, celui dont la main est la plus proche de 21 l'emporte.

Lorsque le solde du joueur est épuisé, une fenêtre s'ouvre pour proposer de quitter ou d'acheter de nouveaux jetons (1000€) pour continuer. Si le joueur quitte le jeu avec un solde positif, il sera invité à enregistrer son score dans le "**Hall of Fame**" s'il fait partie des cinq meilleurs joueurs.



## Technologies utilisées


* Python 3.13 : Langage de programmation principal.
* Pygame 2.6 : Bibliothèque pour le développement de jeux vidéo 2D en Python, utilisée pour les graphiques, le son et la gestion des événements.
* JSON : Utilisé pour la persistance des données du "Hall of Fame".



## Public cible


Ce jeu est destiné aux amateurs de jeux de casino, en particulier ceux qui apprécient les jeux de cartes comme le blackjack. Il est également adapté aux joueurs novices grâce à son gameplay simple et ses règles accessibles.



## Installation


Exécutable (Windows 10/11 - 64 bits)
Téléchargez la dernière version de l'exécutable Python-Blackjack.exe depuis la section Releases de ce dépôt.
Faites un double-clic sur le fichier téléchargé pour lancer le jeu.



## Contact


Pour toute question, assistance supplémentaire ou retour sur le jeu, vous pouvez contacter l'auteur à l'adresse suivante : app.sencie@gmail.com



## Licence


Ce programme est sous licence. Tous droits réservés.

---

Merci de jouer à Python Blackjack ! j'espère que vous apprécierez ce jeu autant que j'ai pris plaisir à le développer.
