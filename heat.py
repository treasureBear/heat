#Heat - My boiler room automation project

def ts_write():
    import urllib
    import urllib.request
    urllib.request.urlopen("https://api.thingspeak.com/update?api_key=0VLIR53FNSJ1KWWW&field1=100")

ts_write()
