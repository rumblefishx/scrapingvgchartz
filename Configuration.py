import configparser

class Configuration:
    
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("settings.properties")
        self.__url_default_base = str(parser.get("URL","url.base.default").strip('"'))
        self.__file_extension = str(parser.get("FILE","file.output.file.extension").strip('"'))
        self.__file_headers = ''.join([parser.get("FILE","file.output.file.headers").strip('"')])
        
    def get_default_base_url(self):
        return self.__url_default_base
    
    def get_file_extension(self):
        return self.__file_extension
    
    def get_file_headers(self):
        return self.__file_headers