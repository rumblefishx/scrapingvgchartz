from Page import Page
from Configuration import Configuration
from FileManager import FileManager
from Enums.EPlatform import EPlatform
import argparse
import sys
import os
import datetime

class Vgchartzdown:
    
    def __init__(self):
        self.__platform = None
        self.__output = EPlatform.ALL

    def read_input_parameters(self):
        parser = argparse.ArgumentParser(description='A script with named parameters')
        parser.add_argument('-platform', '--platform', type=str, help='Video-Game Platform (PS4,NS,XOne) | -platform "PS4"')
        parser.add_argument('-output', '--output', type=str, help='Output file Directory | -output "c\\output\\"')
        
        args_list = ['-o', 'c:\\output\\','-p','PLAY']
        args = parser.parse_args(args_list)
        
        if self.isValidInput(args) == False:
            sys.exit()
            
        self.__output = args.output
        self.__platform = EPlatform[args.platform]
        
    def execute(self):
        
        try:
            self.read_input_parameters()   
        except SystemExit:
            print("Exiting program...") 
            return
        
        conf = Configuration()  
        fm = FileManager(
            output_folder=self.__output,
            file_name=self.getFileName(
                self.__platform,
                conf.get_file_extension()))
        
        page = Page(conf.get_default_base_url(),platform=self.__platform)
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
            
    def isValidInput(self,args):
        
        if(args.output == None):
            print("You must inform a valid output folder!")
            return False
        
        if(os.path.exists(args.output) == False):
            print("Output folder does not exist! Path --> {}".format(args.output))
            return False
            
        if(args.platform == None):
            print("You must inform a platform (ex: -p 'XBOX')")
            return False
        
        if((args.platform in EPlatform._member_names_) == False):
            print("You must inform a valid platform (PLAY / XBOX / NS)")
            return False
            
        return True
    
    def getFileName(self,platform=EPlatform.ALL,extension=".csv"):      
        baseName = platform.value
        dt = f'{datetime.datetime.now():_%d%m%Y_%H%M%S}'
        return ''.join([baseName,dt,extension])
    

if __name__ == "__main__":    
    program = Vgchartzdown()
    program.execute()