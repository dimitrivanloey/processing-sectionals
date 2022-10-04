from datetime import datetime

print(datetime.utcnow())
print(datetime.now())

if datetime.now() == datetime.utcnow():
  print('Winter time')
else:
  print('Summer time')