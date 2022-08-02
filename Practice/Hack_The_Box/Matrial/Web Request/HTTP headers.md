# Headers

---

HTTP headers provide an additional way to pass information between the client and the server. There are headers specific to requests and responses as well as general headers common to both. Headers can have one or multiple values appended after the header name and separated by a colon. There are many headers used for different purposes, which are divided into different categories:

1.  `General Headers`
2.  `Entity Headers`
3.  `Request Headers`
4.  `Response Headers`
5.  `Security Headers`

---

## 1. General Headers

These headers don't belong specifically to a request or a response. They are contextual and are used to describe the message rather than its contents. This [link](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html) provides additional information on general headers.

**Header**

**Description**

`Date`

The `Date` header holds the date and time at which the message originated. It's preferred to convert the time to the standard [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time zone.

`Connection`

The `Connection` header dictates if the current network connection should stay alive after the request finishes. Two commonly used values for this header are `close` and `keep-alive`. The `close` value from either the client or server means that they would like to terminate the connection, while the `keep-alive` header indicates that the connection should remain open.

#### General Headers - Example

  General Headers - Example

```shell-session
DimasMaulana@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

<SNIP>
Date: Sun, 06 Aug 2020 08:49:37 GMT
Connection: keep-alive
```

---

## 2. Entity Headers

Similar to general headers, entity headers can be common to both the request and response. These headers are used to describe the content (entity) being transferred by a message. They are usually found in responses and POST or PUT requests (for example, a file upload). Additional information on entity headers can be found [here](https://www.w3.org/Protocols/rfc2616/rfc2616-sec7.html).

**Header**

**Description**

`Content-Type`

This header is used to describe the type of resource being transferred. The value is automatically added by the browsers on the client-side and returned in the server response.

`Media-Type`

The `media-type` describes the data being passed. For example, the media-type for a PDF is `application/pdf`, while the type for a PNG image is `image/png`. This header can play a crucial role in making the server interpret our input. The `charset` field denotes the encoding standard, such as [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

`Boundary`

The `boundary` directive acts as a maker to separate content when there is more than one in the same message.

`Content-Length`

The `Content-Length` header holds the size of the entity being passed. This header is necessary as the server uses it to read data from the message body.

`Content-Encoding`

Data can undergo multiple transformations before being passed. For example, large amounts of data can be compressed to reduce the message size. The type of encoding being used should be specified using the `Content-Encoding` header.

#### Entity Headers - Example

  Entity Headers - Example

```shell-session
DimasMaulana@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

<SNIP>
Content-Length: 26012
Content-Type: text/html; charset=ISO-8859-4
Content-Encoding: gzip
```

---

## 3. Request Headers

The client sends request headers in an HTTP transaction. They are defined in [RFC 2616](https://tools.ietf.org/html/rfc2616). These headers are used in an HTTP request and do not relate to the content of the message. Headers such as `Accept`, `Accept-*`, and `IF-*` allow for conditional requests. Headers such as `Cookie` or `User-Agent` are sent so that the server can tailor the response. The following headers are commonly seen in HTTP requests. A complete list of request headers and their usage can be found [here](https://tools.ietf.org/html/rfc7231#section-5).

**Header**

**Description**

`Host`

The `Host` header is used to specify the host being queried for the resource. This can be a domain name or an IP address. HTTP servers can be configured to host different websites, which are revealed based on the hostname. This makes the host header an important enumeration target.

`User-Agent`

The `User-Agent` header is used to describe the client requesting resources. For example, a browser or a library. This header can reveal a lot about the client, such as the browser, its version, and the operating system.

`Accept`

The `Accept` header describes which media types the client can understand. It can contain multiple media types separated by commas. The `*/*` value signifies all media types.

`Cookie`

The `Cookie` header should contain cookie-value pairs in the format `name=value`. HTTP is a stateless protocol, meaning the server has no way to identify clients connecting to it. This is a problem when hosting protected resources and content. A [cookie](https://en.wikipedia.org/wiki/HTTP_cookie) is a piece of data stored on the client and server, which acts as an identifier. These are passed to the server per request, thus maintaining the client's access. Cookies can also serve other purposes, such as saving user preferences or session tracking. There can be multiple cookies in a single header separated by a semi-colon.

`Referer`

The `Referer` header denotes where the current request is coming from. For example, clicking a link from Google search results would make `https://google.com` the referer. Trusting this header can be dangerous as it can be easily manipulated, leading to unintended consequences.

`Authorization`

The `Authorization` HTTP header is another way for the server to identify clients. After successful authentication, the server returns a token unique to the client. Unlike cookies, tokens are stored only on the client-side and retrieved by the server per request. There are multiple types of authentication types based on the webserver and application type used.

#### Request Headers - Example

  Request Headers - Example

```shell-session
DimasMaulana@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

Host: www.inlanefreight.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)
Cookie: cookie1=298zf09hf012fh2; cookie2=u32t4o3tb3gg4
Accept: text/plain
Referer: https://www.hackthebox.eu/
Authorization: BASIC cGFzc3dvcmQK
<SNIP>
```

---

## 4. Response Headers

HTTP response headers can be used in an HTTP response and don't relate to the message's content. Certain response headers such as `Age`, `Location`, and `Server` are used to provide more context about the response. The following headers are commonly seen in HTTP responses. [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6) contains more detailed information on Response headers.

**Header**

**Description**

`Server`

The `Server` header contains information about the HTTP server, which handled the request. It can be used to gain information about the server, such as its version, and enumerate it further.

`Set-Cookie`

The `Set-Cookie` header contains the cookies needed for client identification. Browsers parse the cookies and store them for future requests. This header follows the same format as the `Cookie` header.

`WWW-Authenticate`

The `WWW-Authenticate` header notifies the client about the type of authentication required to access the requested resource.

#### Response Headers - Example

  Response Headers - Example

```shell-session
DimasMaulana@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

<SNIP>
Server: Apache/2.2.14 (Win32)
Set-Cookie: name1=value1,name2=value2; Expires=Wed, 09 Jun 2021 10:18:14 GMT
WWW-Authenticate: BASIC realm="localhost"
```

---

## 5. Security Headers

With the increase in the variety of browsers and web-based attacks, it was necessary to define certain headers that enhanced security. HTTP Security headers are a class of response headers used to specify certain rules and policies to be followed by the browser while accessing the website.

The [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) is a great resource for further reading about the various HTTP security header possibilities.

**Header**

**Description**

`Content-Security-Policy`

The CSP header dictates the website's policy towards externally injected resources. This could be JavaScript code as well as script resources. This header instructs the browser to accept resources only from certain trusted domains, hence preventing attacks such as [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting).

`Strict-Transport-Security`

The HTTP Strict Transport Security policy of a website prevents the browser from accessing the website over the plaintext HTTP protocol. All communication is done via the secure HTTPS protocol. This prevents attackers from sniffing web traffic and accessing protected information such as passwords or other sensitive data.

`Referrer-Policy`

This header dictates whether the browser should include the value specified via the `Referer` header or not. It can help in avoiding disclosing sensitive URLs and information while browsing the website.

#### Security Headers - Example

  Security Headers - Example

```shell-session
DimasMaulana@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

<SNIP>
Content-Security-Policy: script-src 'self'
Strict-Transport-Security: max-age=31536000
Referrer-Policy: origin
```

The section above covers a small list of commonly seen HTTP headers. However, there are many more contextual headers that can be used during communication. It's also possible for applications to define custom headers based on their requirements. A complete list of standard HTTP headers can be found at [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).