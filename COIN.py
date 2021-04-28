import time
import pyupbit
import datetime

access = "your-access"
secret = "your-secret"

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
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10): #리플 자동매매 코드, 자산의 13프로, K=0.5
            target_price1 = get_target_price("KRW-XRP", 0.5)
            current_price1 = get_current_price("KRW-XRP")
            if target_price1 < current_price1:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.13)
        else:
            xrp = get_balance("XRP")
            if xrp > 4:
                upbit.sell_market_order("KRW-XRP", xrp*0.9995)
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=10): #비트토렌트 자동매매 코드, 자산의 13프로, K=0.5
            target_price2 = get_target_price("KRW-BTT", 0.5)
            current_price2 = get_current_price("KRW-BTT")
            if target_price2 < current_price2:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTT", krw*0.13)
        else:
            btt = get_balance("BTT")
            if btt > 1000:
                upbit.sell_market_order("KRW-BTT", xrp*0.9995)
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=10): #비체인 자동매매 코드, 자산의 13프로, K=0.5
            target_price3 = get_target_price("KRW-VET", 0.4)
            current_price3 = get_current_price("KRW-VET")
            if target_price3 < current_price3:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-VET", krw*0.13)
        else:
            vet = get_balance("VET")
            if vet > 30:
                upbit.sell_market_order("KRW-VET", xrp*0.9995)
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=10): #도지 자동매매 코드, 자산의 13프로, K=0.5
            target_price4 = get_target_price("KRW-DOGE", 0.5)
            current_price4 = get_current_price("KRW-DOGE")
            if target_price4 < current_price4:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.13)
        else:
            doge = get_balance("DOGE")
            if doge > 20:
                upbit.sell_market_order("KRW-DOGE", doge*0.9995)
        time.sleep(1)
        
        if start_time < now < end_time - datetime.timedelta(seconds=10): #이더리움 클래식 자동매매 코드, 자산의 13프로, K=0.5
            target_price5 = get_target_price("KRW-ETC", 0.6)
            current_price5 = get_current_price("KRW-ETC")
            if target_price5 < current_price5:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETC", krw*0.13)
        else:
            etc = get_balance("ETC")
            if etc > 0.2:
                upbit.sell_market_order("KRW-ETC", doge*0.9995)
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=10): #비트코인골드 자동매매 코드, 자산의 13프로, K=0.5
            target_price5 = get_target_price("KRW-BTG", 0.5)
            current_price5 = get_current_price("KRW-BTG")
            if target_price5 < current_price5:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTG", krw*0.13)
        else:
            btg = get_balance("BTG")
            if btg > 0.05:
                upbit.sell_market_order("KRW-BTG", btg*0.9995)
        time.sleep(1)

        if start_time < now < end_time - datetime.timedelta(seconds=10): #칠리즈 자동매매 코드, 자산의 13프로, K=0.5
            target_price6 = get_target_price("KRW-CHZ", 0.5)
            current_price6 = get_current_price("KRW-CHZ")
            if target_price6 < current_price6:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-CHZ", krw*0.13)
        else:
            chz = get_balance("CHZ")
            if chz > 10:
                upbit.sell_market_order("KRW-CHZ", btg*0.9995)
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)