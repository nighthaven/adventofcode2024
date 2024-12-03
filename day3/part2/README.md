Lorsque vous parcourez la mémoire corrompue, vous remarquez que certaines instructions conditionnelles sont également  
toujours intactes. Si vous gérez certaines des instructions conditionnelles non corrompues du programme,  
vous pourrez peut-être obtenir un résultat encore plus précis.

Vous devrez gérer deux nouvelles instructions :

L'instruction do() active les futures instructions mul.
L'instruction don't() désactive les futures instructions mul.
Seule l'instruction do() ou don't() la plus récente s'applique. Au début du programme, les instructions mul sont activées.

Par exemple:

```
xmul(2,4)&mul[3,7]!^ne pas()_mul(5,5)+mul(32,64](mul(11,8)annuler()?mul(8,5))
```

Cette mémoire corrompue est similaire à l'exemple précédent, mais cette fois les instructions mul(5,5) et mul(11,8)  
sont désactivées car il y a une instruction don't() avant elles. Les autres instructions mul fonctionnent normalement,  
y compris celle de la fin qui est réactivée par une instruction do().

Cette fois, la somme des résultats est de 48 (2*4 + 8*5).

Gérer les nouvelles instructions ; qu'obtenez-vous si vous additionnez tous les résultats  
des multiplications activées uniquement ?