##up ke reviews nhi de rha
## kerala me bhi problem
## j and k aur delhi ko fix karo


print('Enter the state you wish to visit')
##print('Jammu & Kashmir jana hai to Jammu-Kashmir likhna')
state=raw_input()


if ' ' in state:
    state=state.split()
    state=state[0]+'-'+state[1]
    


import requests
from bs4 import BeautifulSoup

state_url='http://www.holidayiq.com/states/'+state+'/'

state_page=requests.get(state_url)
state_ob=BeautifulSoup(state_page.content)

print('Enter OK')
##print('Enter 2 if you want to see the reviews for this state else enter 1')
##print('aur agar seedhe sight-seeing menu pe jana hai to Na likho')
resp=raw_input()

review=[]
title=[]
p_name=[]
if resp==2:
    j=1
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
##    if len(review)==0:
##        print('started')
##        for y in q:
##            try:
##                if y.name=='blockquote' and y.has_attr('class'):
####                    print(y['class'])
##                    if 'margin0' and 'review_datail_height' in y['class']:
####                        print(y.br)
##                        comment=y.get_text().strip()
####                        print(comment)
##                        if comment not in review:
##                            review.append(comment)
####                            print(comment)
##            except: continue
    for i in range(len(review)):
        print p_name[i]
        print title[i]
        print review[i]
        print

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
                city[city_name].append(x['href'])
            
    except: continue

print
print
print('enter serial number for the corresponding city')
print
i_d=1
for x in city:
    city[x].append('http://www.holidayiq.com/hotels/'+x.split(',')[0])
    city[x].append(i_d)
    print(str(i_d)+')')
    i_d+=1
    print(x)
##    print(city[x])
    print

print
print('Plz enter')
response_serial=int(raw_input())

##print(city)

for x in city:
    if city[x][-1]==response_serial:
        load_url= city[x][1]
        break
        
place_page=requests.get(load_url)
place=BeautifulSoup(place_page.content)
q4=list(place.find_all(True))

place_folder={}
i_d=1
for x in q4:
    if x.name=='h5':
        tmp=x.string.encode('ascii','ignore')
        place_folder[i_d]=[tmp,x.a['href']]
        i_d+=1
      
    
##time=[]   
##for x in place_folder:
##    print(place_folder[x][1])
##    ss_page=requests.get(place_folder[x][1])
##    ss=BeautifulSoup(place_page.content)
##    q5=list(ss.find_all(True))
##    print('done')
##    for y in q5:
##        if y.name=='span':            
##            if y.has_attr('class') and 'travellers-recommended-for' in y['class']:
##                tmp=x.string.encode('ascii','ignore')
##                print(tmp)
##
####                print(y['class'])
##            if y.has_attr('class') and 'travellers-recommendation-details' in y['class']:
##                tmp=y.string.encode('ascii','ignore')
##                print('ok')
##                if tmp.split()[0]!='During':
##                    print('ok2')
##                    time.append([x,place_folder[x][0],tmp])

##from tmp3 import *
##
##t1=(get_ss_time(place_folder))
##
##from day_planner import *
##
##yashu=recommend_package(1,place_folder,t1)
        
print('Now choose your sight-seeing destination')
print

for x in place_folder:
    print(str(x)+')')
    print(place_folder[x][0])
    print

response=int(raw_input())
load_url=place_folder[response][1]


##load_url2='http://www.holidayiq.com/Kufri-Shimla-Sightseeing-549-18633.html'
sight_page=requests.get(load_url)
sight=BeautifulSoup(sight_page.content)

q4=list(sight.find_all(True))

print('""""Chief Features"""')
print

for x in q4:
    if x.name=='span':     
        try:
            if 'travellers-recommended-for' in x['class']:
                tmp=x.string.encode('ascii','ignore')
                print(tmp)
            if 'travellers-recommendation-details' in x['class']:
                
                tmp=x.string.encode('ascii','ignore')
                print('##'+tmp)
        except: continue

print
print('ab iska review dekhna hai to 1 dabao')
print
response=int(raw_input())
if response==1:
    for x in q4:
        try:
            if x.name=='p':
                if x.has_attr('class') and x.has_attr('style'):
                    print('###')
                    print(x.a.string.encode('ascii','ignore'))
                    print
            if x.name=='blockquote':
                print(x.string.encode('ascii','ignore'))
                print
                print
        except: continue


