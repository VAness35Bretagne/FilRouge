# Démineur
Projet en orienté objet pour coder le jeu démineur en python.

## Table des matières
- [Lancement](#Lancement)
- [Explication diagramme](#diagramme)
    - [Diagramme de classe](#diagramme_classe)


## Lancement du jeu
Pour lancer le jeu, il faut run la classe InterfaceJoueur. Une fois run, un message est demandé au joueur dans la console pour choisir le niveau du jeu : "débutant", "intermédiaire" ou "difficile". Une fois le niveau renseigné l'interface graphique se lance, et pour initialiser la grille, il suffit de cliquer au hasard sur une case et le jeu démarre.

Si une case contenant une bombe est cliquée, alors le message défaite apparaît. Si tous les drapeaux sont posés, alors le joueur a gagné et un message victoire apparaît.

## Explication diagramme
3 diagrammes différents sont fournis dans le dossier Diagramme: Diagramme de classe, diagramme d'activité et diagramme de cas d'utilisation


## Diagramme de classe 
Deux diagrammes de classe ont été réalisés au cours de ce projet. La différence majeur entre les deux diagrammes "Diagclass_beforeCode" et "Diagclass_afterCode" résulte dans l'association de la classe InterfaceJoueur/joueur au reste du jeu. En effet, avant de coder je pensais la relié à la classe Grille mais finalement la logique voulait qu'elle soit associé à la classe Case car elle requiert des éléments venant de cette classe. De plus, la classe Flag du diagramme 1 devient finalement un objet drapeau dans la classe InterfaceJoueur.

Pour résumer la logique du diagramme, il y a une relation d'héritage entre la grille et la case. Case est une spécialisation de grille, c'est à dire que si grille n'existe pas, case ne peut pas exister. Entre case et interface joueur, il y a une relation de composition. Cela indique que InterfaceJoueur contient des instances de Cases. Ainsi si InterfaceJoueur est détruit alors les instances de Case qu'il contient le sont également.


