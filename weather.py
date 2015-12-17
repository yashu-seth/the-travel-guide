import requests
import json
"""five day response abhi parse nhi kiya hai ...16 day vaala kiya hai...par ye jyaada dino k liye nhi dikhata
dekh lo ise ek baar"""
weathr_cond={
"200":	"thunderstorm with light rain",
"201": "thunderstorm with rain",
"202":	"thunderstorm with heavy rain",
"210":	"light thunderstorm",
"211":	"thunderstorm",
"212":	"heavy thunderstorm",
"221":	"ragged thunderstorm",
"230":	"thunderstorm with light drizzle",
"231":	"thunderstorm with drizzle",
"232":	"thunderstorm with heavy drizzle",##file:11d.png

"300":	"light intensity drizzle",	##[[file:09d.png]]
"301":	"drizzle",	
"302":	"heavy intensity drizzle",	
"310":	"light intensity drizzle rain",	
"311":	"drizzle rain",
"312":	"heavy intensity drizzle rain",	
"313":	"shower rain and drizzle",	
"314":	"heavy shower rain and drizzle",
"321":	"shower drizzle",

"500":	"light rain",	##[[file:10d.png]]
"501":	"moderate rain",	
"502":	"heavy intensity rain",	
"503":	"very heavy rain",	
"504":	"extreme rain",	
"511":	"freezing rain"	,
"520":	"light intensity shower rain",	
"521":	"shower rain",	
"522":	"heavy intensity shower rain",	
"531":	"ragged shower rain",	


"600":	"light snow",	##[[file:13d.png]]
"601":	"snow",	
"602":	"heavy snow",	
"611":	"sleet",	
"612":	"shower sleet",	
"615":	"light rain and snow",	
"616":	"rain and snow",	
"620":	"light shower snow",	
"621":	"shower snow",	
"622":	"heavy shower snow",

"701":	"mist",	##[[file:50d.png]]
"711":	"smoke",	
"721":	"haze",	
"731":	"sand, dust whirls",	
"741":	"fog",	
"751":	"sand",
"761":	"dust",	
"762":	"volcanic ash"	,
"771":	"squalls",	
"781":	"tornado",


"800":	"clear sky",	##[[file:01d.png]] [[file:01n.png]]
"801":	"few clouds",	##[[file:02d.png]] [[file:02n.png]]
"802":	"scattered clouds",	##[[file:03d.png]] [[file:03d.png]]
"803":	"broken clouds",	##[[file:04d.png]] [[file:03d.png]]
"804":	"overcast clouds",##[[file:04d.png]] [[file:04d.png]]


"900":	"tornado",
"901":	"tropical storm",
"902":	"hurricane",
"903":	"cold",
"904":	"hot",
"905":	"windy",
"906":	"hail",


"951":	"calm",
"952":	"light breeze",
"953":	"gentle breeze",
"954":	"moderate breeze",
"955":  "fresh breeze",
"956":	"strong breeze",
"957":  "high wind, near gale",
"958":	"gale",
"959":	"severe gale",
"960":	"storm",
"961":	"violent storm",
"962":	"hurricane",}

import time
print "Enter the name of the city"
print "Put the first letter in caps"
city=raw_input()
print "enter whether you want a  daily forcast...press 1 for this "
#print "enter 2 for 5 day/3 hour forecast"
choice=int(raw_input())
url5='http://api.openweathermap.org/data/2.5/forecast?q='+city
url16='http://api.openweathermap.org/data/2.5/forecast/daily?q='+city+'&units=metric&cnt=7'
if choice==1:
    response=requests.get(url16)
    json_text=json.loads(response.content)
    #print json_text
    print
    for list_elem in json_text['list']:
        unix_time= list_elem['dt']#epoch
        print '##'
        print "Date: "
        print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(unix_time))##use time.gmtime for gmt time
        #print json_text['list'][0]['pressure']
        #print
        print "Cloudiness :" + str(list_elem['clouds'])+"%"
        for we in list_elem['weather']:
            print "Weather Conditions: "+we['description']
        if 'rain' in list_elem:
            print "Precipitation Volume for last 3 hours:"+str(list_elem['rain'])+'mm'
        if 'snow' in list_elem:
            print "Snow Volume in last 3 hours:"+str(list_elem['snow'])+'mm'
        if 'wind' in list_elem:
            print "Wind Speed" +str(list_elem['wind']['speed'])
        print "Temperature"
        print "Day Temperature :"+str(list_elem["temp"]["day"])+" degree centigrade"#-273.15)
        print "Minimum Temperature :"+str(list_elem["temp"]["min"])+" degree centigrade"#-273.15)
        print "Maximum Temperature :"+str(list_elem["temp"]["max"])+" degree centigrade"#-273.15)
elif choice==2:
    response=requests.get(url5)
    print response.content
else:
    print "bad request"
#print json.dumps(response.content, indent=1)
#print response.content
print
print
print("HASHTAG wont give it back")


