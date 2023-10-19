from datetime import datetime 
import os
import csv

class FileManager():
    
    def __init__(self,output_folder,file_name):
        self.__output_folder = output_folder
        self.__file_name = file_name
        
    def getOutputFolder(self):
        return self.__output_folder
    
    def getFileName(self):
        return self.__file_name
    
    def saveOutput(self,games=[{"empty"}],headers = [{"empty"}]):
        
        fulladdress = ''.join([self.getOutputFolder(),self.getFileName()])
        
        try:
            with open(fulladdress,"a",newline='',encoding="utf-8") as file:
                wrt = csv.writer(file)
                
                if(os.stat(fulladdress).st_size == 0):
                    wrt.writerow(headers)
                    
                for game in games:
                    wrt.writerow(game.to_row_format())                    
            
        except Exception as e:
            print("ERROR DURING FILE WRITING / ERROR --> {}"
                  .format(e))
        finally:
            file.close()
            
