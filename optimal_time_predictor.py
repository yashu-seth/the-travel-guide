from flight_func_to_optimize import *
from weatherscrape import *

def get_flight_fare_average(orig_code,dest_code,st_date):

    sol=50
    ad=1
    cd=0
    sd=0
    infl=0
    infs=0
    prc=1
    maxpr='12000'

##    st_date format yyyy-mm-dd
    
    date_avg={}
    date_=st_date.split('-')
    date=st_date
    
    for i in range(15):
        
        response=findflight(orig_code, dest_code, date)
        tot_fare=0
        for x in response:
            tot_fare+=int(x[1])
        date_avg[date]=(tot_fare/10)
        
        
        
        
        if date_[2]=='28' and date_[1]=='02':
                date_=[date_[0],'03','01']
                
        elif date_[2]=='31' and date_[1]=='12':
            date_=[str(int(date_[0])+1),'01','01']
                        
        elif date_[2]=='30' or date_[2]=='31':
            date_[2]='01'
            if date_[1][0]!='0' or date_[1]=='09' or date_[1]=='08':
                date_[1]=str(int(date_[1])+1)
            else:
                date_[1]='0'+str(int(date_[1])+1)

        elif date_[2][0]=='0' and date_[2]!='09' and date_[2]!='08':
            date_[2]='0'+str(int(date_[2])+2)
            
        else:
            date_[2]=str(int(date_[2])+2)

        date=date_[0]+'-'+date_[1]+'-'+date_[2]
        
    return date_avg

def get_forbidden_dates(city,st_date):

    forbidden_dates={}
    date=st_date
    for i in range(15):

        date_=date.split('-')

        forecast=str(findweather(city,date_[2],date_[1]))
        date_put=date_[0]+date_[1]+date_[2]
        if 'thunderstorm' in forecast:

            forbidden_dates[date_put]=1

        if 'rain' in forecast:
            
            forbidden_dates[date_put]=1

        if 'hail storm' in forecast:

            forbidden_dates[date_put]=1

        
        
        if date_[0]=='28' and date_[1]=='02':
                date_=[date_[0],'03','01']
                
        elif date_[0]=='31' and date_[1]=='12':
            date_=[str(int(date_[0])+1),'01','01']
                        
        elif date_[0]=='30' or date_[0]=='31':
            date_[0]='01'
            if date_[1][0]!='0' or date_[1]=='09' or date_[1]=='08':
                date_[1]=str(int(date_[1])+1)
            else:
                date_[1]='0'+str(int(date_[1])+1)

        elif date_[0][0]=='0' and date_[0]!='09' and date_[0]!='08':
            date_[0]='0'+str(int(date_[0])+2)
            
        else:
            date_[0]=str(int(date_[0])+2)

        date=date_[0]+'-'+date_[1]+'-'+date_[2]
    return forbidden_dates


def get_optimal_date(orig_code,dest_code,st_date,city):
    
    forbidden_dates=get_forbidden_dates(city,st_date)
    date_avg=get_flight_fare_average(orig_code,dest_code,st_date)
    t=1000000000000000000000
    
    for x in date_avg:
        if x not in forbidden_dates:
            if date_avg[x]<=t:
                t=date_avg[x]

    return(t)
            
    
inp1=raw_input("Enter destination city - ")
inp2=raw_input("Enter its airport code - ")
inp3=raw_input("Enter your home city airport code")
inp4=raw_input("Enter a tentative date for travel (format- yyyy-mm-dd)")

print("you should plan your trip around - ")
k=(get_optimal_date(inp3,inp2,inp4,inp1))
print(k)

        
    

    
