import requests
from bs4 import BeautifulSoup
import sqlite3
import os



def get_state_reviews(state):
    if ' ' in state:
        state=state.split()
        state=state[0]+'-'+state[1]
    if 'jammu' in state:
        state='jammu-kashmir'
    
    state_url='http://www.holidayiq.com/states/'+state+'/'

    state_page=requests.get(state_url)
    state_ob=BeautifulSoup(state_page.content)

    
    review=[]
    title=[]
    p_name=[]
    q=list(state_ob.find_all(True))
    for y in q:
        if y.has_attr('class') and y.has_attr('style'):
            try:
                if 'h2' in y['class']:
                    if "color: #000000; margin-top: 0 !important;" in y['style']:
                        title.append('## '+y.a.string.encode('ascii','ignore'))
            except: continue
        try:
            if y.name=='div' and y.has_attr('class'):
                comment=y.blockquote.string.encode('ascii','ignore')
                if comment not in review:
                    review.append(comment)
        except: continue
        
        try:
            if y.name=='span' and y.has_attr('class'):
                if 'reviews-no' and 'htr-reviews-no' in y['class']:
                    person=y.string.encode('ascii','ignore')
                    if person not in p_name:
                        p_name.append(person)
        except:
            continue

    if len(review)==0:
        for y in q:
            try:
                if y.name=='blockquote' and y.has_attr('class'):
                    if 'margin0' and 'review_datail_height' in y['class']:
                        comment=y.get_text().strip()
                        if comment not in review:
                            review.append(comment)
            except: continue
    result=[]
    result.append(p_name)
    result.append(title)
    result.append(review)

    return result

##print(get_state_reviews(raw_input()))

def display_city_reviews(state,city):
    print('under construction')
##   city_list=get_city_list_with_details(state)
##   
##   for x in city_list:
##       if x[3]==city:
##           city_url=x[0]
##        
##    city_page=requests.get(city_url)
##    city_ob=BeautifulSoup(city_page.content)
##
##    review=[]
##    title=[]
##    p_name=[]
##
##    q=list(city_ob.find_all(True))
##    for y in q:
##        if y.has_attr('class') and y.has_attr('style'):
##            try:
##                if 'h2' in y['class']:
##                    if "color: #000000; margin-top: 0 !important;" in y['style']:
##                        title.append('## '+y.a.string.encode('ascii','ignore'))
##            except: continue
    

    
    


def get_city_list_with_details(state):
    if ' ' in state:
        state=state.split()
        state=state[0]+'-'+state[1]
    if 'jammu' in state:
        state='jammu-kashmir'
    
    state_url='http://www.holidayiq.com/states/'+state+'/'

    state_page=requests.get(state_url)
    state_ob=BeautifulSoup(state_page.content)

    q=list(state_ob.find_all(True))
    
    city={}
    q2=list(state_ob.find_all(True))
    for x in q2:
        try:
            if x.has_attr('class'):
                city_name=x.h5.string.encode('ascii','ignore')
                if city_name not in city:
                    city[city_name]=[]
                    city[city_name].append(x.h5.a['href'])

            if x.name=='a':
                tmp=x.string.encode('ascii','ignore')
                if 'sightseeing' in tmp:
                    if len(city[city_name])==1:
                        city[city_name].append(x['href'])
                
        except: continue      
    """ yamuna nagar haryana check karna hai, kuch gadbad hai"""
    i_d=1
    for x in city:
        city[x].append('http://www.holidayiq.com/hotels/'+x.split(',')[0])
        city[x].append(x.split(',')[0])
##        city[x].append(i_d)
        i_d+=1

    ##city[0]=city_page link
    ##city[1]=sight-seeing_page link
    ##city[2]=hotels_page link
    ##city[3]=city name
    return city

##print(get_city_list_with_details(raw_input()))



def get_sightseeing_list(state,city):
    city_details=get_city_list_with_details(state)
    for x in city_details:
        if city_details[x][-1]==city:
##            try:
            ss_url=city_details[x][1]
            ss_page=requests.get(ss_url)
            ss_ob=BeautifulSoup(ss_page.content)
##            except:
##            print('Data not available for this choice')
##            assert(False)
    try:
        q4=list(ss_ob.find_all(True))
    except: return ('Data not available for this choice')
    ss_list={}
    i_d=1
    for x in q4:
        if x.name=='h5':
            tmp=x.string.encode('ascii','ignore')
            ss_list[i_d]=[tmp,x.a['href']]
            i_d+=1
    ##ss_list[0]=sight-seeing destination name
    ##ss_list[1]=destination url

    return ss_list

##t1=raw_input()
##t2=raw_input()
##print(get_sightseeing_list(t1,t2))


def get_sightseeing_reviews(state,city,ss_id):
    ss_list=get_sightseeing_list(state,city)
    for x in ss_list:
        if x==int(ss_id):
            sight_page_url=ss_list[x][-1]
            break
    
    sight_page=requests.get(sight_page_url)
    sight=BeautifulSoup(sight_page.content)

    q4=list(sight.find_all(True))
    details=[]
    c=0
    for x in q4:
        if x.name=='span':
            try:
                if 'travellers-recommended-for' in x['class']:
                    tmp=x.string.encode('ascii','ignore')
                    details.append(tmp)
                if 'travellers-recommendation-details' in x['class']:
                    tmp=x.string.encode('ascii','ignore')
                    details.append(tmp)
            except: continue
    title=[]
    review=[]
    p_name=[]
    
    for x in q4:
        try:
            if x.name=='p':
                if x.has_attr('class') and x.has_attr('style'):
                    tmp=(x.a.string.encode('ascii','ignore'))
                    title.append(tmp)
            if x.name=='blockquote':
                tmp=(x.string.encode('ascii','ignore'))
                review.append(tmp)

            if x.name=='span' and x.has_attr('class'):
                if 'reviews-no' and 'htr-reviews-no' in x['class']:
                    person=x.string.encode('ascii','ignore')
                    if person not in p_name:
                        p_name.append(person)
                    
        except: continue
        
    return(details,p_name,title,review)

