import pyupbit

access = "gVREOT8UCJ5mFreoXx8DXo3OLQFpxI7dNw2gZBid"          # 본인 값으로 변경
secret = "Jnf6RQa8MgxiRJskenB7xonB9xuayxqzuxXNbr5B"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회