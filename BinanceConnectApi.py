from ConnectApi import *
from apiAddresses import *
from Log import Log

myLog = Log()
params = {}
hApiKey = {"X-MBX-APIKEY":api_key} #for signed api you must use your own api-secret keys

    
    
#comment out any line you want to test  
#please adjust params dictionary value accordingly  
    
#market data test, unsigned apis
#print(ConnectApi(ckh_servertime))
#print(ConnectApi(latest_price,params))
#print(ConnectApi(exchg_info,params))
#print(ConnectApi(order_book,params))
#print(ConnectApi(recent_trades,params))
#print(ConnectApi(aggregate_trades,params))

#spot account test
#print(ConnectApi(account_information,params=GetTimeStamp(),ApiKey=hApiKey))
#print(ConnectApi(AllCoinsInformation,params=GetTimeStamp(),ApiKey=hApiKey))

params["symbol"] = "BTCUSDT"
params["side"] = "BUY"
params["type"] = "LIMIT"
params["timeInForce"] = "GTC"
params["quantity"] = "1"
params["price"] = "20000"
params.update(GetTimeStamp())

print(ConnectApi(test_order,params=params,ApiKey=hApiKey,pmeth="POST"))

#params.update(GetTimeStamp())
#print(ConnectApi(account_trade_list,params=params,ApiKey=hApiKey)

#print(ConnectApi(CurrentOrderCount,params=GetTimeStamp(),ApiKey=hApiKey))

#mining api test
#print(ConnectApi(acquiringAlgorithm,ApiKey=hApiKey))


	
	
	
	
	