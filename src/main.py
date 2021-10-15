from dotenv import load_dotenv
import os
import requests
import json
import time

# The API being used for ip change detection :
# https://www.ipify.org/
# Surprise Surpise , this website claim 99% uptime with unlimited requests!!!

# I also wanted to include some traceroute method for ip changin , maybe soon.

# NOTE : I still havent handled all exceptions like no internet connection , I will
# add these soon

load_dotenv()
env_vars = (os.getenv("KEY"), os.getenv("ZONE"), os.getenv("ID"),
            os.getenv("EMAIL"), os.getenv("NAME"), os.getenv("TYPE"))

#This tests for a working internet connection
try:
    request = requests.get("https://www.cloudflare.com/", timeout=5)
    print("Connection Established")
except:
    print("No internet connection") # or cloudflare is down :P

else: # Code only executes if internet connection is established
    try:    
        print("Env vars : ")
        print("Key : ", os.getenv("KEY"))
        print("Zone : ", os.getenv("ZONE"))
        print("Domain ID : ", os.getenv("ID"))
        print("Clouflare Account : ", os.getenv("EMAIL"))
        print("Domain Name : ", os.getenv("NAME"))
        print("Domain Type : ", os.getenv("TYPE"))
    except:
        print("Hmm seems like I cant all/few of your env vars , please create a .env file")

    if env_vars.count(None) > 0:
        print("Hmm seems like I cant all/few of your env vars , please create a .env file")

    ipaddr_obj = json.loads(requests.get(
        "https://api64.ipify.org?format=json").text)
    prev = ipaddr_obj["ip"]

    # initial dns update :
    print("Updating DNS pointers!")
    # Building CURL command:

    headers = {
        "X-Auth-Email": os.getenv("EMAIL"),
        "X-Auth-Key": os.getenv("KEY"),
        "Content-Type": "application/json",
    }
    data = json.dumps(
        {
            "type": os.getenv("TYPE"),
            "name": os.getenv("NAME"),
            "content": prev,
            "ttl": 1,
        }
    )

    try:
        response = json.loads(
            requests.put(
                "https://api.cloudflare.com/client/v4/zones/"
                + os.getenv("ZONE")
                + "/dns_records/"
                + os.getenv("ID"),
                headers=headers,
                data=data,
                timeout=10
            ).text
        )
    except TypeError:
        print("Seems like your env vars are not valid!")
    except:
        print("Unable to connect to CloudFlare")

    else: # Code only executes if env vars are valid
        print(response["success"])
        if response["success"] == True:
            print("IP Updated!")
        else:
            print("Sorry!Something went wrong :( , check your env var")

        # looping check

        while True:
            # Catches exception if the response times out or another error while connecting to ipify
            try:
                ipaddr_obj = json.loads(requests.get(
                    "https://api64.ipify.org?format=json", timeout=10).text)
            except:
                print("ipify.org seems to be down.")

            current = ipaddr_obj["ip"]
            print("Your ip address currently :", current)
            print("IP has changed ? :", end="")
            if prev != current:
                prev = current
                print("YES")
                print("Updating DNS pointers!")
                # Building CURL command:

                headers = {
                    "X-Auth-Email": os.getenv("EMAIL"),
                    "X-Auth-Key": os.getenv("KEY"),
                    "Content-Type": "application/json",
                }

                data = json.dumps(
                    {
                        "type": os.getenv("TYPE"),
                        "name": os.getenv("NAME"),
                        "content": current,
                        "ttl": 1,
                    }
                )
                response = json.loads(
                    requests.put(
                        "https://api.cloudflare.com/client/v4/zones/"
                        + os.getenv("ZONE")
                        + "/dns_records/"
                        + os.getenv("ID"),
                        headers=headers,
                        data=data,
                    ).text
                )
                print(response["success"])
                if response["success"] == True:
                    print("IP Updated!")
                else:
                    print("Sorry!Something went wrong :( , check your env var")
                    exit()
            else:
                print("NO")

            time.sleep(8)
