import urllib
def find_map(center_lst):
    
    #center=raw_input("enter a location")
    final_lst=[]
    for center in center_lst:
        new=center.replace(",", "")
        newer=center.replace(" ", "+")
        final_lst.append(newer)
    url='https://maps.googleapis.com/maps/api/staticmap?center='+final_lst[0]+',IN&zoom=13&size=640x640&key=AIzaSyB0Z5xwCsHNYnkA1YSYFePn_qNOQ-R27MM'#&maptype=hybrid'
    for center in final_lst:
        url=url+"&markers=color:blue%7Clabel:S%7C"+center
    for y in range(10):
        try:
            res=urllib.urlopen(url)
            break
        except:
            continue
    f=open('yes.jpg','wb')
    f.write(res.read())
    f.close()
    return f

