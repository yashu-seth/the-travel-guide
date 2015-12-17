import requests
import json
## iski origin aur destination me ensure kr lena ki
##jyaada spaces na ho aur comma k baad hi space ho
def finddrivingdistance():
    
    print "enter origin"

    origin_place=raw_input()

    print "enter destination"
    destination_place=raw_input()
    yo=[]#contains origin,destination in sendable format
    for place in [origin_place, destination_place]:
        new_place=place.replace(',','')#removing commas
        newer=new_place.replace(' ','+')#replacing spaces with plus
        yo.append(newer)

        
    url='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+yo[0]+'&destinations='+yo[1]+'&key=AIzaSyB0Z5xwCsHNYnkA1YSYFePn_qNOQ-R27MM'

    for y in range(10):
        try:
            response=requests.get(url)
            break
        except:
            continue
    j_res= json.loads(response.content)
    result=[]
    for elem in j_res["rows"]:
        for each in elem["elements"]:
            print "Distance is "+ each["distance"]["text"]
            print "Duration of Driving "+each["duration"]["text"]
            result.append(each["distance"]["text"])
            result.append(each["duration"]["text"])
            
    
    
    return  result
        
