import requests, json, tkinter, urllib.request

API_LINK = 'https://api.opendota.com/api/'
PLAYERS_LINK = API_LINK + '/players/'

def get_player_link(playerid):
    return (PLAYERS_LINK + str(playerid))

def get_player_data(playerid):
    link = get_player_link(playerid)
    req = requests.get(link)
    data = json.loads(req.text)
    return data

def write_local_player_data(playerid):
    file = open("player_data.json", "w")
    file.write(json.dumps(get_player_data(playerid), indent=4))
    file.close()

def read_local_player_data():
    file = open("player_data.json", "r")
    player_data = json.loads(file.read())
    return player_data

def get_local_tracked_until():
    return read_local_player_data()['tracked_until']

def get_local_solo_competitive_rank():
    return read_local_player_data()['solo_competitive_rank']

def get_local_account_id():
    return read_local_player_data()['profile']['account_id']

def get_local_personaname():
    return read_local_player_data()['profile']['personaname']

def get_local_steamid():
    return read_local_player_data()['profile']['steamid']

def get_local_avatarmedium():
    return read_local_player_data()['profile']['avatarmedium']

def get_avatarmedium():
    image = urllib.request.urlretrieve(get_local_avatarmedium(), "avatarmedium.jpg")
    return image

def get_local_avatarfull():
    return read_local_player_data()['profile']['avatarfull']

def get_avatarfull():
    image = urllib.request.urlretrieve(get_local_avatarfull(), "avatarfull.jpg")
    return image

def get_local_profileurl():
    return read_local_player_data()['profile']['profileurl']
