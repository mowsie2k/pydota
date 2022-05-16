import requests, json, tkinter, urllib.request, os, glob, profile

API_LINK = 'https://api.opendota.com/api'
PLAYERS_LINK = 'https://api.opendota.com/api/players/'
HEROES_LINK = 'https://api.opendota.com/api/heroes/'

# Classes
# Player
# Holds all data and methods for the Player object. Used to retreive and cache player data based on the playerid.
class Player(object):
    def __init__(self, playerid) -> None:
        self.playerid = playerid
        self.data = {}

    # Populate the Player object
    def populate_data(self):
        # If cached
        if self.check_cache():
            # Load cached data
            self.set_data(self.load_cache())
        # If not cached
        else:
            # Retrieve and cache data
            self.save_cache(self.get_data())
            # Load cached data
            self.set_data(self.load_cache())

    # Check if playerid has cached data
    def check_cache(self):
        if glob.glob('./cache/players/'+self.playerid+'*'):
            # Cached files exist
            return True
        else:
            # Cached files do not exist
            return False

    # Load and return unformatted cache data
    def load_cache(self):
        file = open('./cache/players/'+self.playerid+'_player_data.json',"r")
        data = json.loads(file.read())
        return data
    
    # Format and save cache data
    def save_cache(self,data):
        file = open('./cache/players/'+self.playerid+'_player_data.json',"w")
        file.write(json.dumps(data, indent=4))
        file.close()

    # Retrieve data for playerid
    def get_data(self):
        link = PLAYERS_LINK + self.playerid
        req = requests.get(link)
        data = json.loads(req.text)
        return data

    # Set all data for the Player object
    def set_data(self,data):
        self.data = data

        self.tracked_until = self.data['tracked_until']
        self.solo_competitive_rank = self.data['solo_competitive_rank']
        self.competitive_rank = self.data['competitive_rank']
        self.rank_tier = self.data['rank_tier']
        self.leaderboard_rank = self.data['leaderboard_rank']

        self.mmr_estimate = self.data['mmr_estimate']
        self.mmr_estimate_estimate = self.mmr_estimate['estimate']

        self.profile = self.data['profile']
        self.profile_account_id = self.profile['account_id']
        self.profile_personaname = self.profile['personaname']
        self.profile_name = self.profile['name']
        self.profile_plus = self.profile['plus']
        self.profile_cheese = self.profile['cheese']
        self.profile_steamid = self.profile['steamid']
        # TODO Get images
        self.profile_avatar = self.profile['avatar']
        self.profile_avatarmedium = self.profile['avatarmedium']
        self.profile_avatarfull = self.profile['avatarfull']
        self.profile_profileurl = self.profile['profileurl']
        self.profile_last_login = self.profile['last_login']
        self.profile_loccountrycode = self.profile['loccountrycode']
        self.profile_is_contributor = self.profile['is_contributor']

# Hero data
def get_heroes_data():
    link = HEROES_LINK
    req = requests.get(link)
    data = json.loads(req.text)
    return data

def write_local_heroes_data():
    file = open("heroes_data.json", "w")
    file.write(json.dumps(get_heroes_data(), indent=4))
    file.close()

def read_local_heroes_data():
    file = open("heroes_data.json", "r")
    heroes_data = json.loads(file.read())
    return heroes_data
