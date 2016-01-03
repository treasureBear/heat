#Heat - My boiler room automation project

def ts_write(t_in,t_out,t_acc,t_room,t_outside,l_pellets,s_set):
    import urllib
    import urllib.request
    url = "https://api.thingspeak.com/update?api_key=0VLIR53FNSJ1KWWW"
    url = url+"&field1="+str(t_in)
    url = url+"&field2="+str(t_out)
    url = url+"&field3="+str(t_acc)
    url = url+"&field4="+str(t_room)
    url = url+"&field5="+str(t_outside)
    url = url+"&field6="+str(l_pellets)
    url = url+"&field7="+str(s_set)
    urllib.request.urlopen(url)

    msg = urllib.request.urlopen("https://api.thingspeak.com/channels/76296/feeds/last.json")
    return msg

t_target = ts_write(2,1.1,1.2,1.3,1.4,1.5,1.6)
print(t_target)
print(t_target.read())
