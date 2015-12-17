import requests
import json
def find_hotels(state, city):
    url2='http://127.0.0.1:5000/get-hotel-list?state=Uttar-Pradesh&city=Lucknow'
    url="https://localhost:5000"
    url=url+"/get-hotel-list?state="+state+"&city="+city
    res=requests.get(url2)
    k=json.loads(res.content)
    

##k=find_hotels("Uttar-Pradesh", "Lucknow")
    sorted_k=[]
    print(len(k))
    for i in range(len(k)):
        
        sorted_k.append([])
    print(sorted_k)
    for x in k:
        y=int(x)
    ##    print(k[y-1])
        sorted_k[y-1]=k[x]

    return sorted_k
    
