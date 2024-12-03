Votre analyse n’a fait que confirmer ce que tout le monde craignait :  
les deux listes d’identifiants de localisation sont en effet très différentes.

Ou le sont-ils ?
Les historiens ne parviennent pas à se mettre d'accord sur le groupe qui a commis les erreurs  
ni sur la manière de lire la plupart des écritures du chef, mais dans le tumulte,  
vous remarquez un détail intéressant : de nombreux identifiants de lieux apparaissent dans les deux listes !  
Peut-être que les autres chiffres ne sont pas du tout des identifiants de localisation,  
mais plutôt une écriture manuscrite mal interprétée.

Cette fois, vous devrez déterminer exactement à quelle fréquence chaque numéro de la liste  
de gauche apparaît dans la liste de droite. Calculez un score total de similarité en additionnant  
chaque nombre dans la liste de gauche après l'avoir multiplié par le nombre de fois que ce nombre  
apparaît dans la liste de droite.

Voici à nouveau les mêmes exemples de listes :

| 3 | 4 |  
| 4 | 3 |  
| 2 | 5 |  
| 1 | 3 |  
| 3 | 9 |  
| 3 | 3 |  

Pour ces exemples de listes, voici le processus de recherche du score de similarité :

Le premier chiffre de la liste de gauche est 3. Il apparaît trois fois dans la liste de droite,  
donc le score de similarité augmente de 3 * 3 = 9.  
Le deuxième nombre dans la liste de gauche est 4. Il apparaît une fois dans la liste de droite,  
donc le score de similarité augmente de 4 * 1 = 4.  
Le troisième nombre dans la liste de gauche est 2. Il n'apparaît pas dans la liste de droite,  
donc le score de similarité n'augmente pas (2 * 0 = 0).  
Le quatrième chiffre, 1, n'apparaît pas non plus dans la liste de droite.  
Le cinquième chiffre, 3, apparaît trois fois dans la liste de droite ;  
le score de similarité augmente de 9.  
Le dernier chiffre, 3, apparaît trois fois dans la liste de droite ;  
le score de similarité augmente à nouveau de 9.  
Ainsi, pour ces exemples de listes, le score de similarité à la fin de ce processus est de 31 (9 + 4 + 0 + 0 + 9 + 9).

Considérez encore une fois vos listes de gauche et de droite. Quel est leur score de similarité ?