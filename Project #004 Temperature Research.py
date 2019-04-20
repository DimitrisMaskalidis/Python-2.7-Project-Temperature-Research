av=0; max=0; cold=0; count=0; pl=0; pres=0
city=raw_input("Write city name: ")
while city!="END":
    count+=1
    temper=input("Write the temperature of the day: ")
    maxTemp=temper
    minTemp=temper
    for i in range(29):
        av+=temper
        if temper<5:
            pl+=1
        if temper>maxTemp:
            maxTemp=temper
        if temper<minTemp:
            minTemp=temper
        temper=input("Write the temperature of the day: ")
    print "The differance between highest and lowest temperature is",maxTemp-minTemp
    av=av/30.0
    if count==1:
        max=av
    if av>max:
        max=av
        maxname=city
    if av>30:
        pres+=1
    if pl==30:
        cold+=1
    pl=0
    city=raw_input("Write city name: ")
print "The percentage of the cities with average temperature more than 30 is",count/pres*100,"%"
print "The city with the highest average temperature is",maxname,"with",max,"average temperature"             
if cold>0:
    print "There is a city with temperature below 5 every day"
        
