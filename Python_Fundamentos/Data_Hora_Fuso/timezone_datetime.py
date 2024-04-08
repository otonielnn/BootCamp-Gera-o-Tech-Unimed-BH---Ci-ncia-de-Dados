from datetime import datetime, timezone, timedelta

data_london = datetime.now(timezone(timedelta(hours=1)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_london)
print(data_sao_paulo)
