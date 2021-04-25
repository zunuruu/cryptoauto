import time
import pyupbit
import datetime

access = "lAVWp8Rz7bUxzDHFEx8uf6xcVpzVaCfk61XM4add"
secret = "81laTOHDS4raawc0JTax98HcY5Vm3x5cUhncyAdw"

#이더리움 k=0,7, 3일이동평균선 이상일때 매수
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
                
def get_ma3(ticker):
    """3일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=3) #애매함
    ma3 = df['close'].rolling(3).mean().iloc[-1]
    return ma3

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
        start_time = get_start_time("KRW-ETH") #9시
        end_time = start_time + datetime.timedelta(days=1) #9시 +1일
        
        #9시에서 8시59분50초사이이면 시작
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETH", 0.7) #이더리움,k=0.7
            ma3 = get_ma3("KRW-ETH")
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price and ma3 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)
        else:
            eth = get_balance("ETH")
            if eth > 0.002:
                upbit.sell_market_order("KRW-ETH", eth*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)