# TP7 SECU : Accès réseau sécurisé

## I. VPN

### 🌞 Monter un serveur VPN Wireguard sur vpn.tp7.secu

```
[dany@vpn ~]$ sudo wg show
interface: wg0
  public key: sho1lE98EmKMMP41SBpT9V33mriHoq4KNJqqDoYyVlQ=
  private key: (hidden)
  listening port: 13337

peer: Uvb5wzpbcoxW7f1jcTcczev2prwBSZXecKgAYEV+SVs=
  endpoint: 10.7.1.11:57649
  allowed ips: 10.7.2.11/32
  latest handshake: 1 minute, 7 seconds ago
  transfer: 4.06 KiB received, 4.11 KiB sent
```

### 🌞 Client Wireguard sur martine.tp7.secu

```
[dany@marine wireguard]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=61 time=13.3 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=61 time=15.0 ms
^C
--- 1.1.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 13.273/14.148/15.023/0.875 ms
[dany@marine wireguard]$ sudo wg show
[sudo] password for dany: 
interface: marine
  public key: Uvb5wzpbcoxW7f1jcTcczev2prwBSZXecKgAYEV+SVs=
  private key: (hidden)
  listening port: 57649
  fwmark: 0xca6c

peer: sho1lE98EmKMMP41SBpT9V33mriHoq4KNJqqDoYyVlQ=
  endpoint: 10.7.1.100:13337
  allowed ips: 0.0.0.0/0
  latest handshake: 1 minute ago
  transfer: 4.80 KiB received, 5.16 KiB sent
```
### 🌞 Client Wireguard sur votre PC

```
danyg@danygThinkPad:~/wiregaurd$ ping 10.7.2.11
PING 10.7.2.11 (10.7.2.11) 56(84) bytes of data.
64 bytes from 10.7.2.11: icmp_seq=1 ttl=63 time=2.08 ms
^C
--- 10.7.2.11 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.080/2.080/2.080/0.000 ms

danyg@danygThinkPad:~/wiregaurd$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=56 time=13.8 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=56 time=15.9 ms
^C
--- 1.1.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 13.819/14.837/15.856/1.018 ms
```

### 🌞 Ecrire un script client.sh

## II. SSH

### 🌞 Générez des confs Wireguard pour tout le monde

j'ai fais la conf de bastion et web a la main car je n'ai pas encore fais le script a l'heure où je fais cette partie
- web

```
[dany@web wireguard]$ ping 10.7.2.11
PING 10.7.2.11 (10.7.2.11) 56(84) bytes of data.
64 bytes from 10.7.2.11: icmp_seq=1 ttl=63 time=1.41 ms
64 bytes from 10.7.2.11: icmp_seq=2 ttl=63 time=1.80 ms
^C
--- 10.7.2.11 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 1.407/1.604/1.801/0.197 ms

[dany@web wireguard]$ ping 10.7.2.12
PING 10.7.2.12 (10.7.2.12) 56(84) bytes of data.
64 bytes from 10.7.2.12: icmp_seq=1 ttl=63 time=1.78 ms
64 bytes from 10.7.2.12: icmp_seq=2 ttl=63 time=1.82 ms
^C
--- 10.7.2.12 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 1.783/1.799/1.815/0.016 ms
```
- bastion

```
[dany@bastion wireguard]$ ping 10.7.2.13
PING 10.7.2.13 (10.7.2.13) 56(84) bytes of data.
64 bytes from 10.7.2.13: icmp_seq=1 ttl=63 time=1.29 ms
^C
--- 10.7.2.13 ping statistics ---
2 packets transmitted, 1 received, 50% packet loss, time 1008ms
rtt min/avg/max/mdev = 1.290/1.290/1.290/0.000 ms



[dany@bastion wireguard]$ ping 10.7.2.11
PING 10.7.2.11 (10.7.2.11) 56(84) bytes of data.
64 bytes from 10.7.2.11: icmp_seq=1 ttl=63 time=1.32 ms
^C
--- 10.7.2.11 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.316/1.316/1.316/0.000 ms



[dany@bastion wireguard]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=61 time=14.0 ms
^C
--- 1.1.1.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 13.978/13.978/13.978/0.000 ms
```