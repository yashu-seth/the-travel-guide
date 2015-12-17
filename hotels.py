import requests
from bs4 import BeautifulSoup 

##print('hmmm.... to hotel dekhna hai?? To dekho na mana kon kiya hai...')
s=requests.get('http://www.holidayiq.com/hotels')

soup_main_hotels=BeautifulSoup(s.content)

ob1=soup_main_hotels.div

li=ob1.find_all('li')
##li = list for all elements containing li where city hotels are

print('Input the city of your choice')
print('Please ensure the initial letter is in caps')
inp_city=raw_input()
print('Your choice is '+inp_city)
try:
        for x in li:
                t=list(x.stripped_strings)
                #print "t is"+t
                #assert False
                for y in t:
                        if y=='Hotels in '+inp_city:
                                re=x.a['href']
                            
        if re:
                print('Hotel list is being loaded, this may not take long...')
except:
        print('please ensure that you have typed the correct spelling')
##        print('kg k bachche k tarah speeling mistake mat kar')


s2=requests.get(re)
soup_city_hotel=BeautifulSoup(s2.content)

q=list(soup_city_hotel.find_all(True))

load_hotel_names=[]
i=0
for x in q:
    if(x.has_attr('class')):
        if 'hotel-list-hotel-name' in x['class']:
            load_hotel_names.append([])
            load_hotel_names[i].append(x.a['title'])
            load_hotel_names[i].append(x.a['href'])
            i+=1
        elif 'hotel-semlayout-title' in x['class']:
            load_hotel_names.append([])
            load_hotel_names[i].append(x.a.string.encode('ascii','ignore'))
            load_hotel_names[i].append(x.a['href'])
            i+=1

                                
j=1
print('enter the number of hotels to see the reviews for')
tmp=int(raw_input())
if tmp>len(load_hotel_names): tmp=len(load_hotel_names)
##if tmp>10:
##        print('itna sara review dekhega to pgla jayega..')
##        print('par ab bola hai to dekho')
for x in load_hotel_names[:tmp]:
        try:
            
                print
                print(str(j)+')')
                j+=1
##                print(x)
                print(x[0])
                print
##                connect_timeout = 0.0001
##                read_timeout=1.0
##                try:
##                    
##                    s3=requests.get(url=x[1])#, timeout=(connect_timeout, 10.0))
##                except requests.exceptions.ConnectionError as e:
##                    print "These aren't the domains we're looking for."
##                except requests.exceptions.ConnectTimeout as e:
##                    print "Too slow Mojo!"
                s3=requests.get(x[1])
                try:
                    s3.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print "And you get an HTTPError:", e.message

                soup_hotel=BeautifulSoup(s3.content)
                print ("got content now")
                q2=list(soup_hotel.find_all(True))
                for y in q2:
                        if y.has_attr('class'):
                                try:
                                    if 'reviews-tag-line-link' in y['class']:
                                        print
                                        print
                                        print('## '+y.a.string.encode('ascii','ignore'))
                                except: continue
                                
                                try:
                                    if y.name=='blockquote':
                                        print(y.string.encode('ascii','ignore'))
                                except: continue
                                
                                        
        except: continue
                                


