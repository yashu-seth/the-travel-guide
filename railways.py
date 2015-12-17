import requests
import json

API_KEY='***********************'
url='http://api.erail.in/stations/?key='

"""Get Station Codes"""

url1=url+API_KEY
response1=requests.get(url1)
json_station_list=json.loads(response1.content)



def get_station_code(st_name,json_station_list):
    qry_codes=[]
    i_d=1
    for x in json_station_list:
        if st_name in x['name']:
            tmp=[]
            tmp.append(i_d)
            tmp.append(x['code'])
            tmp.append(x['name'])
            qry_codes.append(tmp)
            i_d+=1
    return qry_codes

def display_st_options_and_result(station_codes):
    print('Enter you desired station serial no.')
    for x in station_codes:
        print
        print(str(x[0])+')')
        print(x[2])
    choice=int(raw_input())
    for x in station_codes:
        if choice==x[0]:
            return x[1]

print('Enter your home city (first letter in caps)')
source_station=raw_input()
source_station_codes=get_station_code(source_station,json_station_list)
##print(source_station_codes)
source_st_code=(display_st_options_and_result(source_station_codes))
print
print('Enter your destination city (first letter in caps)')
dest_station=raw_input()
dest_station_codes=get_station_code(dest_station,json_station_list)
##print(source_station_codes)
dest_st_code=(display_st_options_and_result(dest_station_codes))

"""Get trains between stations"""

print('Enter the date of travel(in the following eg. format- "5-sep-2015")')
date=raw_input()
date='&date='+date
class_='&class=3A'
source_st_query='&stnfrom='+source_st_code
dest_st_query='&stnto='+dest_st_code
url2='http://api.erail.in/trains/?key='+API_KEY+source_st_query+dest_st_query+date+class_

sample_url='http://api.erail.in/trains/?key='+API_KEY
sample_url+='&stnfrom=PNBE&stnto=BSB&date=25-mar-2015&class=3A'
sample_date='25-MAR-2015'

def get_trains_bw_stations(json_trains):
    trains_list=[]
    id_=1
    n=int(raw_input("set the limit for number of trains"))
    for x in json_trains['result'][:n]:
        tmp=[]
        tmp.append(id_)
        id_+=1
        tmp.append('Train Name- '+x['name'])
        tmp.append('Train No.- '+x['trainno'])
        tmp.append('Destination Arrival Time- '+x['arr'])
        tmp.append('Source Departure Time- '+x['dep'])
        tmp.append('Travel Time- '+x['traveltime'])
        tmp.append('Running Days- '+x['rundays'])
        tmp.append('Classes Available- '+x['cls'])
        tmp.append('Train Type- '+x['type'])
        tmp.append('source- '+x['from'])
        tmp.append('destination- '+x['to'])
        trains_list.append(tmp)
    return trains_list

def get_fare(train_no,source_code,dest_code,date,API_KEY,quota='GN',age='AD'):
    url='http://api.erail.in/fare/?key='+API_KEY
    url+='&trainno='+train_no
    url+='&stnfrom='+source_code+'&stnto='+dest_code
    url+='&age=AD&quota=GN&date='+date
    url2='http://api.erail.in/fare/?key='+API_KEY+'&trainno=12138&stnfrom=NDLS&stnto=CSTM&age=AD&quota=GN&date=25-MAR-2015'
    response=requests.get(url)
    json_fare=json.loads(response.content)
    print
    print(json_fare)

def get_availability(train_no,source_code,dest_code,date,API_KEY,quota='GN'):
        print('Enter Class(SL|3A|2A|1A)')
        class_=raw_input()
        url='http://api.erail.in/seats/?key='+API_KEY
        url+='&trainno='+train_no
        url+='&stnfrom='+source_code+'&stnto='+dest_code
        url+='&quota=GN'+'&class='+class_+'&date='+date
        sample_url='http://api.erail.in/seats/?key='+API_KEY+'&trainno=12138&stnfrom=NDLS&stnto=CSTM&quota=GN&class=SL&date=25-MAR-2015'
        response=requests.get(url)
        json_availability=json.loads(response.content)
##        for x in json_availability:
##            print(x)
        print(json_availability)
    
    
def display_trains_and_get_details(trains_list,date,API_KEY):
    for x in trains_list:
        for y in x:
            print(y)
        print
    print("enter the chioce of your train")
    choice=int(raw_input())
    for x in trains_list:
        if x[0]==choice:
            train_no=x[2].split()[-1]
            source_code=x[9].split()[-1]
            dest_code=x[10].split()[-1]
            break
##    print('Enter fare to get fare')
##    choice=raw_input()
##    if choice=='fare':
##        print(get_fare(train_no,source_code,dest_code,date,API_KEY))
    print('Enter 1 to get seat availability')
    choice=raw_input()
    if choice=='1':
        print(get_availability(train_no,source_code,dest_code,date,API_KEY))
        
response2=requests.get(url2)
json_trains=json.loads(response2.content)
print(json_trains['status'])

list_=get_trains_bw_stations(json_trains)
display_trains_and_get_details(list_,date,API_KEY)

 
        
##print(get_fare('12488', 'BSB', 'NDLS', API_KEY,quota='GN',age='AD'))

        


    
