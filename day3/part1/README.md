"Nos ordinateurs ont des problèmes, donc je ne sais pas si nous avons des historiens en chef en stock !  
Vous pouvez cependant vérifier l'entrepôt", déclare le commerçant légèrement troublé du magasin de location de luges du Pôle Nord.  
Les historiens partent jeter un œil.

Le commerçant se tourne vers vous. « Y a-t-il une chance que vous puissiez comprendre pourquoi nos ordinateurs  
rencontrent à nouveau des problèmes ? »

L'ordinateur semble essayer d'exécuter un programme, mais sa mémoire (votre saisie de puzzle) est corrompue.  
Toutes les instructions ont été mélangées !
Il semble que le but du programme soit simplement de multiplier certains nombres.  
Il le fait avec des instructions telles que mul(X,Y), où X et Y sont chacun des nombres de 1 à 3 chiffres.  
Par exemple, mul(44,46) multiplie 44 par 46 pour obtenir un résultat de 2024.  
De même, mul(123,4) multiplierait 123 par 4.

Cependant, comme la mémoire du programme a été corrompue, il existe également de nombreux caractères invalides  
qui doivent être ignorés, même s'ils semblent faire partie d'une instruction mul.  
Des séquences comme mul(4*, mul(6,9!, ?(12,34) ou mul ( 2 , 4 ) ne font rien.

Par exemple, considérons la section suivante de mémoire corrompue :

```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```

Seules xmul(2,4), mul(5,5), mul(11,8), mul(8,5)  sont a prendre
L'addition du résultat de chaque instruction produit 161 (2*4 + 5*5 + 11*8 + 8*5).

Analysez la mémoire corrompue à la recherche d'instructions mul non corrompues.  
Qu'obtient-on si l'on additionne tous les résultats des multiplications ?