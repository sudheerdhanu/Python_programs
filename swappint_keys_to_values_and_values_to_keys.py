d={"a":1,"b":2,"c":1,"d":2}
print("Input :",d)
'create the a sample dict like as a i/p dict'
d1={}

for i in d.values():
    d1[i]=[]


keys=d.keys()
values=set(d.values())
for i in values:
    for key in d.keys():
        if(d[key]==i):
            d1[i].append(key)

print("output:",d1)


