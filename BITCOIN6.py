import time
import pyupbit
import datetime
#매도코드 삭제, elif문 수정 10프로 손절, 자동매수만 해놓고 내 판단으로 팔기, 원칙은 아침9시전팔기.
eb1=0
eb2=0
eb3=0
eb4=0
eb5=0
eb6=0
eb7=0
eb8=0
eb9=0


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
            if target_price < current_price < target_price*1.03 :
                krw = get_balance("KRW")
                if krw > 300000 and eb1==0:
                    eb1=1 #구매 확인코드
                    upbit.buy_market_order("KRW-ETH", 500000) #30만원 매수 코드
            elif current_price < target_price*0.90 and eb1==1 : #-10프로 손절라인 만들기 코드
                eth = get_balance("ETH")
                upbit.sell_market_order("KRW-ETH", eth*1)
        else:
            eb1=0
                
        time.sleep(0.1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #리플 자동매매 코드, 자산의 13프로, K=0.5
            target_price1 = get_target_price("KRW-XRP", 0.5)
            current_price1 = get_current_price("KRW-XRP")
            if target_price1 < current_price1<target_price1*1.03:
                krw = get_balance("KRW")
                if krw > 300000 and eb2==0:
                    eb2=1
                    upbit.buy_market_order("KRW-XRP", 500000)
            elif current_price < target_price*0.90 and eb2==1 :
                xrp = get_balance("XRP")
                upbit.sell_market_order("KRW-XRP", xrp*1)    
        else:
            eb2=0
                
        time.sleep(0.1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #비트토렌트 자동매매 코드, 자산의 13프로, K=0.5
            target_price2 = get_target_price("KRW-BTT", 0.5)
            current_price2 = get_current_price("KRW-BTT")
            if target_price2 < current_price2<target_price2*1.03:
                krw = get_balance("KRW")
                if krw > 300000 and eb3==0:
                    eb3=1
                    upbit.buy_market_order("KRW-BTT", 500000)
            elif current_price < target_price*0.90 and eb2==1 :
                btt = get_balance("BTT")
                upbit.sell_market_order("KRW-BTT", btt*1)
                eb3=1        
        else:
            eb3=0

        time.sleep(0.1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #비체인 자동매매 코드, 자산의 13프로, K=0.5
            target_price3 = get_target_price("KRW-VET", 0.4)
            current_price3 = get_current_price("KRW-VET")
            if target_price3 < current_price3<target_price3*1.03:
                krw = get_balance("KRW")
                if krw > 300000 and eb4==0:
                    eb4=1
                    upbit.buy_market_order("KRW-VET", 500000)
            elif current_price < target_price*0.90 and eb4==1 :
                vet = get_balance("VET")
                upbit.sell_market_order("KRW-VET", vet*1)
                eb4=1
        else:
            eb4=0
            
        time.sleep(0.1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #도지 자동매매 코드, 자산의 13프로, K=0.5
            target_price4 = get_target_price("KRW-DOGE", 0.5)
            current_price4 = get_current_price("KRW-DOGE")
            if target_price4 < current_price4<target_price4*1.03:
                krw = get_balance("KRW")
                if krw > 300000 and eb5==0:
                    eb5=1
                    upbit.buy_market_order("KRW-DOGE", 500000)
            elif current_price < target_price*0.90 and eb5==1 :
                doge = get_balance("DOGE")
                upbit.sell_market_order("KRW-DOGE", doge*1)
                eb5=1
        else:
            eb5=0
        
        time.sleep(0.1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=60): #이더리움 클래식 자동매매 코드, 자산의 13프로, K=0.5
            target_price5 = get_target_price("KRW-ETC", 0.6)
            current_price5 = get_current_price("KRW-ETC")
            if target_price5 < current_price5<target_price5*1.03:
                if krw > 300000 and eb6==0:
                    eb6=1
                    upbit.buy_market_order("KRW-ETC", 500000)
            elif current_price < target_price*0.90 and eb6==0 :
                etc = get_balance("ETC")
                upbit.sell_market_order("KRW-ETC", etc*1)
                eb6=1
        else:
            eb6=0
        
        time.sleep(0.1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #비트코인골드 자동매매 코드, 자산의 13프로, K=0.5
            target_price6 = get_target_price("KRW-BTG", 0.5)
            current_price6 = get_current_price("KRW-BTG")
            if target_price6 < current_price6 < target_price6*1.03:
                krw = get_balance("KRW")
                if krw > 300000 and eb7==0:
                    eb7=1
                    upbit.buy_market_order("KRW-BTG", 500000)
            elif current_price < target_price*0.90 and eb7==1 :
                btg = get_balance("BTG")
                upbit.sell_market_order("KRW-BTG", btg*1)
                eb7=1
        else:
            eb7=0
            
        time.sleep(0.1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #칠리즈 자동매매 코드, 자산의 13프로, K=0.5
            target_price7 = get_target_price("KRW-CHZ", 0.5)
            current_price7 = get_current_price("KRW-CHZ")
            if target_price7 < current_price7 < target_price7*1.03: 
                krw = get_balance("KRW")
                if krw > 300000 and eb8==0:
                    eb8=1
                    upbit.buy_market_order("KRW-CHZ", 500000)
            elif current_price < target_price*0.90 and eb8==1 :
                chz = get_balance("CHZ")
                upbit.sell_market_order("KRW-CHZ", chz*1)
                eb8=1
        else:
            eb8=0
            
        time.sleep(0.1)

        if start_time < now < end_time - datetime.timedelta(seconds=60): #메디블록 자동매매 코드, 자산의 13프로, K=0.5
            target_price8 = get_target_price("KRW-MED", 0.9)
            current_price8 = get_current_price("KRW-MED")
            if target_price8 < current_price8 < target_price8*1.03: 
                krw = get_balance("KRW")
                if krw > 300000 and eb9==0:
                    eb9=1
                    upbit.buy_market_order("KRW-MED", 500000)
            elif current_price < target_price*0.90 and eb9==1:
                med = get_balance("MED")
                if med > 30:
                 upbit.sell_market_order("KRW-MED", med*1)
                 eb9=1
        else:
            eb9=0
            
        time.sleep(0.1)

    except Exception as e:
        print(e)
        time.sleep(0.1)