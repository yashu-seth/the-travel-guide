##maxprice aur passengers abhi dekh lena
import json
import requests
url='https://www.googleapis.com/qpxExpress/v1/trips/search?key='
headers={'Content-Type': 'application/json'}
apikey='************************'
url=url+apikey

####json request is of the form:
##{
##  "request": {
##    "passengers": {
##      "adultCount": "1"
##    },
##    "slice": [
##      {
##        "origin": "SFO",
##        "destination": "LAX",
##        "date": "2014-09-19"
##      }
##    ],
##    "solutions": "1"
##  }
##}

origin_code=raw_input("enter orig code")
desti_code=raw_input("enter dest code")
date=raw_input("input date in the format yyyy-mm-dd")
sol=raw_input("no. of air solutions required")
ad=int(raw_input("no of adults"))
cd=int(raw_input("no of children"))
sd=int(raw_input("no. of senior citizens"))
infl=int(raw_input("no. of infants in lap"))
infs=int(raw_input("no. of infants to be assigned a seat"))
#maxpr=raw_input("maximum price you can afford")
prelst=['COACH', 'PREMIUM_COACH', 'BUSINESS', 'FIRST']
print "available Cabins"
count=1
for ca in prelst:
    print count,
    print  "  "+ca
    count+=1
prc=int(raw_input("enter preffered cabin"))
obj={
  "request": {
    "passengers": {
      "adultCount": ad,
      "childCount": cd,
      "infantInLapCount": infl,
      "infantInSeatCount": infs,
      "seniorCount": sd,
    },
    "slice": [
      {
        "origin": origin_code,
        "destination": desti_code,
        "date": date,
        "preferedCabin":prelst[prc-1]
      }
    ],
    "solutions": sol,
    #"maxprice": "INR-"+maxpr,
  }
}

##request.maxprice vaale se max price tak ki airlines hi aayenge
json_request=json.dumps(obj)
for y in range(10):
    try:
        resp=requests.post(url, data=json_request, headers=headers)
        break
    except:
        continue
j=json.loads(resp.content)

print "airports involved"
for airport in j["trips"]["data"]["airport"]:
    print "##"
    print airport["code"]
    print airport["name"]
    ##print airport["city"]
print    
##print "ye city k baare me"
##for city in j["trips"]["data"]["city"]:
##    print "##"
##    print city["kind"]
##    print city["code"]
##    print city["country"]
##    print city["name"]
######    
####print "ye sab aircrafts available hai"
####print
####for aircraft in j["trips"]["data"]["aircraft"]:
####    print "##"
####    print aircraft["name"]
####
####print
####print "ye carriers k naam"
####print
####for carr in j["trips"]["data"]["carrier"]:
####    print "##"
####    print carr["name"]
####    print "code:"+ carr["code"]

    

for alltrips in j["trips"]["tripOption"]:
    for each in alltrips["slice"]:
        print "Duration of the trip"+ str(each["duration"])
        print "the segments that constitute the flight are"
        for seg in each["segment"]:
            print "##"
            print "Duration is "+ str(seg["duration"])
            print "The flight this is a segment of:"
            print "Carrier "+ str(seg["flight"]["carrier"])
            print "In Cabin: " +str(seg["cabin"])
            for leg in seg["leg"]:
                print "Aircraft:"+ str(leg["aircraft"])
                print "Arrival Time "+ str(leg["arrivalTime"])
                print "Departure Time " +str(leg["departureTime"])
                if leg.get("originTerminal"):
                    
                    print "origin Terminal"+ str(leg["originTerminal"])
                if leg.get("destinationTerminal"):
                    print "destination Terminal "+str(leg["destinationTerminal"])
                #print "the duration  of this leg is" + str(leg["duration"])
    for each in alltrips["pricing"]:
        print "the total base fare per passenger " + str(each["baseFareTotal"])
        print "total fare so calculated is"
        basefare=[int(  each["baseFareTotal"].split("R")[1])]
        #print basefare
        #assert False
        print "INR"+str((int(ad)+int(sd)+int(cd)+int(infs))*basefare[0])
        #assert False
        print "the horizontal fare Calculation \n"+str(each["fareCalculation"])
        print "**this is devoid of taxes**"
