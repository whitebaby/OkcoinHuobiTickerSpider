from gevent import monkey; monkey.patch_all()
import time
import urllib2
import json
import MySQLdb
import gevent
conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='',
        db ='btc',
        )
cur = conn.cursor()
def OkCnSpotTicker():
    # print time.time()
    url='https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny' 
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass
    # print time.time()   
    ret = response.read()  
    dict = json.loads(ret)
    # print(dict["ticker"]["last"])
    date = dict['date']              
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']                   
    sqli= "insert into okcnspotticker(date,ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol) values ('%s','%s','%s','%s','%s','%s','%s')" %(date,buy,high,last,low,sell,vol)
    cur.execute(sqli)
    # print time.time()
def OkComSpotTicker():
    url='https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass       
    ret = response.read()  
    dict = json.loads(ret)
    # print(dict["ticker"]["last"])
    date = dict['date']              
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']                   
    sqli= "insert into okcomspotticker(date,ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol) values ('%s','%s','%s','%s','%s','%s','%s')" %(date,buy,high,last,low,sell,vol)
    cur.execute(sqli)
def OkComFutureTickerThisWeek():
    url='https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week'   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass       
    ret = response.read()  
    dict = json.loads(ret)
    # print(dict["ticker"]["last"])
    date = dict['date']              
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']  
    contract_id = dict['ticker']['contract_id']                   
    unit_amount = dict['ticker']['unit_amount']                   
    sqli= "insert into okcomfuturetickerthisweek(date,ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol,ticker_contract_id,ticker_unit_amount) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(date,buy,high,last,low,sell,vol,contract_id,unit_amount)
    cur.execute(sqli)
def OkComFutureTickerNextWeek():
    url='https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=next_week'   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass        
    ret = response.read()  
    dict = json.loads(ret)
    # print(dict["ticker"]["last"])
    date = dict['date']              
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']
    contract_id = dict['ticker']['contract_id']                   
    unit_amount = dict['ticker']['unit_amount']                   
    sqli= "insert into okcomfuturetickernextweek(date,ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol,ticker_contract_id,ticker_unit_amount) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(date,buy,high,last,low,sell,vol,contract_id,unit_amount)
    cur.execute(sqli)
def OkComFutureTickerQuarter():
    url='https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=quarter'   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass       
    ret = response.read()  
    dict = json.loads(ret)
    # print(dict["ticker"]["last"])
    date = dict['date']              
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']                   
    contract_id = dict['ticker']['contract_id']                   
    unit_amount = dict['ticker']['unit_amount']                   
    sqli= "insert into okcomfuturetickerquarter(date,ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol,ticker_contract_id,ticker_unit_amount) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(date,buy,high,last,low,sell,vol,contract_id,unit_amount)
    cur.execute(sqli)
def HuoCnSpotTicker():
    url='http://api.huobi.com/staticmarket/ticker_btc_json.js' 
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass  
    ret = response.read()  
    dict = json.loads(ret)          
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']                   
    sqli= "insert into huocnspotticker(ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol) values ('%s','%s','%s','%s','%s','%s')" %(buy,high,last,low,sell,vol)
    cur.execute(sqli)
def HuoComSpotTicker():
    url='http://api.huobi.com/usdmarket/ticker_btc_json.js' 
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass  
    ret = response.read()  
    dict = json.loads(ret)          
    buy = dict['ticker']['buy']                    
    high = dict['ticker']['high']                    
    last = dict['ticker']['last']                   
    low = dict['ticker']['low']                    
    sell = dict['ticker']['sell']            
    vol = dict['ticker']['vol']                   
    sqli= "insert into huocomspotticker(ticker_buy,ticker_high,ticker_last,ticker_low,ticker_sell,ticker_vol) values ('%s','%s','%s','%s','%s','%s')" %(buy,high,last,low,sell,vol)
    cur.execute(sqli)
def BitVcFutureThisTicker():
      
    url='http://market.bitvc.com/futures/ticker_btc_week.js' 
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass  
    ret = response.read()

    dict = json.loads(ret)          
    buy = dict['buy']                    
    high = dict['high']                    
    last = dict['last']                   
    low = dict['low']                    
    sell = dict['sell']            
    vol = dict['vol']                   
    hold = dict['hold']                   
    ticker_open = dict['open']                   
    limit_highest_price = dict['limit_highest_price']                   
    limit_lowest_price = dict['limit_lowest_price']                   
    contract_type = dict['contract_type']                   
    contract_id = dict['contract_id']                   
    ticker_time = dict['time']                   
    sqli= "insert into bitvcfuturetickerthisweek(buy,high,last,low,sell,vol,hold,open,limit_highest_price,limit_lowest_price,contract_type,contract_id,time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(buy,high,last,low,sell,vol,hold,ticker_open,limit_highest_price,limit_lowest_price,contract_type,contract_id,ticker_time)
    cur.execute(sqli)
def BitVcFutureNextTicker():
    url='http://market.bitvc.com/futures/ticker_btc_next_week.js' 
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print "Failed to reach the server"
            print "The reason:",e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
    else:
        pass  
    ret = response.read()  
    dict = json.loads(ret)          
    buy = dict['buy']                    
    high = dict['high']                    
    last = dict['last']                   
    low = dict['low']                    
    sell = dict['sell']            
    vol = dict['vol']                   
    hold = dict['hold']                   
    ticker_open = dict['open']                   
    limit_highest_price = dict['limit_highest_price']                   
    limit_lowest_price = dict['limit_lowest_price']                   
    contract_type = dict['contract_type']                   
    contract_id = dict['contract_id']                   
    ticker_time = dict['time']                   
    sqli= "insert into bitvcfuturetickernextweek(buy,high,last,low,sell,vol,hold,open,limit_highest_price,limit_lowest_price,contract_type,contract_id,time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(buy,high,last,low,sell,vol,hold,ticker_open,limit_highest_price,limit_lowest_price,contract_type,contract_id,ticker_time)
    cur.execute(sqli)
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
x = 0
while True:
    # x = 0
    t1 = time.time()
    print x
    gevent.joinall([
        gevent.spawn(OkCnSpotTicker),
        gevent.spawn(OkComSpotTicker),
        gevent.spawn(OkComFutureTickerThisWeek),
        gevent.spawn(OkComFutureTickerNextWeek),
        gevent.spawn(OkComFutureTickerQuarter),
        gevent.spawn(HuoCnSpotTicker),
        gevent.spawn(HuoComSpotTicker),
        gevent.spawn(BitVcFutureThisTicker),
        gevent.spawn(BitVcFutureNextTicker),
    ])
    x = x + 1
    t2 = time.time()
    print t2-t1
    # print GetNowTime()
    time.sleep(1) 
	

