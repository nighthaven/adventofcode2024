Les ingénieurs sont surpris par le faible nombre de rapports de sécurité jusqu'à ce qu'ils se rendent compte qu'ils ont  
oublié de vous parler du problème de l'amortisseur.

Le Problem Dampener est un module monté sur le réacteur qui permet aux systèmes de sécurité du réacteur de tolérer  
un seul niveau défectueux dans ce qui serait autrement un rapport sûr.  
C'est comme si le mauvais niveau n'était jamais arrivé !

Désormais, les mêmes règles s'appliquent qu'auparavant, sauf si la suppression d'un seul niveau d'un rapport  
non sécurisé rend celui-ci sûr, le rapport est alors considéré comme sûr.

Un plus grand nombre de rapports de l'exemple ci-dessus sont désormais sécurisés :

7 6 4 2 1 : Coffre-fort sans supprimer aucun niveau.  
1 2 7 8 9 : dangereux quel que soit le niveau supprimé.  
9 7 6 2 1 : dangereux quel que soit le niveau supprimé.  
1 3 2 4 5 : Sécurisé en supprimant le deuxième niveau, 3.  
8 6 4 4 1 : Coffre-fort en supprimant le troisième niveau, 4.  
1 3 6 7 9 : Coffre-fort sans supprimer aucun niveau.  
Grâce au Problem Dampener, 4 rapports sont réellement sûrs !  

Mettez à jour votre analyse en gérant les situations dans lesquelles le Problem Dampener peut supprimer  
un seul niveau des rapports dangereux. Combien de rapports sont désormais sécurisés ?