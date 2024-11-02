# TP6 : Un peu de root-me
## I. DNS Rebinding
### 🌞 Write-up de l'épreuve
- Le devops de cette petite application web a peu de temps et peu de moyens. L’interface d’administration est ainsi, comme souvent, embarquée avec l’IHM utilisateur. Pour autant il s’est assuré qu’on ne puisse pas y accéder de l’extérieur !

### 🌞 Proposer une version du code qui n'est pas vulnérable
## II. Netfilter erreurs courantes
### 🌞 Write-up de l'épreuve

- Netfilter - erreurs courantes
Un administrateur plein de bonne volonté a essayé de renforcer la sécurité de son serveur en ajustant les règles du pare-feu. Vérifiez qu’il a bien fait son travail !

### 🌞 Proposer un jeu de règles firewall

## III. ARP Spoofing Ecoute active
### 🌞 Write-up de l'épreuve
- ARP Spoofing - Écoute active 
Votre ami vous assure que vous ne pouvez pas récupérer les informations confidentielles qui transitent sur son réseau. Il est tellement sûr de lui qu’il vous donne un accès à son LAN via une machine que vous contrôlez.

Le flag est la concaténation de la réponse à une requête sur le réseau, ainsi que le mot de passe de la base de données, de la forme suivante : reponse:db_password.
    Démarrez le CTF-ATD "ARP Spoofing EcouteActive"
    Connectez-vous en SSH sur la machine port 22222 (root:root)
    Il n’y a pas de validation de l’environnement virtuel avec un /passwd

N’hésitez pas à changer le mot de passe de l’utilisateur root afin d’être seul sur la machine pour réaliser vos manipulations.
