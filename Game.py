class Game:
    
    def __init__(self, conf):
        if(conf is None):
            return
                
        self.__title = conf.get("title")
        self.__console = conf.get("console")
        self.__publisher = conf.get("publisher")
        self.__developer = conf.get("developer")
        self.__critic_score = conf.get("critic_score")
        self.__user_score = conf.get("user_score")
        self.__total_shipped = conf.get("total_shipped")
        self.__total_sales = conf.get("total_sales")
        self.__na_sales = conf.get("na_sales")
        self.__pal_sales = conf.get("pal_sales")
        self.__japan_sales = conf.get("japan_sales")
        self.__release_date = conf.get("release_date")
        
    def set_title(self,title):
        self.__title = title
        
    def get_title(self):
        return self.__title
        
    def set_console(self,console):
        self.__console = console
    
    def get_console(self):
        return self.__console
        
    def set_publisher(self,publisher):
        self.__publisher = publisher
        
    def get_publisher(self):
        return self.__publisher
    
    def set_developer(self,developer):
        self.__developer = developer 
        
    def get_developer(self):
        return self.__developer
    
    def set_critic_score(self,critic_score):
        self.__critic_score = critic_score
    
    def get_critic_score(self):
        return self.__critic_score
    
    def set_user_score(self,user_score):
        self.__user_score = user_score
        
    def get_user_score(self):
        return self.__user_score
    
    def set_total_shipped(self,total_shipped):
        self.__total_shipped = total_shipped
        
    def get_total_shipped(self):
        self.__total_shipped
        
    def set_total_sales(self,total_sales):
        self.__total_sales = total_sales
        
    def get_total_sales(self):
        return self.__total_sales
    
    def set_na_sales(self,na_sales):
        self.__na_sales = na_sales

    def get_na_sales(self):
        return self.__na_sales
    
    def set_pal_sales(self,pal_sales):
        self.__pal_sales = pal_sales
        
    def get_pal_sales(self):
        return self.__pal_sales

    def set_japan_sales(self,japan_sales):
        self.__japan_sales = japan_sales
        
    def get_japan_sales(self):
        return self.__japan_sales
    
    def set_release_date(self,release_date):
        self.__release_date = release_date
        
    def get_release_date(self):
        return self.__release_date
    
    def to_string(self):
        return ''.join(["Title: {}\n",
                        "Platform: {}\n", 
                        "Publisher: {}\n",
                        "Developer: {}\n",
                        "Critic Score: {}\n",
                        "Total Shipped: {}\n",
                        "Total Sales: {}\n",
                        "NA_Sales: {}\n",
                        "PAL_Sales: {}\n",
                        "Japan_Sales: {}\n",
                        "Release Date: {}\n\n"]).format(self.__title,
                          self.__console,
                          self.__publisher,
                          self.__developer,
                          self.__critic_score,
                          self.__total_shipped,
                          self.__total_sales,
                          self.__na_sales,
                          self.__pal_sales,
                          self.__japan_sales,
                          self.__release_date)
    
    def to_row_format(self):
        return [self.__title,
                self.__console,
                self.__publisher,
                self.__developer,
                self.__critic_score,
                self.__user_score,
                self.__total_shipped,
                self.__total_sales,
                self.__na_sales,
                self.__pal_sales,
                self.__japan_sales,
                self.__release_date]
    
        
