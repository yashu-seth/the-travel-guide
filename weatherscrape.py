import requests
from bs4 import BeautifulSoup, Tag

##print ("Enter the name of the city")
##print("Ensure that the first letter is in caps")
##print("In case you are obsessed with Bangalore...put it's new name...Bengaluru")
##city=raw_input()
def findweather(city, dd, mm):
    for y in range(10):
        try:
            wiki_response=requests.get('http://en.wikipedia.org/wiki/List_of_airports_in_India')
            break
        except:
            continue
    wiki_soup=BeautifulSoup(wiki_response.content)
    table=wiki_soup.findAll('table')
    all_tr=table[3].findAll('tr')
    code=''
    count=1
    for tr in all_tr[1:]:
        
        #print count
        count+=1
        resp=[]
        all_td=tr.findAll('td')
        for td in all_td:
            resp.append(td.get_text().strip())
        for text in resp:
            if city in text:
                #print resp
                for r in resp:
                    if r[0]=='V':
                        code=r
        if code!='':
            break
        else:
            continue


    #print code
    if city=='Goa':
        code='VAGO'
##    print "enter date on which you plan to visit the place"
##    print "input date then month and then year seperated by a new line"
##    dd=raw_input()
##    mm=raw_input()
##    yy=raw_input()
    url='http://www.wunderground.com/history/airport/'+code+'/1972/'+mm+'/'+dd+'/PlannerHistory.html?req_city='+code+'&req_state=&req_statename=India&reqdb.zip=00000&reqdb.magic=3&reqdb.wmo=42369&MR=1'
    for y in range(10):
        try:
            response=requests.get(url)
            break
        except:
            continue
    soup=BeautifulSoup(response.content)
    mydivs=soup.findAll("div",{"class": "layerImage"})
    lst_fore=[]
    for mydiv in mydivs:
        imagehead_tags=mydiv.findAll("div",{"class":"imageHead"})
        #print imagehead_tags
        for tags in imagehead_tags:
            lst_fore.append(tags.get_text())##ajeeb
        

    w=soup.findAll("div",{"class":"layerAbout"})
    paralst=[]
    for layerabouts in w:
        paralst.append(layerabouts.findAll("p"))
    #print paralst
    #assert False
    forecast=[]
    for each in paralst:
        for elem in each:
            forecast.append(elem.text)
    #print forecast
##    for comment in forecast:
##        print comment
##    for keyword in lst_fore:
##        print keyword

    return forecast
print ("Enter the name of the city")
print("Ensure that the first letter is in caps")
print("In case you are obsessed with Bangalore...put it's new name...Bengaluru")
city=raw_input()

print "enter date on which you plan to visit the place"
print "input date then month and then year seperated by a new line"
dd=raw_input()
mm=raw_input()
yy=raw_input()
h=(findweather(city, dd, mm))
for x in h:
    print(str(x))
