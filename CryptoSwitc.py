import os
import time
import configparser
import random

import urllib.request
import json

import datetime

class Coin:
    def __init__(self, name):
        self.willingToMine = False
        self.command = ''  # the command that is run when we want to mine this coin.
        self.tarDiff_High = 9999999
        self.tarDiff_Low = 9999999
        self.priority = 9999999
        self.urlGetDiffCoin = ' '
        self.miningNow = False
        self.name = name
        self.difficulty = 9999999
        self.statusFile = "CloseFile"


coins = {}  #value for setting of coin
buffPri = [] #keep for find min priority
sortPri = ()    #convert list to tuple
minPri = 0  #mininum prioryty
lastCoin = " "
lastClose = " "
countRun = 0
lastminPri = 0
lasCoinAgain = 0
#timescan = 1

opener = urllib.request.build_opener()



def openFile(Filename):
    try:
        os.startfile(Filename)
    except ValueError:
        print("Error")

def closeFile():
    try:
        os.system('TASKKILL /F /IM cmd.exe')
    except ValueError:
        print("Error")

def getDifficulty(coin):

    #diff = random.randint(1000,70000)
    #coins[coin].difficulty = diff

    #coins[coin].difficulty = 55000

    #if coin == "rvn":
    #    diff = 1000
    #    coins[coin].difficulty  = diff

    #if coin == "eth":
    #    diff = 1000
    #    coins[coin].difficulty  = diff

    #if coin == "era":
    #   diff = 1000
    #   coins[coin].difficulty  = diff

    #global countRun
    #if countRun < 10:
    #   countRun = countRun + 1
    #    coins[coin].difficulty = 1000
    #if countRun >= 10:
    #    coins[coin].difficulty = 9999999
    #    countRun = countRun + 1
    #    if countRun > 20:
    #        countRun = 0

    #print (coin,"diff: ",coins[coin].difficulty," coutn: ",countRun)
    return

def getDiffApiRVN():
    key = 'rvn'
    urlRvnApi = 'http://rvnhodl.com/api/getdifficulty'
    req = urllib.request.Request(urlRvnApi)
    opener = urllib.request.build_opener()
    f = opener.open(req, timeout=5)
    diffRVN = json.load(f)
    coins[key].difficulty = diffRVN
    #print(diffRVN)

def getDiffApiETH():
    key = 'eth'
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open('https://api.ethermine.org/networkStats')
    apiDiff = json.load(response)
    rawdiff = apiDiff['data']
    diffETH = rawdiff['difficulty']
    coins[key].difficulty = diffETH
    #print(diffETH)

def getDiffApiETC():
    key = 'etc'
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open('https://api-etc.ethermine.org/networkStats')
    apiDiff = json.load(response)
    rawdiff = apiDiff['data']
    diffETC = rawdiff['difficulty']
    coins[key].difficulty = diffETC
    #print(diffETC)

def job():
   # tasks of the script
   print("I'm working...")

coins['rvn'] =  Coin('Ravencoin')
coins['eth'] =  Coin('Ethereum')
coins['etc'] =  Coin('Ethermine')


# Read in config file
Config = configparser.ConfigParser()
Config.read('./config.config')

# Enable the coins you want to mine here.
for key in coins:
    try:
        coins[key].willingToMine = Config.getboolean('MineCoins','mine'+key)
    except:
        continue

# Scripts
for key in coins:
    try:
        coins[key].command = Config.get('Scripts',key+'script')
    except:
        continue

#tarDiff
for key in coins:
    try:
        coins[key].tarDiff_High = Config.get('tarDiff_High','tarDiff'+key)
        #print(coins[key].tarDiff_High)
    except:
        continue

for key in coins:
    try:
        coins[key].tarDiff_Low = Config.get('tarDiff_Low','tarDiff'+key)
        #print(coins[key].tarDiff_Low)
    except:
        continue

#priority
for key in coins:
    try:
        coins[key].priority = Config.get('priority','pri'+key)
    except:
        continue

#timescan
timescan = 1
try:
    timescan = Config.get('looptime','timescan')
except:
    print("Error")

#get Diff Api All Coin
getDiffApiRVN()
getDiffApiETH()
getDiffApiETC()

while True:
    #job()
    #for key in coins:
        #getDifficulty(key)

    for key in coins:
        #print(coins[key].name,"Difficulty :",coins[key].difficulty)
        if coins[key].willingToMine == True:
            if coins[key].difficulty >= int(coins[key].tarDiff_Low) and coins[key].difficulty <= int(coins[key].tarDiff_High):
                coins[key].miningNow = True
                buffPri.append(coins[key].priority)

    if len(buffPri) > 0:
        sortPri = tuple(buffPri)
        minPri = min(sortPri)
        lastminPri = minPri
    else:
        if lastClose != " ":
            if lastClose != "CloseFile":
                closeFile()
                lastClose = "CloseFile"
                for key in coins:
                    if coins[key].priority == lastminPri:
                        coins[key].statusFile = "CloseFile"



    for key in coins:
        if coins[key].priority == minPri:
            if coins[key].name != lastCoin or lasCoinAgain > 0:
                if coins[key].statusFile != "OpenFile":
                    try:
                        closeFile()
                        openFile(coins[key].command)
                        coins[key].statusFile = "OpenFile"
                        lastCoin = coins[key].name
                        lastClose = "OpenFile"
                        lasCoinAgain = lasCoinAgain +1
                        if lasCoinAgain >= 5:
                            lasCoinAgain = 5
                    except:
                        print("Error")

    buffPri = []
    sortPri = ()
    minPri = 0

    for key in coins:
        try:
            print(str(key)+" Diff : "+str(coins[key].difficulty))
        except:
            continue
    tmin = int(timescan)/60
    print("time scan : "+str(timescan)+" sec = "+str(tmin)+" min ")

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    time.sleep(int(timescan))