import json, os, datetime, copy

ACCOUNTS = 'accounts'
USERNAME = 'username'
PASSWORD = 'password'
LASTLOGIN = 'lastlogin'
FAVORITES = 'favorites'
accountDataPath = '/accountData.json'

def getAccountData():
    if (os.path.isfile(accountDataPath)):
        with open(accountDataPath) as json_file:
            return json.load(json_file)
    accounts = {}
    accounts[ACCOUNTS] = []
    return accounts

def saveAccountData(accounts):
    with open(accountDataPath, 'w') as outfile:
        json.dump(accounts, outfile)

def addNewUser(username, password):
    accounts = getAccountData()

    for a in accounts[ACCOUNTS]:
        if (a[USERNAME] == username):
            return None

    user = {
        USERNAME : username,
        PASSWORD : password,
        LASTLOGIN : datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        FAVORITES : []
    }
    accounts[ACCOUNTS].append(user)

    saveAccountData(accounts)
    return user

def getUser(username, password):
    accounts = getAccountData()

    if (accounts != None):
        for a in accounts[ACCOUNTS]:
            if (a[USERNAME] == username and a[PASSWORD] == password):
                user = copy.deepcopy(a)
                a[LASTLOGIN] = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                saveAccountData(accounts)
                return user
    return None

def addNewFavorite(username, favorite):
    accounts = getAccountData()

    if (accounts != None):
        for a in accounts[ACCOUNTS]:
            if (a[USERNAME] == username):
                if (favorite not in a[FAVORITES]):
                    a[FAVORITES].append(favorite)
                    saveAccountData(accounts)

def getFavorites(username):
    accounts = getAccountData()

    if (accounts != None):
        for a in accounts[ACCOUNTS]:
            if (a[USERNAME] == username):
                return a[FAVORITES]
    return []
