import urllib.parse
import hmac,hashlib
from secret_api_keys import * #you should place yours
from Connect import Connect
from apiAddresses import ckh_servertime


def ConnectApi(endpoint, params = {},ApiKey = {}, pmeth = "GET"):
    if ApiKey!={}:
        paybytes = urllib.parse.urlencode(params)
        params["signature"] = hmac.new(secret_key.encode("utf-8"), paybytes.encode("utf-8"), hashlib.sha256).hexdigest()
   
    res = Connect(endpoint,pheaders=ApiKey,pparams=params,pmethod=pmeth) 
    return res


#you can use as 
#GetTimeStamp() 
#or anyDictionary.update(GetTimeStamp())
def GetTimeStamp():
    dict={}
    dict["timestamp"] = str(ConnectApi(ckh_servertime)["serverTime"])
    return dict
