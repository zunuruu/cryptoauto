import pyupbit
import numpy as np

#원화시장 7일동안 시가/고가/저가/종가/거래량
df = pyupbit.get_ohlcv("KRW-CRO", count=90)
#변동폭*k 계산, (고가-저가)*k값
df['range'] = (df['high'] - df['low']) * 0.7

#target(매수가),range 컬럼을 한칸씩 밑으로 내림(.shift)//레인지는 전날 이기 때문에
df['target'] = df['open'] + df['range'].shift(1)

fee=0.0005

#ror(수익률), np.where(조건문, 참일때값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

# 누적 곱 계산 (crumprod) -> 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down(하락폭) 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 최대하락폭 계산 (드로우 다운중에 맥스값)
print("MDD(%): ", df['dd'].max())
#엑셀로 출력
df.to_excel("dd.xlsx")