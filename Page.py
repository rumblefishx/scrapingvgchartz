import requests 
from Enums.EPlatform import EPlatform
from Enums.EGenre import EGenre
from Game import Game
from bs4 import BeautifulSoup
from DateUtils import DateUtils

class Page:
        
    def __init__(self,base,page=1,platform=EPlatform.ALL,genre=EGenre.ALL):
        self.__url_base = base
        self.__page = page
        self.__platform = platform.value
        self.__genre = genre.value  
        self.__games = [] 
        
    def next_page(self):
        self.__page = self.__page + 1
        self.load()
        return self
        
    def get_current_page(self):
        return self.__page
    
    def get_platform(self):
        return self.__platform
    
    def get_genre(self):
        return self.__genre
    
    def get_games(self):
        return self.__games
    
    def load(self):
        self.__games.clear()
        
        url = self.__url_base.format(
            self.__page,
            self.__platform,
            self.__genre
        )
            
        response = requests.get(url)
        
        du = DateUtils()

        if response.status_code == 200:
            source = response.text
            parser = BeautifulSoup(source, 'html.parser')
            mainDiv = parser.find('div',{"id": "generalBody"})

            dataTable = mainDiv.find_next('table')
            
            dataRows = dataTable.find_all('tr')
            
            if(len(dataRows) > 3):
                for game in dataRows[3:]:
                    gameDetails = game.find_all("td")           
                    
                    dateStr = du.get_formatted_date(gameDetails[14].contents[0].strip())
                    
                    attr = {
                            #Game Title
                            'title':gameDetails[2].find_next("a").contents[0].strip().encode('utf-8').decode('charmap'),
                            #Game Console
                            'console':gameDetails[3].find_next("img")['alt'],
                            #Publisher
                            'publisher':gameDetails[4].contents[0].strip(),
                            #Developer
                            'developer':gameDetails[5].contents[0].strip(),
                            #Critic Score
                            'critic_score':gameDetails[7].contents[0].strip(),
                            #User Score
                            'user_score':gameDetails[8].contents[0].strip(),
                            #Total Shiped
                            'total_shipped':gameDetails[9].contents[0].strip(),
                            #Total Sales
                            'total_sales':gameDetails[10].contents[0].strip(),
                            #NA Sales
                            'na_sales':gameDetails[11].contents[0].strip(),
                            #PAL Sales
                            'pal_sales':gameDetails[12].contents[0].strip(),
                            #Japan Sales
                            'japan_sales':gameDetails[13].contents[0].strip(),
                            #Release Date
                            'release_date':dateStr
                            }

                    game = Game(attr)            
                    self.__games.append(game)                   
                    
        else:
            raise FileNotFoundError("The Page Requested Has Not Been Found ! (number: {})".format(self.__page))