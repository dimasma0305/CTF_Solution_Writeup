# HTTP Methods and Codes

---

Multiple HTTP methods can be used while accessing resources. In the HTTP protocol, several request methods allow the browser to send information, forms, or files to the server. These methods are used, among other things, to tell the server how to process the request we send and how to reply. Let us look at some of the commonly used methods.

**Method**

**Description**

`GET`

This is the most common HTTP method, which requests a specific resource. Additional data can be passed to the server via query strings.

`POST`

This is another common method used to send data to the server. It can handle multiple types of input, such as text, PDFs, and other forms of binary data. This data is appended in the request body present after the headers. The POST method is commonly used when sending information (forms, logins) or uploading data to a website, such as images or documents.

`HEAD`

This method requests the headers that would be returned if a GET request was made to the server. It doesn't return the request body and is usually made to check the response length before downloading resources.

`PUT`

This method is similar to POST, as it's used to create new resources on the server. Allowing this method without proper controls can lead to the addition of malicious resources (i.e., uploading a malicious file to the webserver).

`DELETE`

This method lets users delete an existing resource on the webserver. It can lead to Denial of Service (DoS) without proper controls in place.

`OPTIONS`

This method returns information about the server, such as the methods accepted by it.

Note: Both "PUT" and "DELETE" are usually associated with WebDAV servers, which will discuss later.

The list above highlights only a few methods. The availability of a particular method depends on the server as well as the application configuration.

---

## Response Codes

The server uses the HTTP status codes to tell the client whether the request was successfully processed. An HTTP server can return five types of response codes:

**Type**

**Description**

`1xx`

Usually provides information and continues processing the request.

`2xx`

Positive response codes returned when a request succeeds.

`3xx`

Returned when the server redirects the client.

`4xx`

This class of codes signifies improper requests from the client. For example, requesting a resource that doesn't exist or requesting a bad format.

`5xx`

Returned when there is some problem with the HTTP server itself.

Let's look at some common HTTP response codes and their meaning.

**Type**

**Description**

`200 OK`

Returned on a successful request, and the response usually contains the requested resource.

`302 Found`

This code redirects the client to another URL. For example, redirecting the user to their dashboard after a successful login.

![paypal](https://academy.hackthebox.com/storage/modules/35/paypal.png)

One common example of seeing redirects is during online shopping, where websites redirect you to the payment gateway.

**Type**

**Description**

`400 Bad Request`

Usually returned on encountering malformed requests such as requests with missing line terminators.

`403 Forbidden`

This code signifies that the client doesn't have appropriate access to the resource. It can also be returned when the server detects malicious input from the user.

![apache_403](https://academy.hackthebox.com/storage/modules/35/apache_403.png)

The image above depicts a 403 Forbidden error returned by Apache.

**Type**

**Description**

`404 Not Found`

Returned when the client requests a resource that doesn't exist on the server.

For example, the following page is seen while trying to visit a non-existent page on Google.

![google_404](https://academy.hackthebox.com/storage/modules/35/google_404.png)

**Type**

**Description**

`500 Internal Server Error`

As the name describes, this code is returned when the server cannot process the request.

![500_error](https://academy.hackthebox.com/storage/modules/35/500_error.png)

The image shows the default page returned by [IIS](https://en.wikipedia.org/wiki/Internet_Information_Services) when it encounters a server error. Apart from the standard HTTP codes, various servers and providers such as [Cloudflare](https://support.cloudflare.com/hc/en-us/articles/115003014432-HTTP-Status-Codes) or [AWS](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APIError.html) implement their own codes.

 Previous

 Mark Complete & Next

Next 

 Cheat Sheet