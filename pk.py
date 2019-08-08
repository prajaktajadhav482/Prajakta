cname=input("enter name")
units=eval(input("enter no.of units consumed"))
dc=50
if units>500:
    charge=3000+dc
elif units>100 and units<=200:
    charge=500+dc
elif units>200 and units<=300:
    charge=650+dc
elif units>300 and units<=500:
    charge=800+dc
else:
     charges=0+dc
print('enter name',cname)
print('no. of units consumed',units)
print('charges',charge)      
    
