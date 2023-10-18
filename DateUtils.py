from datetime import datetime
from Enums.EMonths import EMonths

class DateUtils:

    def get_formatted_date(self,dtStr):
        
        if(dtStr == "N/A"):
            return dtStr
        
        try:
            dtparts = dtStr.split(" ")
            day = (dtparts[0])[:2]       
            month = self.monthToNumber(dtparts[1])        
            intYear = int(dtparts[2])
            year = ""
            
            if(intYear) > datetime.now().year:
                year = ("19{}".format(intYear))
            else:
                year = ("20{}".format(intYear))
                    
            return '/'.join([day,month,year])
        except Exception as e:
            print("conversionFail -- date ({}) > {}".format(dtStr,e))
            return "conversionFail" 
        
    
    def monthToNumber(self,monthStr):
        for month in EMonths:
            if(month.name == monthStr):
                return "%02d"%month.value

if __name__ == "__main__":
    utils = DateUtils()
    print(utils.get_formatted_date("17th Sep 20"))