##inp1='uttar pradesh'
##inp2='Varanasi'
##inp3=1
##
##print(get_sightseeing_reviews(inp1,inp2,inp3))

def get_hotel_list(state,city):
    city_details=get_city_list_with_details(state)
    for x in city_details:
        if city_details[x][-1]==city:
            city_hotels_url=city_details[x][2]
    
    s2=requests.get(city_hotels_url)
    soup_city_hotel=BeautifulSoup(s2.content)

    q=list(soup_city_hotel.find_all(True))

    load_hotel_names=[]
    i=0
    for x in q:
        if(x.has_attr('class')):
            if 'hotel-list-hotel-name' in x['class']:
                load_hotel_names.append([])
                load_hotel_names[i].append(i+1)
                load_hotel_names[i].append(x.a['title'])
                load_hotel_names[i].append(x.a['href'])
                i+=1
            elif 'hotel-semlayout-title' in x['class']:
                load_hotel_names.append([])
                load_hotel_names[i].append(i+1)
                load_hotel_names[i].append(x.a.string.encode('ascii','ignore'))
                load_hotel_names[i].append(x.a['href'])
                i+=1
##    loadhotelnames[0]=id,[1]=hotelname,[2]=link
    return(load_hotel_names)


##t1=raw_input()
##t2=raw_input()
##print(get_hotel_list(t1,t2))



def get_hotel_reviews(state,city,hotel_id):
    hotel_list=get_hotel_list(state,city)
    c=0
    for x in hotel_list:
        if x[0]==hotel_id:
            c=1
            hotel_url=x[2]
    if c==0:
        return('id does noe exist')
    

    s3=requests.get(hotel_url)
    soup_hotel=BeautifulSoup(s3.content)
    q2=list(soup_hotel.find_all(True))

    title=[]
    review=[]
    p_name=[]  ##abhi karna hai
    for y in q2:
        if y.has_attr('class'):
            try:
                if 'reviews-tag-line-link' in y['class']:
                    tmp=(y.a.string.encode('ascii','ignore'))
                    title.append(tmp)
            except: continue
            
            try:
                if y.name=='blockquote':
                    tmp=(y.string.encode('ascii','ignore'))
                    review.append(tmp)
            except: continue
            
            try:
                if y.name=='span' and y.has_attr('class'):
                    if 'reviews-no' and 'htr-reviews-no' in y['class']:
                        person=y.string.encode('ascii','ignore')
                        if person not in p_name:
                            p_name.append(person)
            except: continue
                

    return(p_name,title,review)

##inp1='uttar pradesh'
##inp2='Varanasi'
##inp3=2
##
##print(get_hotel_reviews(inp1,inp2,inp3))


    
def get_ss_time(state,city):
    conn=sqlite3.connect('ss_cache.db')
    c=conn.cursor()
    
    def tableCreate():
        c.execute("CREATE TABLE IF NOT EXISTS ss_time( query TEXT, time TEXT)")

    def dataEntry(query, time):
        c.execute("INSERT INTO ss_time (query, time) VALUES (?,?)",
              (query, time))
        conn.commit()
    tableCreate()
##    if  os.path.isfile('ss_cache.db'):
##        pass
##    else:
##        tableCreate()
        
    #sql="SELECT * FROM ss_time WHERE keyword =?"
    queryasked= state+city
    c.execute('''SELECT query, time FROM ss_time''')
    all_rows=c.fetchall()
    query_lst=[]
    for row in all_rows:
        
        query_lst.append(row[0])
    if queryasked in query_lst:
       # print "query in db"
##        c.execute('''SELECT query, time FROM ss_time WHERE query=?''', (queryasked,))
        c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="%s"'.\
            format(coi="time", tn="ss_time", cn="query") % queryasked)
        all_rows_for_query = c.fetchall()
        res=[]
        for tu in all_rows_for_query:
            #res.append(int(tu[0]))
            v=tu[0]
            v=v.replace('[','')
            v=v.replace(']','')
            lop=v.split(',')
            l=[]
            for each in lop:
                l.append(float(each))
            
        return l
        
    else:
        #print "query not in db"
        
        
    #dataEntry(idfordb,forecast_list[0], forecast_list[1], forecast_list[2])

        ss_folder=get_sightseeing_list(state,city)
        
        time=[]
        #print(len(ss_folder))
        for x in ss_folder:
            ss_page=requests.get(ss_folder[x][1])
            ss=BeautifulSoup(ss_page.content)
            q5=list(ss.find_all(True))
            check=0
            for y in q5:
                if y.name=='span':            
                    if y.has_attr('class') and 'travellers-recommended-for' in y['class']:
                        tmp=y.string.encode('ascii','ignore')
                        if 'Length' in tmp: check=1

                    if y.has_attr('class') and 'travellers-recommendation-details' in y['class']:
                        if check==1:
                            tmp=y.string.encode('ascii','ignore')
                            if '3hrs' in tmp:
                                time.append(4.25)
                            elif '1-2hrs' in tmp:
                                time.append(1.5)
                            elif '1hr' in tmp:
                                time.append(0.7)
                            else:
                                time.append(1)
                            check=0
        if len(ss_folder)>len(time):
            for i in range(len(ss_folder)-len(time)):
                time.append(1)
        dataEntry(queryasked, str(time))
        return time    


##t1=raw_input()
##t2=raw_input()
##print(get_ss_time(t1,t2))

