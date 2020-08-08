import requests
import json
from os import system

system("cls")

api_key = ""

class RiotGames():
    def __init__(self,summoner_name,region,api_key):
        self.summoner_name = summoner_name
        self.region = region
        self.api_url = f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key="
        self.api_key = api_key
        self.total_url = f"{self.api_url}{self.api_key}"
        self.result = requests.get(self.total_url)
        self.result_json = json.loads(self.result.text)
        self.id = self.result_json["id"]
        self.level = self.result_json["summonerLevel"]
        print(f"{self.summoner_name} {self.level} Level")
        print("="*30)

    def SoloDuo(self):
        self.url = f"https://{self.region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.id}?api_key={self.api_key}"
        self.url = requests.get(self.url)
        self.url = json.loads(self.url.text)
        for i in self.url:
            if i["queueType"] == "RANKED_SOLO_5x5":
                print(f" Solo Duo Ranked ".center(30,"="))
                print(f'{i["tier"]} {i["rank"]}')
                print(f'{i["leaguePoints"]}LP / {i["wins"]}W {i["losses"]}L')
                win_rate = int((100*i["wins"])/(i["wins"]+i["losses"]))
                print(f"Win Rate {win_rate} %")
                
            
                
    def FlexRanked(self):
        self.url = f"https://{self.region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.id}?api_key={self.api_key}"
        self.url = requests.get(self.url)
        self.url = json.loads(self.url.text)
        for i in self.url:
            if i["queueType"] == "RANKED_FLEX_SR":
                print(f" Flex Ranked ".center(30,"="))
                print(f'{i["tier"]} {i["rank"]}')
                print(f'{i["leaguePoints"]}LP / {i["wins"]}W {i["losses"]}L')
                win_rate = int((100*i["wins"])/(i["wins"]+i["losses"]))
                print(f"Win Rate {win_rate} %")   
                
                

    
        


regions = ["br1","eun1","euw1","jp1","kr","la1","la2","na1","oc1","ru","tr1"]

while True:
    print(f"Enter the region")
    for i in regions:
        print(f"{i}")
    region = input(">")
    if region not in regions:
        print("Invalid region")
        continue
    else:
        break

system("cls")

while True:
    print("Enter summoner name")
    summoner_name = input(">")
    try:
        system("cls")
        r1 = RiotGames(summoner_name,region,api_key)
        r1.SoloDuo()
        r1.FlexRanked()
        break
    except KeyError:
        system("cls")
        print(f"No summoner named {summoner_name} in {region}")
        break
    








    


    
