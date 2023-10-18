import configparser

class Configuration:
    
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("settings.properties")
        self.__url_default_base = str(parser.get("URL","url.base.default").strip('"'))
        self.__output_folder = str(parser.get("FILE","file.output.folder").strip('"'))
        self.__filename = str(parser.get("FILE","file.output.file.name").strip('"'))
        self.__file_extension = str(parser.get("FILE","file.output.file.extension").strip('"'))
        self.__file_headers = ''.join([parser.get("FILE","file.output.file.headers").strip('"')])
        
    def get_default_base_url(self):
        return self.__url_default_base
    
    def get_output_folder(self):
        return self.__output_folder
    
    def get_file_name(self):
        return self.__filename
    
    def get_file_extension(self):
        return self.__file_extension
    
    def get_file_headers(self):
        return self.__file_headers