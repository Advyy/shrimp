import json
import requests

from datetime import datetime, date, timedelta

def read_json(filename): 
    with open(f"./{filename}.json", 'r') as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"./{filename}.json", 'w') as file:
        data = json.dump(data, file, indent=4)
    
def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv

def spoiler(spoil): 
    list1 = spoil.split(" ")

    words = []

    for word in list1: 
        wordList = list(word)
        wordList.append(" ")

        for letter in wordList: 
            if letter == " ": 
                words.append(" ")
            else: 
                words.append(f"||{letter}||")

    final = "".join(words)
    return final

def refresh_token(): 
    creds = read_json("creds")

    client_secret = "lj8ui55fvLXtHppD"
    client_id = "OjvzkK0zlQPxKrnJ4Ck0hR8TdxQqspN3"
    refresh_token_str = creds["refresh_token"]

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    data = {
        "client_secret": client_secret,
        "client_id": client_id, 
        "refresh_token": refresh_token_str,
        "grant_type": "refresh_token", 
        "redirect_uri": "https://advysugar.com"
    }
    req = requests.post(url=f"https://api.dexcom.com/v2/oauth2/token", data=data, headers=headers)

    json_data = req.json()
    
    print(json_data)
    

    creds
    credsData = {
        "auth_token": f'Bearer {json_data["access_token"]}', 
        "refresh_token": json_data["refresh_token"]
    }


    write_json(filename="creds", data=credsData)

def get_sugar(): 
    # refresh_token()
    creds = read_json("creds")
    headers = {
        'authorization': creds["auth_token"]
    }

    time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    today = date.today()
    td = timedelta(1)
    
    
    req = requests.get(url=f"https://api.dexcom.com/v2/users/self/egvs?startDate={time}&endDate={today + td}T12:30:30", headers=headers)
    
    json = req.json()

    

    sugarVal = json["egvs"][-1]
    # sugar = sugarVal["value"]

    return sugarVal