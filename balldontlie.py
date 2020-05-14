import json, requests

class balldontlie:
    '''Base class that interacts with the "balldontlie" api'''
    def __init__(self, url):
        '''Payload specifies that there should be 100 results per page to minimize
        the total amount of pages'''
        payload = {'per_page': 100}
        data = requests.get(url, params=payload).json()
        self.data = data['data']
        self.totalpages = data['meta']['total_pages']
    
    def __repr__(self):
        return "Data: {} \n Total Pages: {}".format(self.data, self.totalpages)
        




class player:
    '''This class provides the user with basic details about a player which include
    their first name, last name, and id num. This information can later be used 
    to calculate their stats'''
    def __init__(self, firstname, lastname, idnum):
        self.firstname = firstname
        self.lastname = lastname
        self.idnum = idnum
    '''This function requests the average stats for however many seasons the user
    inputs from the API, returning a stat object'''
    def getstats(self, player, seasons):
        url = 'https://www.balldontlie.io/api/v1/season_averages?season=' + str(seasons) +'&player_ids[]=' + str(self.idnum)
        data = requests.get(url).json()
        for info in data['data']:
            '''Occasionally there may be an error within the api resulting in
            there being a none type when parsing through the data in the api'''
            if type(data['data']) is None:
                continue
            else:
                return stats(info['pts'], info['ast'], info['reb'], info['blk'], 
                info['stl'], info['games_played'], info['fga'], info['fgm'], 
                info['fg3a'], info['fg3m'], info['fta'], info['ftm'], 
                info['turnover'])

        
        

class stats:
    '''This class models the data that the API with its attributes being every
    basic basketball stat recorded for players.'''
    def __init__(self, points, assists, rebounds, blocks, steals, games_played, fga
    ,fgm, fg3a, fg3m, fta, ftm, turnovers):
        self.points = points
        self.assists = assists
        self.rebounds = rebounds
        self.blocks = blocks
        self.steals = steals
        self.games_played = games_played
        self.fga = fga
        self.fgm = fgm
        self.fg3a = fg3a
        self.fg3m = fg3m
        self.fta = fta
        self.ftm = ftm
        self.turnovers = turnovers
    def __repr__(self):
        return '''Points: {} \n Assists: {} \n Rebounds: {} \n Blocks: {} \n Steals: {} \n Games Played: {} \n FGA: {} \n FGM: {} \n FG3A: {} \n FG3m: {} \n FTA: {} \n FTM: {} \n Turnovers {} \n'''.format(self.points, self.assists, self.rebounds, self.blocks, 
        self.steals, self.games_played, self.fga, 
        self.fgm, self.fg3a, self.fg3m, self.fta, self.ftm, self.turnovers)
    
    '''This function calculates player efficiency rating which is a stat that many
    consider to be an accurate measurement of how much a singular player has an
    affect on the game. The function returns a floating point number.'''
    def calculate_PER(self, playerstat):
        '''credit to http://www.rustylarue.com/more-than-94/player-efficiency-stats 
        for the equation'''
        return round(float(self.fgm * 2) - float(self.fga * .75) + float(self.fg3m * 3) 
        - float(self.fg3a * .84) + float(self.ftm) - float(self.fta * -.65) + 
        float(self.rebounds) + float(self.assists) + float(self.blocks) + 
        float(self.steals)  - float(self.turnovers), 3)
