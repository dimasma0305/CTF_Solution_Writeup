# GET Method

---

The HTTP method `GET` is the most commonly used. Its main purpose is to request a given resource and retrieve it. It's possible to send data through a GET request with the help of query parameters. However, this data should be limited, and `POST` should be used if more input is needed.

Let's look at some basic examples demonstrating `GET` requests.

Note: You can follow along by spawning the target at the end of this section first. The domain "http://inlanefreight.com" is used here as an example, which you need to replace with the IP address of your spawned target.

 

![](https://academy.hackthebox.com/storage/modules/35/get_auth.png)

Browsing to the above page prompts us to authenticate. This kind of authentication is known as [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), wherein the server prompts us to provide credentials before access the resource. Entering random values into the fields and clicking `OK` should display the following message.

 

![](https://academy.hackthebox.com/storage/modules/35/get_unauth.png)

The server denied us access to the page due to incorrect credentials. Refresh the page and enter the credentials to proceed:

-   `admin:password`

 

![](https://academy.hackthebox.com/storage/modules/35/get_dash.png)

This lets us into the dashboard, which allows search for ports. Let's take a step back and analyze the request process. Restart the browser so that the authenticated credentials are discarded. Turn on Burp intercept and enter the URL in the browser.

![get_burp_get](https://academy.hackthebox.com/storage/modules/35/get_burp_get.png)

Hit `[Ctrl + R]` to send this to Repeater so that we can look at the response.

![get_burp_401](https://academy.hackthebox.com/storage/modules/35/get_burp_401.png)

Forward the request in Repeater to examine the response. We see that the server responded with `401 Unauthorized` with the `WWW-Authenticate` header. This header notifies the browser that the authentication scheme is `Basic`. Go back to the proxy tab, forward the request and enter the correct credentials in the browser.

![get_auth_header](https://academy.hackthebox.com/storage/modules/35/get_auth_header.png)

This time we see an additional `Authorization` header in the request. This header contains the authentication type, i.e., `Basic` and a [Base64](https://en.wikipedia.org/wiki/Base64) encoded value. This value is nothing but the credentials entered through the browser. Highlight the string and hit `[Ctrl + Shift +B]` to Base64 decode it.

![get_auth_decoded](https://academy.hackthebox.com/storage/modules/35/get_auth_decoded.png)

As we can see, the credentials are put in the form `username:password` before encoding them. This helps the server parse it and authorize us. Click on `Forward` to send the request, after which we should be redirected to the dashboard.

From the previous sections, we know that credentials can be specified via the URL as well. Let's test it out. Restart the browser and enter the following URL.

 

![](https://academy.hackthebox.com/storage/modules/35/get_url.png)

The browser informs us that it's logging us in as the `admin` user. Clicking on `OK` should successfully log us in without any credential prompts.

A few more types of Authorization types are `Digest` and `Bearer`. The `Digest` type is used to hash the credentials using the MD5 hashing algorithm. This prevents cleartext transmission of credentials as opposed to `Basic`. More detailed information on the process can be found [here](https://tools.ietf.org/html/rfc7616).

The `Bearer` type, on the other hand, is used to send "tokens," which identify the client. These tokens can be defined and created by the applications as they wish. They're commonly associated with the [OAuth](https://tools.ietf.org/html/rfc6749) authorization framework.

---

## Query Parameters

Enter something into the search box present on the admin dashboard.

 

![](https://academy.hackthebox.com/storage/modules/35/get_param.png)

After entering "`a`", the query parameter "`port_code`" was appended to the URL with the value "`a`". This means we can also pass data to the page directly without entering it into the search box. For example,

 

![](https://academy.hackthebox.com/storage/modules/35/get_us.png)

It's also possible to use multiple parameter value pairs separated by an "`&`" (`ampersand`).