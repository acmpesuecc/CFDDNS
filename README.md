# DDNS Using CloudFlare

## Getting started

CloudFlare is a really good service to use as you dns, altho they dont provide service
for ddns , and everyone deserves a domain without that "ddns" in thier domain.

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

I also wanted to include some traceroute method for ip changin , maybe soon.

NOTE : I still havent handled all exceptions like no internet connection , I will
add these soon

