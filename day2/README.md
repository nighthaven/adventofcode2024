Heureusement, le premier endroit que les historiens souhaitent rechercher n'est pas très loin du bureau de l'historien en chef.  
Alors que la centrale de fusion/fission nucléaire de Red-Nosed Reindeer ne semble contenir aucun signe de l'historien en chef,  
les ingénieurs se précipitent vers vous dès qu'ils vous voient.  
Apparemment, ils parlent encore de l'époque où Rudolph a été sauvé grâce à la synthèse moléculaire à partir d'un seul électron.

Ils s'empressent d'ajouter que - puisque vous êtes déjà là -  
ils apprécieraient vraiment votre aide pour analyser certaines données inhabituelles du réacteur Red-Nosed.  
Vous vous retournez pour vérifier si les historiens vous attendent,  
mais ils semblent déjà divisés en groupes qui fouillent actuellement tous les recoins de l'établissement.  
Vous proposez votre aide pour les données inhabituelles.

Les données inhabituelles (votre saisie de puzzle) se composent de nombreux rapports,  
un rapport par ligne. Chaque rapport est une liste de nombres appelés niveaux séparés par des espaces. Par exemple:

7 6 4 2 1  
1 2 7 8 9  
9 7 6 2 1  
1 3 2 4 5  
8 6 4 4 1  
1 3 6 7 9  

Cet exemple de données contient six rapports contenant chacun cinq niveaux.
Les ingénieurs tentent de déterminer quels rapports sont sûrs.  
Les systèmes de sûreté des réacteurs au Nez Rouge ne peuvent tolérer que des niveaux qui augmentent ou diminuent progressivement.  
Ainsi, un rapport n’est considéré comme sûr que si les deux conditions suivantes sont vraies :

Les niveaux sont soit tous croissants, soit tous décroissants.  
Deux niveaux adjacents diffèrent d'au moins un et d'au plus trois.  
Dans l'exemple ci-dessus, les rapports peuvent être jugés sûrs ou dangereux en vérifiant ces règles :  

7 6 4 2 1 : Sûr car les niveaux diminuent tous de 1 ou 2.  
1 2 7 8 9 : dangereux car 2 7 est une augmentation de 5.  
9 7 6 2 1 : dangereux car 6 2 est une diminution de 4.  
1 3 2 4 5 : dangereux car 1 3 augmente mais 3 2 diminue.  
8 6 4 4 1 : Dangereux car 4 4 n'est ni une augmentation ni une diminution.  
1 3 6 7 9 : Sûr car les niveaux augmentent tous de 1, 2 ou 3.  
Ainsi, dans cet exemple, 2 rapports sont sûrs.  

Analysez les données inhabituelles des ingénieurs. Combien de rapports sont sûrs ?
