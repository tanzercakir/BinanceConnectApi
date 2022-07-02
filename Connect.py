import requests
from Log import Log
from apiAddresses import *

def Connect (endPoint,pmethod="GET",pheaders={},pparams={},pdata={}):   
    for base in baseList: 
        Url = base + endPoint
        try:
            result = requests.request(pmethod,Url,headers=pheaders,params=pparams,data=pdata)
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if 400 <= result.status_code < 500:
                Log.write(str(e))
        except requests.exceptions.ConnectionError as e:
            Log.write(str(e))  
        except requests.exceptions.TooManyRedirects as e:   
            Log.write(str(e))       
        except requests.exceptions.Timeout as e:
            Log.write(str(e))
        except requests.exceptions.ContentDecodingError as e:
            Log.write(str(e))
        except Exception as e:
            Log.write(str(e))
        else:            
            return result.json()
