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

### 🌞 Proposer un jeu de règles firewall

## III. ARP Spoofing Ecoute active
### 🌞 Write-up de l'épreuve


## IV. Bonus : Trafic Global System for Mobile communications

### ⭐ BONUS : Write-up de l'épreuve
