from datetime import datetime 
import os
import csv

class FileManager():
    
    def __init__(self,output_folder,file_name,extension,append_time=True):
        self.__output_folder = output_folder
        self.__file_name = file_name
        self.__append_time = append_time
        self.__file_extension = extension
        
    def getOutputFolder(self):
        return self.__output_folder
    
    def getFileName(self):
        return self.__file_name
    
    def getExtension(self):
        return self.__file_extension
    
    def saveOutput(self,games=[{"empty"}],headers = [{"empty"}]):
        
        fulladdress = self.getFullOutputFileAddress()
        
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
            
    def getFullOutputFileAddress(self):
        
        str_1 = ""
        str_2 = ""
        str_3 = ""
        
        str_1 = ''.join([self.getOutputFolder(),self.getFileName()])
        
        if(self.__append_time):
            str_2 = datetime.now().replace(":","")
        
        str_3 = self.getExtension()
        
        return ''.join([str_1,str_2,str_3])