from WindPy import *
w.start()
w.isconnected()
data=w.wsd("600036.SH","close","2019-05-01")#取招商银行收盘价等信息
print(data)