import requests
import json
from hotels_and_sight_seeing import *

def find_driving_distance(origin_place, destination_place):
##    print(origin_place, destination_place)
    
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
    try:
        for elem in j_res["rows"]:
            for each in elem["elements"]:
    ##            result.append(each["distance"]["text"])
    ##            result.append(each["duration"]["text"])
                tmp=each["duration"]["text"].split()
                if len(tmp)==2:
                    time=float(tmp[0])/60
                elif len(tmp)==4:
                    time=float(tmp[0])+(float(tmp[2])/60)
                else:
                    time=2
                
        return time
    except: return 1.3
        
###################################################


def get_prox_factor(travel_time):
    if travel_time<=0.5:
        prox_factor=0.85
    elif travel_time<=1:
        prox_factor=0.65
    elif travel_time<=1.5:
        prox_factor=0.5
    elif travel_time<=2:
        prox_factor=0.2
    elif travel_time<=2.5:
        prox_factor=0.1
    else:
        prox_factor=0
##    print('travel time',travel_time)
##    print(prox_factor)
    return prox_factor


###################################################



def recommend_package(ss_list,time):
##    city_points=(40-(2*(city_rank-1)))
    visited={}
    day_plans=[]
    dis=[]
    time_limit=7.5

    pk=[]
    pk_points=0
    pk_time=0
    while(len(visited)!=len(ss_list)):
        fun=1
        for x in ss_list:
            if x not in visited:
                
                ss_name=ss_list[x][0]
                ss_rank=x
                ss_points=(400-((ss_rank-1)*(ss_rank-1)))
                if ss_rank==1:
                    ss_points+=800
                
                if len(pk)==0:
                    pk.append(ss_name)
                    visited[ss_rank]=ss_name
                    ss_time=time[ss_rank-1]
                    base=ss_name
                    pk_points+=ss_points
                    pk_time+=ss_time
                    
                else:    
                    ss_time=time[ss_rank-1] 
                    travel_time=find_driving_distance(base,ss_name)*(1.2)
                    tot_time=ss_time+travel_time
                    
                    prox_factor=get_prox_factor(travel_time)

                    if pk_time+tot_time>time_limit:
                        continue
                    else:
                        pk.append(ss_name)
                        visited[ss_rank]=ss_name
                        pk_time+=tot_time
                        pk_points+=ss_points
                        tmp=0
                        for x in visited:
                            tmp+=(40-(2*(x-1)))
                        pk_points+=tmp*prox_factor
            
##        pk_points+=city_points
        tmp=[pk,pk_time,pk_points]
        day_plans.append(tmp)
        pk=[]
        pk_points=0
        pk_time=0



    return(day_plans)

###############################################


state=raw_input('Enter the name of state - ')
city=raw_input('Enter city - ')
t1=get_sightseeing_list(state,city)
t2=get_ss_time(state,city)
print(t2)
##t2=[1.5, 4.25, 0.7, 1.5, 0.7, 0.7, 1.5, 1.5, 1.5, 1.5, 0.7, 1.5, 4.25, 0.7, 1.5, 1.5, 1.5, 1.5, 4.25, 1.5]
t3=recommend_package(t1,t2)
tot_days=len(t3)
planned_days=[]
for i in range(tot_days):
    planned_days.append([])
points=[]
for x in t3:
    points.append(x[-1])
##print(points)
points.sort()
##print(points)
for i in range (len(points)):
    for y in t3:
        if y[-1]==points[i]:
            planned_days[tot_days-i-1]=y[0]
            
##print(planned_days)

for i in range(len( planned_days )):
    print('## Day-'+str(i+1))
    for x in planned_days[i]:
        print('--'+x)
    print
    
    
