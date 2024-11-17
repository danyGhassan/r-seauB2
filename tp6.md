# TP6 : Un peu de root-me
## I. DNS Rebinding
### 🌞 Write-up de l'épreuve
- ### DNS Rebinding 
Lorsque on se renseinge sur DNS rebinding sur google : Le DNS rebinding est une technique couramment utilisée par les cyberattaquants. Elle consiste à manipuler la résolution de nom de domaine de façon à ce que le visiteur d’une page web malveillante exécute un script côté client qui attaque d’autres machines sur le réseau.

Le but de l'épreuve est de contourner l'utilisation principal du site du challenge  qui est de reproduire de façon simple le site qu'on lui donne en argument.

Notre objectif sera donc de contourner l'utilisation principal du programme est d'accéder a la page admin avec le DNS Rebinding.

Lorsque nous cherchons "DNS Rebinding tool" sur goole nous trouvons cette page : [DNS Rebinding tool ](https://lock.cmpxchg8b.com/rebinder.html)

Lorsqu'on lit le code source donné par l'epreuve , nous découvrons que pour accéder a la page admin, nous avons besoin d'avoir cette ip : 127.0.0.1 .
Nous obtenons donc 7f000001.c0a80001.rbndr.us . Mais pour accéder a la page admin il faut préciser le chemin en plus de "l'url": 7f000001.c0a80001.rbndr.us:54022/admin

en spammant cette url on obtiens le flag .


### 🌞 Proposer une version du code qui n'est pas vulnérable
## II. Netfilter erreurs courantes
### 🌞 Write-up de l'épreuve
Le but de cette épreuve est d'acceder a la page admin qui est : http://challenge01.root-me.org:54017
Pour se faire nous devons regarder plus en profondeur sur les régles données des iptables et ce sont ses deux lignes qui vont nous intéresser : 
```
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j DROP
# Previous rules ensure we're dealing with legitimate requests -> ACCEPT them now
IP46T -A INPUT-HTTP -j ACCEPT
```
Pour pouvoir accéder a la page , nous devons valider la première condition et une fois qu'on la valider notre trafic sera accepté par le firewall.
```
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j DROP
```
Ce que veut dire cette ligne est que les 20 premiers paquets seront DROP.
Nous devons donc créer un programme qui vous nous premettre d'envoyer 20 requettes a l'addresse et donc la 21eme sera accepté.

```
For i in {1..20}; do netcat challenge01.root-me.org 54017 & do | http://challenge01.root-me.org:54017/reseau/ch17
```
se script va donc envoyer 20 requettes au firewall et le 21 nous allons lire la page avec curl. Le flag sera donnée grâce au curl.

### 🌞 Proposer un jeu de règles firewall
```
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j DROP
# Previous rules ensure we're dealing with legitimate requests -> ACCEPT them now
IP46T -A INPUT-HTTP -j ACCEPT
```
Au lieu d'accepter le paquet nous pouvons tous simplement le DROP, donc :
```
IP46T -A INPUT-HTTP -j DROP
```

## III. ARP Spoofing Ecoute active
### 🌞 Write-up de l'épreuve
cette epreuve je l'ai faite avec matis donc voici son repo : [arp spoofing](https://github.com/MatisCelestin/TP-RESEAU-B2/blob/main/TP-6/TP-6.MD#iii-arp-spoofing-ecoute-active)

### 🌞 Proposer une configuration pour empêcher votre attaque
Pour empêcher de retrouver le mot de passe nous pouvons tout simplement utiliser la dernière version de MYSQL

## IV. Bonus : Trafic Global System for Mobile communications

### ⭐ BONUS : Write-up de l'épreuve

Voici l'énnoncé de cette epreuve : Vous êtes mandaté pour analyser une capture réseau. Vous devez remettre quelque chose de compréhensible à votre interlocuteur, même si à première vue la trace parait incomplète.

Le les acronymes de cette épreuve est GSM et si on fait quelque recherche , GSM c'est un tout simplement la 2G.

Lorqu'on tape sur GSM decoder on va tomber sur ce site : [gsm decoder](https://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/online-sms-pdu-decoder/) .

Lorsqu'on analyse la capture donnée, on se rends compte qu'il y'a une trame avec plus de données que les autres, on donc recupérer la data sous forme d'hexa de cette trame
```
00ff9c0402030201ffff0b5a0791233010210068040b917120336603f800002140206165028047c7f79b0c52bfc52c101d5d0699d9e133283d0785e764f87b6da7956bb7f82d2c8b
```
 et on va ensuite la mettre sur le site. Le site va nous mettre une erreur, mais lorsqu'on regarde la syntaxe demandé par le site , leurs hexa commence par 07 , on va donc supprimé tout les caractères de notre capture jusqu'au caractère 07 se qui va donner : 

```
0791233010210068040b917120336603f800002140206165028047c7f79b0c52bfc52c101d5d0699d9e133283d0785e764f87b6da7956bb7f82d2c8b
```
On mettant cela sur le site nous allons obtenir le flag.
