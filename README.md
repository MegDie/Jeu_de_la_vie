### Le jeu de la vie 

Le jeu de la vie est un automate cellulaire mis au point par le mathématicien britannique John Horton Conway en 1970. Il s'agit d'un jeu à **zéro** joueur, autrement dit, son évolution est entièrement déterminée par son état initial.

L'univers du jeu est dans notre cas une grille carrée de taille finie. De plus, le pourtour de la grille est toujours inactif/mort. Leq cellules du jeu ne peuvent prendre qu'un état parmi l'un des deux états possibles: **vivant** (1) ou **mort** (0).

Chaque cellule interagit avec ses huit cellules voisines et à chaque étape, les transitions suivantes se produisent:

  + Toute cellule morte ayant exactement 3 voisins vivants devient une cellule vivante (*naissance*)
  + Toute cellule vivante avec 2 ou 3 voisins vivants reste vivante à la génération suivante (*équilibre*)
  + Toute cellule vivante ayant 4 voisins vivants ou plus meurt à la génération suivante (*mort par étouffement*)
  + Toute cellule vivante ayant 0 ou 1 voisin vivant décède à la génaration suivante (*mort par isolement*à



