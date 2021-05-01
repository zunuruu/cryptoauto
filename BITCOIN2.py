import time
import pyupbit
import datetime

eb1=0
eb2=0
eb3=0
eb4=0
eb5=0
eb6=0
eb7=0
eb8=0


access = "wo6M91tMd9hyr6k8dQke2zxFRLxubXxYS6uTxRTp"
secret = "9iZPNaw73ngnwxIYobpeU6XxXSr5xR9L9icwv3gX"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        krw = get_balance("KRW")
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #이더리움 자동매매 코드 09:00~08:59
            target_price = get_target_price("KRW-ETH", 0.1) #K=0.1
            current_price = get_current_price("KRW-ETH") 
            if target_price < current_price <target_price*1.01 :
                krw = get_balance("KRW")
                if krw > 5000 and eb1==0:
                    eb1=1 #구매 확인코드
                    upbit.buy_market_order("KRW-ETH", 300000) #30만원 매수 코드
            elif current_price < target_price*0.94 : #손절라인 만들기 코드
                eth = get_balance("ETH")
                if eth > 0.002:
                 upbit.sell_market_order("KRW-ETH", eth*0.9995)
                 eb1=0
        else:
            eth = get_balance("ETH") #종가전량매도코드
            if eth > 0.002:
                upbit.sell_market_order("KRW-ETH", eth*0.9995)
                eb1=0
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #리플 자동매매 코드, 자산의 13프로, K=0.5
            target_price1 = get_target_price("KRW-XRP", 0.5)
            current_price1 = get_current_price("KRW-XRP")
            if target_price1 < current_price1<target_price1*1.01:
                krw = get_balance("KRW")
                if krw > 5000 and eb2==0:
                    eb2=1
                    upbit.buy_market_order("KRW-XRP", 300000)
            elif current_price < target_price*0.94 :
                xrp = get_balance("XRP")
                if xrp > 4:
                 upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                 eb2=0        
        else:
            xrp = get_balance("XRP")
            if xrp > 4:
                upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                eb2=0
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #비트토렌트 자동매매 코드, 자산의 13프로, K=0.5
            target_price2 = get_target_price("KRW-BTT", 0.5)
            current_price2 = get_current_price("KRW-BTT")
            if target_price2 < current_price2<target_price2*1.01:
                krw = get_balance("KRW")
                if krw > 5000 and eb3==0:
                    eb3=1
                    upbit.buy_market_order("KRW-BTT", 300000)
            elif current_price < target_price*0.94 :
                btt = get_balance("BTT")
                if btt > 1000:
                 upbit.sell_market_order("KRW-BTT", btt*0.9995)
                 eb3=0        
        else:
            btt = get_balance("BTT")
            if btt > 1000:
                upbit.sell_market_order("KRW-BTT", btt*0.9995)
                eb3=0
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #비체인 자동매매 코드, 자산의 13프로, K=0.5
            target_price3 = get_target_price("KRW-VET", 0.4)
            current_price3 = get_current_price("KRW-VET")
            if target_price3 < current_price3<target_price3*1.01:
                krw = get_balance("KRW")
                if krw > 5000 and eb4==0:
                    eb4=1
                    upbit.buy_market_order("KRW-VET", 300000)
            elif current_price < target_price*0.94 :
                vet = get_balance("VET")
                if vet > 30 :
                 upbit.sell_market_order("KRW-VET", vet*0.9995)
                 eb4=0        
        else:
            vet = get_balance("VET")
            if vet > 30:
                eb4=0
                upbit.sell_market_order("KRW-VET", vet*0.9995)
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #도지 자동매매 코드, 자산의 13프로, K=0.5
            target_price4 = get_target_price("KRW-DOGE", 0.5)
            current_price4 = get_current_price("KRW-DOGE")
            if target_price4 < current_price4<target_price4*1.03:
                krw = get_balance("KRW")
                if krw > 5000 and eb5==0:
                    eb5=1
                    upbit.buy_market_order("KRW-DOGE", 300000)
            elif current_price < target_price*0.94 :
                doge = get_balance("DOGE")
                if doge > 20:
                 upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                 eb5=0        
        else:
            doge = get_balance("DOGE")
            if doge > 20:
                eb5=0
                upbit.sell_market_order("KRW-DOGE", doge*0.9995)
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #이더리움 클래식 자동매매 코드, 자산의 13프로, K=0.5
            target_price5 = get_target_price("KRW-ETC", 0.6)
            current_price5 = get_current_price("KRW-ETC")
            if target_price5 < current_price5<target_price5*1.03:
                if krw > 5000 and eb6==0:
                    eb6=1
                    upbit.buy_market_order("KRW-ETC", 300000)
            elif current_price < target_price*0.94 :
                etc = get_balance("ETC")
                if etc > 0.2:
                 upbit.sell_market_order("KRW-ETC", etc*0.9995)
                 eb6=0
        else:
            etc = get_balance("ETC")
            if etc > 0.2:
                eb6=0
                upbit.sell_market_order("KRW-ETC", etc*0.9995)
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #비트코인골드 자동매매 코드, 자산의 13프로, K=0.5
            target_price6 = get_target_price("KRW-BTG", 0.5)
            current_price6 = get_current_price("KRW-BTG")
            if target_price6 < current_price6 < target_price6*1.03:
                krw = get_balance("KRW")
                if krw > 5000 and eb7==0:
                    eb7=1
                    upbit.buy_market_order("KRW-BTG", 300000)
            elif current_price < target_price*0.94 :
                btg = get_balance("BTG")
                if btg > 0.05:
                 upbit.sell_market_order("KRW-BTG", btg*0.9995)
                 eb7=0
        else:
            btg = get_balance("BTG")
            if btg > 0.05:
                eb7=0
                upbit.sell_market_order("KRW-BTG", btg*0.9995)
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #칠리즈 자동매매 코드, 자산의 13프로, K=0.5
            target_price7 = get_target_price("KRW-CHZ", 0.5)
            current_price7 = get_current_price("KRW-CHZ")
            if target_price7 < current_price7 < target_price7*1.03: 
                krw = get_balance("KRW")
                if krw > 5000 and eb8==0:
                    eb8=1
                    upbit.buy_market_order("KRW-CHZ", 300000)
            elif current_price < target_price*0.94 :
                chz = get_balance("CHZ")
                if chz > 10:
                 upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                 eb8=0
        else:
            chz = get_balance("CHZ")
            if chz > 10:
                eb8=0
                upbit.sell_market_order("KRW-CHZ", chz*0.9995)
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)