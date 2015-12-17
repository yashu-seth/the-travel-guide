
## prc ke input ka dhyan rakhna
import json
import requests
###############(string,string,string,string, int, int, int, int, int , int, string)
## date ka format 2015-09-29
## sol-- no of airfare soln hai ## sabh k type ka dhyan rakhna
## baki ad-adults
## cd- children
## sd-senior citizens
## infl-infants who dont require a seat
## infs-infants who require a seat
## prc  preferred cabin hai
##'COACH', 'PREMIUM_COACH', 'BUSINESS', 'FIRST'
## inme se bhar dena
## matlab jaise 'coach' k liye 1
## maxpr string hai to  jaise '7000' pass krna
def findflight(origin_code, desti_code, date, sol='10', ad=1, cd=0, sd=0, infl=0, infs=0, prc=1, maxpr='12000'): 
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
    prelst=['COACH', 'PREMIUM_COACH', 'BUSINESS', 'FIRST']
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
        "maxprice": "INR-"+maxpr
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
    response=[]##response is the final list we're going to return
    res_lst=[]

##    res_lst.append( "airports involved")
##    for airport in j["trips"]["data"]["airport"]:
##        res_lst.append("##")
##        res_lst.append( airport["code"])
##        res_lst.append( airport["name"])
##    response.append("\n".join(res_lst))
        ##print airport["city"]
##    print    
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

        
    print(j)
    for alltrips in j["trips"]["tripOption"]:
        print(alltrips)
        res_lst=[]
        for each in alltrips["slice"]:
            res_lst.append(str(each["duration"]))
##            res_lst.append( "The segments that constitute the flight are ")
##            for seg in each["segment"]:
##                res_lst.append( "##")
##                res_lst.append( "Duration is "+ str(seg["duration"]))
##                res_lst.append( "The flight this is a segment of:")
##                res_lst.append( "Carrier "+ str(seg["flight"]["carrier"]))
##                res_lst.append( "In Cabin: " +str(seg["cabin"]))
##                for leg in seg["leg"]:
##                    res_lst.append( "Aircraft:"+ str(leg["aircraft"]))
##                    res_lst.append( "Arrival Time "+ str(leg["arrivalTime"]))
##                    res_lst.append( "Departure Time " +str(leg["departureTime"]))
##                    if leg.get("originTerminal"):
##                        
##                        res_lst.append( "origin Terminal"+ str(leg["originTerminal"]))
##                    if leg.get("destinationTerminal"):
##                        res_lst.append( "destination Terminal "+str(leg["destinationTerminal"]))
                    #print "the duration  of this leg is" + str(leg["duration"])
        for each in alltrips["pricing"]:
##            res_lst.append("the total base fare per passenger " + str(each["baseFareTotal"]))
##            res_lst.append( "The total fare so calculated is")
            basefare=[int(  each["baseFareTotal"].split("R")[1])]
            #print basefare
            #assert False
            res_lst.append(str((int(ad)+int(sd)+int(cd)+int(infs))*basefare[0]))
            #assert False
##            res_lst.append( "the horizontal fare Calculation \n"+str(each["fareCalculation"]))
##            res_lst.append( "**this is devoid of taxes**")
##        res_string="\n".join(res_lst)
        response.append(res_lst)
    return response
