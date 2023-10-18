from Page import Page
from Configuration import Configuration
from FileManager import FileManager
from Enums.EPlatform import EPlatform

if __name__ == "__main__":
    
    if(1==1):
        exit
    
    conf = Configuration()  
    fm = FileManager(
        output_folder=conf.get_output_folder(),
        file_name=conf.get_file_name(),
        extension=conf.get_file_extension(),
        append_time=False)
    
    page = Page(conf.get_default_base_url(),
                headers=conf.get_file_headers(),
                platform=EPlatform.NINTENDO_SWITCH)
    iteration = 1
    savepoints = 3
    games = []
    
    while(True):
        try:  
            print("page : %d"%page.get_current_page())
            page.load()  
            
            if(len(page.get_games()) == 0):
                fm.saveOutput(games,headers)
                break
                
            games.extend(page.get_games())
            page = page.next_page()
            iteration = iteration + 1
            
            if(iteration % savepoints == 0):
                headers = conf.get_file_headers().split(",")
                fm.saveOutput(games,headers)
                games = []
                
        except FileNotFoundError as ex:
            if(len(games) > 0):
                fm.saveOutput(games)
            print(ex)
            break