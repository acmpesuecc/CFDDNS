# DDNS Using CloudFlare

## Getting started

CloudFlare is a really good service to use as you dns, sadly they dont provide service
for pointing your statc dns at your dynamic IP , everyone deserves a domain without that "ddns" in thier domain.

Now , Using this python script you can get your self a cheap domain name, use cloudflare
as DNS and make it works like a DDNS!.

Altho this does take up some work from your side , like setting up a ./src/.env file 
with this structure : 

```
KEY=<api key>
ZONE=<domain zone>
ID=<domain id>
EMAIL=<email assosiated with cloudflare>
NAME=<domain name>
TYPE=<domain type>
```

NOTE : ofc the env file should NOT have <> surrouding those values

## IP API

The API being used for ip change detection :
https://www.ipify.org/
Surprise Surpise , this website claim 99% uptime with unlimited requests!!!

## Instructions to perform a traceroute 
### On Windows

1. Open cmd.
2. Once the Terminal Box is open, type-<br>
      **tracert example.com** <br>
      *(replace example.com with your domain name)*
3. It is also possible to run a traceroute using your access domain or IP:<br>
   **tracert rcbi-b1hp.accessdomain.com<br>
   tracert 64.13.192.208**<br>

### On Mac

1. Open the Terminal app.
2. Once you have your Terminal box open, type<br>
     **traceroute example.com**<br>
    *(replace example.com with your domain name)* <br>
3. It is also possible to run a traceroute using your access domain or IP.<br>
   **traceroute rcbi-b1hp.accessdomain.com**


You should get an output though this...<br> 
If u get an output like  *** or **Request Time Out**, then you know there's likely a network related issue.<br> 

