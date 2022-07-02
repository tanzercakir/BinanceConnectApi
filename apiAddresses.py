# can be added any api endpoints here
# some of them below are added here for reference


base     = "https://api.binance.com"
address1 = "https://api1.binance.com"
address2 = "https://api2.binance.com"
address3 = "https://api3.binance.com"

baseList = [base,address1,address2,address3]

#Market Data Endpoints
ckh_servertime      = "/api/v3/time"                
exchg_info          = "/api/v3/exchangeInfo"        
order_book          = "/api/v3/depth"               
recent_trades       = "/api/v3/trades"   
aggregate_trades    = "/api/v3/aggTrades"              
latest_price        = "/api/v3/ticker/price"              

#some spot account api may give 400 and 401 errors. Check parameters if that is the case
#Spot Account/Trade
test_order          = "/api/v3/order/test"                  #POST  (HMAC SHA256)
new_order           = "/api/v3/order"                       #POST  (HMAC SHA256)
cancel_order        = "/api/v3/order"                       #DELETE  (HMAC SHA256)
cancel_open_orders  = "/api/v3/openOrders"                  #DELETE (HMAC SHA256)
query_order         = "/api/v3/order"                       #GET  (HMAC SHA256)
current_open_orders = "/api/v3/openOrders"                  #GET  (HMAC SHA256)
account_information = "/api/v3/account"                     #GET  (HMAC SHA256)
account_trade_list  = "/api/v3/myTrades"                    #GET  (HMAC SHA256)   
all_orders          = "/api/v3/allOrders"                   #GET  (HMAC SHA256)
CurrentOrderCount   = "/api/v3/rateLimit/order"             #GET  (HMAC SHA256)

#Wallet Endpoints
AllCoinsInformation = "/sapi/v1/capital/config/getall"      #GET  (HMAC SHA256)

#Savings Endpoints
productlist         = "/sapi/v1/lending/daily/product/list" #GET  (HMAC SHA256)

#Mining Endpoints
acquiringAlgorithm  = "/sapi/v1/mining/pub/algoList"        #GET  (HMAC SHA256)

