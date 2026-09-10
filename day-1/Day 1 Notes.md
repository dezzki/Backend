
### [API For beginners](https://youtu.be/WXsD0ZgxjRw?si=EBsfAEJ7JVY-Dqmm "https://youtu.be/WXsD0ZgxjRw?si=EBsfAEJ7JVY-Dqmm") - Watched First 2 hours of this video and understood the API (Twilio part)

### Tested with a Twilio trial number 
- Sent texts to my extra number and used GET and POST commands
- Used Rest Foxx
	- Environment
	- Basic Auth
	- Query
	- Body


### [HTTP Header Crash Course](https://www.youtube.com/watch?v=iYM2zFP3Zn0) - Watched the complete thing

- I don't know how to use express server so, had to just watch that part for now.


### Testing Headers myself.

#### Test 1 - ```curl -v example.com```

Output :
```
* Host example.com:80 was resolved.
* IPv6: 2606:4700:90c5:72db:f2ef:5f5:ef6b:ff98
* IPv4: 172.66.147.243, 104.20.23.154
*   Trying [2606:4700:90c5:72db:f2ef:5f5:ef6b:ff98]:80...
*   Trying 172.66.147.243:80...
* Established connection to example.com (172.66.147.243 port 80) from 192.168.1.5 port 56251
* using HTTP/1.x
> GET / HTTP/1.1  {Request Type and Http Protocol}
> Host: example.com
> User-Agent: curl/8.21.0
> Accept: */*
>
* Request completely sent off
< HTTP/1.1 200 OK {Status code 200 - OK}
< Date: Wed, 09 Sep 2026 20:52:33 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
< Server: cloudflare
< Last-Modified: Wed, 02 Sep 2026 22:14:26 GMT
< Allow: GET, HEAD
< Accept-Ranges: bytes
< Age: 12316
< cf-cache-status: HIT
< CF-RAY: a38913caec22f4fe-DEL
<
<!doctype html><html lang="en"><head><title>Example Domain</title><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>
* Connection #0 to host example.com:80 left intact
```

#### Test 2 - ```curl -v api.github.com```

output:
```
* Host api.github.com:80 was resolved.
* IPv6: (none)
* IPv4: 20.207.73.85
*   Trying 20.207.73.85:80...
* Established connection to api.github.com (20.207.73.85 port 80) from 192.168.1.5 port 56103
* using HTTP/1.x
> GET / HTTP/1.1
> Host: api.github.com
> User-Agent: curl/8.21.0
> Accept: */*
>
* Request completely sent off
< HTTP/1.1 301 Moved Permanently {301  - Moved to new URL}
< Content-Length: 0
< Location: https://api.github.com/
<
* Connection #0 to host api.github.com:80 left intact
```

#### Test 3 - ``` curl -v -d "hello=world" https://httpbin.org/post ```

Output :
```
* Host httpbin.org:443 was resolved.
* IPv6: (none)
* IPv4: 98.88.229.31, 44.194.227.11, 44.195.8.204, 100.59.99.192, 3.212.75.38, 98.88.64.13, 18.235.200.183, 100.63.40.118
*   Trying 98.88.229.31:443...
*   Trying 44.194.227.11:443...
* schannel: disabled automatic use of client certificate
* ALPN: curl offers http/1.1
* ALPN: server accepted http/1.1
* Established connection to httpbin.org (98.88.229.31 port 443) from 192.168.1.5 port 49949
* using HTTP/1.x
> POST /post HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.21.0
> Accept: */*
> Content-Length: 11
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 11 bytes
< HTTP/1.1 200 OK
< Date: Wed, 09 Sep 2026 20:54:43 GMT
< Content-Type: application/json
< Content-Length: 431
< Connection: keep-alive
< Server: gunicorn/19.9.0
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
<
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "hello": "world"
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "11",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "curl/8.21.0",
    "X-Amzn-Trace-Id": "Root=1-6aa1c793-42af6104172cdaeb5fe9f688"
  },
  "json": null,
  "origin": "122.161.50.169",
  "url": "https://httpbin.org/post"
}
* Connection #0 to host httpbin.org:443 left intact
```