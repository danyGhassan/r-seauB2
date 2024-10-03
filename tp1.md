# TP1 : Maîtrise réseau du votre poste

## I. Basics

### ☀️ Carte réseau WiFi
- l'adresse MAC de votre carte WiFi
```
PS C:\Users\ghass> ipconfig /all

Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 48-E7-DA-A7-C7-5F
```
- l'adresse IP de votre carte WiFi
```
PS C:\Users\ghass> ipconfig /all

Carte réseau sans fil Wi-Fi :
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.73.73(préféré)
```
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi

```
PS C:\Users\ghass> ipconfig /all

Carte réseau sans fil Wi-Fi :
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
```
### ☀️ Déso pas déso

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi
```
10.33.64.0
```
-   l'adresse de broadcast
```
10.33.79.255
```

- le nombre d'adresses IP disponibles dans ce réseau
```
(2**12)-2=4094
```

### ☀️ Hostname

- déterminer le hostname de votre PC

```
PS C:\Users\ghass> hostname
LAPTOP-64JKSH1D
```

### ☀️ Passerelle du réseau
- l'adresse IP de la passerelle du réseau
```
Carte réseau sans fil Wi-Fi :
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
```
- l'adresse MAC de la passerelle du réseau

```
PS C:\Users\ghass> arp -a

Interface : 10.33.73.73 --- 0x4
  Adresse Internet      Adresse physique      Type
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```
### ☀️ Serveur DHCP et DNS

- l'adresse IP du serveur DHCP qui vous a filé une IP
```

Carte réseau sans fil Wi-Fi :
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
```
- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet
```
Carte réseau sans fil Wi-Fi :
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

### ☀️ Table de routage

- dans votre table de routage, laquelle est la route par défaut

```
PS C:\Users\ghass> route print
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254      10.33.73.73     30
```
## II. Go further

### ☀️ Hosts ?
- faites en sorte que pour votre PC, le nom b2.hello.vous corresponde à l'IP 1.1.1.1,
prouvez avec un ping b2.hello.vous que ça ping bien 1.1.1.1

```
PS C:\Users\ghass> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=252 ms TTL=55

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 2, reçus = 2, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 14ms, Maximum = 252ms, Moyenne = 133ms
```

### ☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...

- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo

```
64.233.184.188
```
- le port du serveur auquel vous êtes connectés
```
49665
```
- le port que votre PC a ouvert en local pour se connecter au port du serveur distant
```
443
```
### ☀️ Requêtes DNS

- à quelle adresse IP correspond le nom de domaine www.thinkerview.com
```

PS C:\Users\ghass> nslookup www.thinkerview.com
Serveur :   dns.google
Address:  8.8.8.8
```

```
PS C:\Users\ghass> nslookup 143.90.88.12
Nom :    EAOcf-140p12.ppp15.odn.ne.jp
Address:  143.90.88.12
```

### ☀️ Hop hop hop

- par combien de machines vos paquets passent quand vous essayez de joindre www.ynov.com
```
PS C:\Users\ghass> tracert ynov.com

Détermination de l’itinéraire vers ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     5 ms    19 ms     2 ms  10.33.79.254
  2     4 ms     2 ms     2 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3   228 ms     3 ms     3 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     4 ms     4 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    15 ms    11 ms    11 ms  164.147.6.194.rev.sfr.net [194.6.147.164]
  6     *        *        *     Délai d’attente de la demande dépassé.
  7     *       19 ms   337 ms  162.158.20.240
  8   207 ms    15 ms   276 ms  172.67.74.226

Itinéraire déterminé.
```
### ☀️ IP publique

