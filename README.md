# testCrytoSwitch
-ดาวน์โหลด Python3: https://www.python.org/downloads
-ใน File config.config: True = ชุด False = ไม่ขุด

       [MineCoins]
       mineRVN = True
       mineETH = True
       mineETC = True
       
-กำหนด File.bat ว่าอยู่ที่ไหน

       [Scripts]
       RVNscript = C:\Users\Administrator\Documents\RVN.bat
       ETHscript = ETH.bat
       ETCscript = ETC.bat
       
-กำหนดช่วงของค่า diff High/Low

       [tarDiff_High]
       tarDiffRVN = 40000
       tarDiffETH = 3522206773042161
       tarDiffETC = 206456480047318


       [tarDiff_Low]
       tarDiffRVN  = 8000
       tarDiffETH  = 2000000000000000
       tarDiffETC  = 100000000000000

-กำหนด priority: 1 = สำคัญสุด

       [prority]
       priRVN = 1
       priETH = 2
       priETC = 3
       
-กำหนด loop time

       [looptime]
       timescan = 1800
###1800 sec = 30 min

-เปิด python
>Start->Python 3.6 ->IDLE(Python 3.6 64 bit)
>เมนู File->Open->CryptoSwitc.py
>เมนู Run->Run Module


