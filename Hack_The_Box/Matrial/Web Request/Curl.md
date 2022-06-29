# cURL

---

[CURL](https://curl.haxx.se/) (client URL) is a command-line tool and library which primarily supports HTTP along with many other protocols. This makes it a good candidate for scripts as well as automation. The tool takes in at least one argument, i.e., the resource to fetch.

---

## GET Request

The default HTTP requests made by `cURL` are GET requests. Let's try requesting the page from the GET section.

#### cURL - GET Request

  cURL - GET Request

```shell-session
DimasMaulana@htb[/htb]$ curl http://inlanefreight.com/

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you are authorized to access the document requested.  Either you supplied the wrong credentials (e.g., bad password), or your browser doesn't understand how to supply the credentials required.</p> 
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at inlanefreight.com Port 80</address>
</body></html>
```

Unlike browsers, `cURL` can't render HTML and run JavaScript, meaning the entire response is provided to us raw. As we can see above, the server returned a `401 Unauthorized` page as we didn't specify the credentials. It's possible to view the raw HTTP requests using the "`-v`" switch to increase verbosity.

#### cURL - GET Request Verbose

  cURL - GET Request Verbose

```shell-session
DimasMaulana@htb[/htb]$  curl http://inlanefreight.com/ -v

*   Trying 192.168.0.108:80...
* TCP_NODELAY set
* Connected to inlanefreight.com (192.168.0.108) port 80 (#0)
> GET / HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Unauthorized
< Date: Tue, 21 Jul 2020 05:20:15 GMT
< Server: Apache/2.4.41 (Ubuntu)
< WWW-Authenticate: Basic realm="Restricted Content"
< Content-Length: 464
< Content-Type: text/html; charset=iso-8859-1
< 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>

<SNIP>
```

This time we see the HTTP headers being sent and received. `cURL` understands the standard URL format, which means we can specify credentials in the URL.

#### cURL - Basic AUTH Login

  cURL - Basic AUTH Login

```shell-session
DimasMaulana@htb[/htb]$  curl http://admin:password@inlanefreight.com/ -vvv

*   Trying 192.168.0.108:80...
* TCP_NODELAY set
* Connected to inlanefreight.com (192.168.0.108) port 80 (#0)
* Server auth using Basic with user 'admin'
> GET / HTTP/1.1
> Host: inlanefreight.com
> Authorization: Basic YWRtaW46cGFzc3dvcmQ=
> User-Agent: curl/7.65.3
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Date: Tue, 21 Jul 2020 05:23:27 GMT
< Server: Apache/2.4.41 (Ubuntu)
< location: search.php
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8

<SNIP>
```

It parsed the credentials and added the `Authorization` header with the encoded data. The server then responded with `302 Found`, which means authentication was successful.

Alternately, the "`-u`" flag can be used to specify credentials as well.

#### cURL - Basic AUTH Login

  cURL - Basic AUTH Login

```shell-session
DimasMaulana@htb[/htb]$  curl -u admin:password  http://inlanefreight.com/ -vvv

*   Trying 192.168.0.108:80...
* TCP_NODELAY set
* Connected to inlanefreight.com (192.168.0.108) port 80 (#0)
* Server auth using Basic with user 'admin'
> GET / HTTP/1.1
> Host: inlanefreight.com
> Authorization: Basic YWRtaW46cGFzc3dvcmQ=
> User-Agent: curl/7.65.3
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Date: Tue, 21 Jul 2020 05:25:25 GMT
< Server: Apache/2.4.41 (Ubuntu)
< location: search.php
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
```

Unlike browsers, `cURL` doesn't redirect us to the specified location by default. The "`-L`" flag instructs curl to follow redirections.

#### cURL - Basic AUTH Login & Follow Redirections

  cURL - Basic AUTH Login & Follow Redirections

```shell-session
DimasMaulana@htb[/htb]$ curl -u admin:password -L http://inlanefreight.com/

<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Search Ports</title>

    <link href="./style.css" rel="stylesheet">
        </head>

  <body>
  <h1 align=center>Admin Dashboard</h1>
  <div class="container-narrow" style="width:820px">
<SNIP>
```

This time we're successfully redirected to the dashboard on "`/search.php`". `cURL` doesn't cache credentials as browsers do, which means we'll have to specify them per request. Let's try sending a GET request with the "`port_code`" parameter.

#### cURL - GET Request With Parameter

  cURL - GET Request With Parameter

```shell-session
DimasMaulana@htb[/htb]$ curl -u admin:password 'http://inlanefreight.com/search.php?port_code=us'

<SNIP>
<tr><td style="width:400px" colspan=3>KR PUS</td><td style="width:400px" colspan=3>Busan</td><td style="width:450px" colspan=3>19.85</tr>
<tr><td style="width:400px" colspan=3>US LAX</td><td style="width:400px" colspan=3>Los Angeles</td><td style="width:450px" colspan=3>8.86</tr>
<tr><td style="width:400px" colspan=3>US NYC</td><td style="width:400px" colspan=3>New York</td><td style="width:450px" colspan=3>6.25</tr>
<tr><td style="width:400px" colspan=3>US SAV</td><td style="width:400px" colspan=3>Savannah</td><td style="width:450px" colspan=3>3.64</tr></tbody>
</table>
<SNIP>
```

The request was successful, and the results are returned.

---

## POST Method

Let's try to login to the page from the POST section using `cURL`. The default "`Content-Type`" used by `cURL` is "`application/x-www-form-urlencoded`", the data for which can be passed using the "`-d`" flag.

#### cURL - Passing Data

  cURL - Passing Data

```shell-session
DimasMaulana@htb[/htb]$ curl -d 'username=admin&password=password' -L http://inlanefreight.com/login.php

<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Inlanefreight</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<hgroup>
  <h1>Admin panel</h1>
  <h3>

    </h3>
    </hgroup>
    <form action="" method="post">
      <div class="group">
        <input name="username" type="text"><span class="highlight"></span><span class="bar"></span>
        <label>Username</label>
      </div>
<SNIP>
```

`cURL` automatically sends a POST request when the "`-d`" flag is used. It's found that we're still on the login page even after specifying valid credentials. Let's use the "`-v`" switch to debug this.

#### cURL - Debug

  cURL - Debug

```shell-session
DimasMaulana@htb[/htb]$ curl -d 'username=admin&password=password' -L  http://inlanefreight.com/login.php -v

> POST /login.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> Content-Length: 32
> Content-Type: application/x-www-form-urlencoded
> 
< HTTP/1.1 302 Found
< Date: Tue, 21 Jul 2020 06:45:35 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Set-Cookie: PHPSESSID=j8lf78vrq599vg2hi67miqt3so; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Location: admin/dashboard.php

* Issue another request to this URL: 'http://inlanefreight.com/admin/dashboard.php'
* Switch from POST to GET
> GET /admin/dashboard.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*

< HTTP/1.1 302 Found
< Date: Tue, 21 Jul 2020 06:45:35 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Set-Cookie: PHPSESSID=v4b9c3nbjfnsin756c72jmjbnl; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Location: /login.php
<
* Issue another request to this URL: 'http://inlanefreight.com/login.php'
> GET /login.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Tue, 21 Jul 2020 06:45:35 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Vary: Accept-Encoding
< Content-Length: 938
< Content-Type: text/html; charset=UTF-8
```

The command above shows the entire communication process. First, the POST request is sent with the credentials, which is validated by the server. The server returns a `302 Found` response and redirects us to the dashboard. `cURL` then attempts to send a GET request to the dashboard but is redirected back to the login page.

Why did this happen? On close observation, it can be seen that `cURL` didn't resend the cookies it received after logging in. This leads to authentication failure by the dashboard, ultimately leading to the redirect.

The "`--cookie`" or "`--cookie-jar`" option can be used to specify cookie usage in `cURL`. This can point to `/dev/null` or a file on the disk, where the cookies will be saved.

#### cURL - Cookie

  cURL - Cookie

```shell-session
DimasMaulana@htb[/htb]$ curl -d 'username=admin&password=password' -L --cookie-jar /dev/null  http://inlanefreight.com/login.php -v

> POST /login.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> Content-Length: 32
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 32 out of 32 bytes
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Date: Tue, 21 Jul 2020 06:53:15 GMT
< Server: Apache/2.4.41 (Ubuntu)
* Added cookie PHPSESSID="9gse3o6agurgbjugp81du90hco" for domain inlanefreight.com, path /, expire 0
< Set-Cookie: PHPSESSID=9gse3o6agurgbjugp81du90hco; path=/
< Pragma: no-cache
< Location: admin/dashboard.php
< Content-Length: 938
< Content-Type: text/html; charset=UTF-8
< 

* Issue another request to this URL: 'http://inlanefreight.com/admin/dashboard.php'
* Switch from POST to GET
* Connected to inlanefreight.com (192.168.0.108) port 80 (#0)
> GET /admin/dashboard.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> Cookie: PHPSESSID=9gse3o6agurgbjugp81du90hco
> 
< HTTP/1.1 200 OK
< Date: Tue, 21 Jul 2020 06:53:15 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Expires: Thu, 19 Nov 1981 08:52:00 GM
< Content-Length: 845
< Content-Type: text/html; charset=UTF-8
< 

<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Dashboard</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
<link rel="stylesheet" href="./style.css">

</head>
<body>
<hgroup>
<h1 align=center>Admin panel</h1>
<SNIP>
```

This time the cookie was attached to the subsequent requests, resulting in a successful login.

#### cURL - Cookie File

  cURL - Cookie File

```shell-session
DimasMaulana@htb[/htb]$ curl -d 'username=admin&password=password' -L --cookie-jar cookies.txt  http://inlanefreight.com/login.php

DimasMaulana@htb[/htb]$ cat cookies.txt 
# Netscape HTTP Cookie File
# https://curl.haxx.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

inlanefreight.com       FALSE   /       FALSE   0       PHPSESSID       3rbv7tptmgv0m5u3lnc1dfjkr6
```

Specifying a file name as the argument saves the cookies to a file, which can be used to access the page later directly.

#### cURL - Cookie File

  cURL - Cookie File

```shell-session
DimasMaulana@htb[/htb]$ curl http://inlanefreight.com/admin/dashboard.php -v

DimasMaulana@htb[/htb]$ curl --cookie cookies.txt http://inlanefreight.com/admin/dashboard.php -v

> GET /admin/dashboard.php HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> Cookie: PHPSESSID=8r7dflu3a9i6n1ppos3cfal2v7
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Tue, 21 Jul 2020 07:00:27 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Vary: Accept-Encoding
< Content-Length: 845
< Content-Type: text/html; charset=UTF-8
< 
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Dashboard</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
<link rel="stylesheet" href="./style.css">

</head>
<body>
<hgroup>
<h1 align=center>Admin panel</h1>
<SNIP>
```

As we can see above, the first request without cookies failed, but the second one with the "`--cookie`" flag succeeded.

---

## Content-Type header

It's also possible to send JSON data using `cURL`. This can be done by specifying the "`application/json`" header with the "`-H`" flag.

#### cURL - Content-Type

  cURL - Content-Type

```shell-session
DimasMaulana@htb[/htb]$ curl -H 'Content-Type: application/json' -d '{ "username" : "admin", "password" : "password" }' --cookie-jar /dev/null -L  http://inlanefreight.com/login.php

<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Dashboard</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
<link rel="stylesheet" href="./style.css">

</head>
<body>
<hgroup>
<h1 align=center>Admin panel</h1>
<SNIP>
```

The "`-H`" option can be used to specify any header type. The response above shows that the login was successful with JSON data as well.

---

## PUT and DELETE Methods

The "`-X`" option can be used to specify the request method to use.

#### cURL - OPTIONS Request

  cURL - OPTIONS Request

```shell-session
DimasMaulana@htb[/htb]$ curl -X OPTIONS http://inlanefreight.com/ -vv

* TCP_NODELAY set
* Connected to inlanefreight.com 0 port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: inlanefreight.com
> User-Agent: curl/7.65.3
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.10.3 (Ubuntu)
< Date: Tue, 21 Jul 2020 07:03:22 GMT
< Content-Length: 0
< Connection: keep-alive
< DAV: 1
< Allow: GET,HEAD,PUT,DELETE,MKCOL,COPY,MOVE,PROPFIND,OPTIONS
```

The command above sent an OPTIONS request to the server. Let's try uploading a file using the PUT method.

#### cURL - File Upload

  cURL - File Upload

```shell-session
DimasMaulana@htb[/htb]$ echo "curl file upload!" > test.txt

DimasMaulana@htb[/htb]$ curl -X PUT -d @test.txt http://inlanefreight.com/test.txt -vv

* Connected to inlanefreight.com port 80 (#0)
DimasMaulana@htb[/htb]$ curl http://inlanefreight.com/test.txt

curl file upload!
```

We first create a file named `test.txt`. The "`@`" symbol is used by `cURL` to read the file and send it's contents as the data. As we can see, the file was uploaded successfully and retrieved later.

The `DELETE` method can be used similarly.

#### cURL - DELETE Method

  cURL - DELETE Method

```shell-session
DimasMaulana@htb[/htb]$ curl -X DELETE http://inlanefreight.com/test.txt -vv
*   Trying 192.168.0.108:80...
* TCP_NODELAY set
* Connected to inlanefreight.com (192.168.0.108) port 80 (#0)
DimasMaulana@htb[/htb]$ curl http://inlanefreight.com/test.txt
<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.10.3 (Ubuntu)</center>
</body>
</html>
```

As we can see above, the file was deleted successfully.

---

## Conclusion

In this module, we covered core concepts necessary for beginning to work with web applications such as understanding the differences between HTTP and HTTPS, an analysis of HTTP requests and responses, and an overview of key HTTP headers and methods and response codes. We took a deeper dive into the `GET`, `POST`, `PUT`, and `DELETE` methods with accompanying hands-on exercises. Finally, we covered the basics of the `Burp Suite` and `cURL` tools, which are two essential and powerful tools to have in our toolkits as we continue to work with web applications and begin enumerating and exploiting web application vulnerabilities in later modules. Throughout this module, we were provided with a wealth of external resources worth studying in-depth to gain a firm grasp over these core concepts that will come up again and again in our information security journey.