import requests
import json
import os
from datetime import datetime
def loaddata():
    my_API_Kay = "KL54EKVPQVU3DR8FJCE9TN6NW"
    location = input("Podaj miasto: ")

    if not os.path.exists(f"D:\windowAP\AP\{location}.json"):
        r =requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?key={my_API_Kay} ").json()
        miasto = r["address"]
        with open(f"{miasto}.json","w") as f:
            json.dump(r,f)

    loadJson(f"{location}.json")


def loadJson(patch):
    with open(patch,'r') as f:
        data = json.load(f)
        print("1")

    now = datetime.now().strftime("%H:00:00")
    for i in data["days"][0]["hours"]:
        if i["datetime"] == now:
            print(f"""Temperatura dzisiaj: {T_C(i["temp"])}""")
    

def T_C(zmienna):
    return round((zmienna -32)/2,2)

if __name__ == "__main__":
    loaddata()
    
    #print(now)
