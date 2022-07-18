# POST Method

---

Unlike the `GET` method, the `POST` places user parameters in an HTTP Request body. This has three main benefits:

-   `Lack of Logging`: This may sound counter-intuitive as logging is generally viewed as a good thing. However, POST Requests can handle tasks such as file uploads and user logins. Logging these fields can result in the local disk filling up or passwords being stored in plaintext. When coming across a login form that accepts logins via a `GET` request, this should always be a `HIGH` finding as it will likely result in credentials being stored in log files.
    
-   `Less Encoding Requirements`: URLs are designed to be shared, which means they need to confirm to characters that can be converted to letters. The POST request places data in the body which can accept binary data. The only characters that need to be encoded are those that are used to separate parameters.
    
-   `More data can be sent`: The maximum URL Length varies between browsers (Chrome/Firefox/IE), web servers (IIS, Apache, nginx), Content Delivery Networks (Fastly, Cloudfront, Cloudflare), and even URL Shorteners (bit.ly, amzn.to). Generally speaking, URL's should be kept to below 2,000 characters.
    

Note: The domain "http://inlanefreight.com" is used here as an example, which you need to replace with the IP address of your spawned target.

---

## Examining a Request

Let's examine a simple web page that utilizes POST Requests to handle logins. We will log in with the administrative credentials (`admin:password`), then examine how web servers keep track of who we are. Below is the login page. You can follow along by spawning the target at the end of this section. `The credentials to the target is guest/guest`, because you will need to examine the cookie to escalate and escalate to the admin user.

 

![](https://academy.hackthebox.com/storage/modules/35/post_panel.png)

We can log into the application with `admin: password` or `guest:guest`. If we want to log out of the website, we can either find the `logout` button or delete our cookies by clicking on the lock icon followed by `Clear Cookies and Site Data`. It is recommended to utilize the `logout` button of websites because this gives the webserver notice that you want to logout. By clearing cookies, you never notify the web server that you want to log out, and it will not have a chance to terminate your cookies. If your cookies were intercepted, the person who intercepted them would have access to your account until they expire (generally 30 days).

![clear_cookies](https://academy.hackthebox.com/storage/modules/35/clear_cookies.png)

Now that the cookies are cleared, we can log in again. This time we will turn on Burp before logging in to intercept the login credentials and view the request.

![post_login_intercept](https://academy.hackthebox.com/storage/modules/35/post_login_intercept.png)

We see a `POST` request being made to `/login.php`. The `Content-Type` header is set to `application/x-www-form-urlencoded`, which is the media type for URL encoded form data. The request's body is found to contain two parameters, i.e., `username` and `password` with the values `admin` and `password`.

Hit `[Ctrl + R]` to send this request to Repeater and click Send.

![post_repeater_302](https://academy.hackthebox.com/storage/modules/35/post_repeater_302.png)

After sending the request through Repeater, we see that the page returns a `302 Found` response code. We also see a cookie named `PHPSESSID` through the `Set-Cookie` header. The `Location` header signifies the page we're being redirected to. However, sending a request with an incorrect password results in a `200 OK` with a `Login Failed` message.

In this case, due to the name PHPSESSID, it is apparent that the cookie is a "Session," which is just a unique string of characters. Generally speaking, Session ID's are almost always `hashes`, which can be identified by:

-   Containing only hexadecimal characters. (a-f, 0-9).
-   Being divisible by 8.

Every user of the application has a unique Session ID, which maps to either a file or database entry on the server, which stores information about your login. Not all applications utilize sessions. Many frameworks will allow the user to hold information about their login session. This minimizes the processing power of the webserver as it no longer has thousands of sessions to keep track of.

To do this securely, the webserver must cryptographically sign the request and provide the user the hash to the data they hold. Due to the user not knowing the signing key used to create the hash, they cannot modify the data. However, if no signing key is utilized, the user can modify the cookie and potentially trick the server into giving them more privileges than intended. When coming across cookies that you don't recognize, it is always important to try to decode them (base64/URL/etc.) and attempt to modify their values.

Let's take a step back and examine what happens on a failed request. Below is a screenshot showing Burp Repeater using the credentials `admin:test` to login.

![post_login_fail](https://academy.hackthebox.com/storage/modules/35/post_login_fail.png)

Now that we understand what happens on a successful and unsuccessful login. Let us verify that the server treats us as an unauthenticated user upon tampering with the Cookie.

Navigate back to the page and log into the web application. You can either disable Burpsuite during login or simply `forward` the request in burp. Once you are logged in, enable Burp and refresh the page to see the request sent to the server.

![post_dash_intercept](https://academy.hackthebox.com/storage/modules/35/post_dash_intercept.png)

We see the request being sent to `/admin/dashboard.php` along with the cookie. We know that cookies are used to identify a client; what if we remove the cookie header? Hit `[Ctrl + R]` to send it to Repeater and then delete the cookie header.

![post_dash_redir](https://academy.hackthebox.com/storage/modules/35/post_dash_redir.png)

It's found that the server redirects us back to the login page. This is because it had no way to confirm that we had already authenticated to the service. Hit `[Ctrl + Z]` to undo the changes and retain the cookie header.

![post_dash_succ](https://academy.hackthebox.com/storage/modules/35/post_dash_succ.png)

This time there was no redirection, and we have access to the admin dashboard.

---

## Content-Type

The Content-Type Header is a crucial piece to the POST Request. This tells the webserver what type of content to expect. In our examples above, it was set to `application/x-www-form-urlencoded`. Which tells the server to expect something along the lines of: `ParamName1=Value1&ParamName2=Value`.

There are many other content types. Another popular one is `application/json`, which is used for [JSON](https://en.wikipedia.org/wiki/JSON) resources. JSON or JavaScript Object Notation is a simplified way to store and transfer data and is easy to interpret and parse. A JSON object consists of data-value pairs enclosed with braces.

For example:

Code: json

```json
{ "name1" : "value1", "name2" : "value2" }
```

Multiple libraries and applications support JSON input, including web applications. It's often possible to alter the Content-Type and make applications parse inputs in different formats.

Let's intercept a request to the login page and try sending the following JSON input.

Code: json

```json
{ "username" : "admin", "password" : "password" }
```

The Content-Type header should be changed to `application/json` for the server to parse it as JSON.

![post_json](https://academy.hackthebox.com/storage/modules/35/post_json.png)

We see that the server successfully accepted the credentials and is redirecting us to the dashboard.

It can also be seen that setting Content-Type to `application/x-www-form-urlencoded` doesn't result in successful authentication. This is because the server assumes the input to be form data while it's actually JSON.

![post_json_form](https://academy.hackthebox.com/storage/modules/35/post_json_form.png)

Changing between URLEncoded and JSON may seem meaningless, but changing formats may lead to situations that the developer did not expect. Many Frameworks natively support JSON due to having a REST API, which is used when a computer communicates to the webserver versus the user. In programming, JSON is a widely used format for safely storing objects.

An example of this is performing SQL injection on a MongoDB Database. To perform an injection, the attacker must send an array. An example of doing this with `application/x-www-form-urlencoded` is: `username=admin&password[$ge]=0`, which would attempt to tell the server my username is admin and password is greater than 0. Many web servers will not process the request because using brackets on a variable name is not common. However, in REST APIs, arrays are common and will not be blocked by the framework. Changing the request to:

Code: json

```json
{ "username" : "admin", "password" : {"$ge":"0"} }
```

will allow for injection if the developer did not protect against it. Content-Type modification can play a crucial role in finding vulnerabilities and causing unintended bugs in web applications. However, the processing of various media types depends solely on the application logic and what it expects.