#d= nested dictionary
d={"emp1":{"name":"Anuraag", "role":"jdev"},
   "emp2":{"name":"Mahesh", "role":"sdev"},
   "emp3":{"name":"Yashu", "role":"dev"}}
print("\n",d)

#iterate through nested dictionary
for key,value in d.items():
    print("\nEmployee Id:",key)
    for i in value:
        print(i+ ":",value[i])


#accessing nested dictionary items
print("\n",d["emp1"]["name"])
print(d['emp2']['role'])

"""print(d["emp3"]["sal"]) will raise key error exception"""
#get() method will avoid the key error exception
print("\n",d['emp3'].get("name"))
print(d['emp3'].get("sal"))

#change nested dictionary items
d["emp3"]["name"]="afaq"
d['emp3']['role']='manager'
print("\nchanged emp3=",d["emp3"])

#add or update nested dict items
d['emp2']={"name":"Yashu","role":"jdev"}
print("\n",d)
d['emp4']={"name":"Mahesh","role":"sdev"}
print("\n",d)

#merging dictionaries
d1={"emp1":{"name":"Anuraag", "role":"jdev"},
    "emp2":{"name":"Mahesh", "role":"sdev"}}

d2={"emp2":{"name":"Yashu", "role":"dev"},
    "emp3":{"name":"Afaq","role":"manager"}}

d1.update(d2)
"""emp2 will be updated and emp3 will be added in d1"""
print("\n",d1)

#removing dict items
print("\nd=",d)
x=d.pop("emp3")
print("\n",d)
"""removed item x"""
print("removed=",x)
#popitem() will remove last inserted item
e=d.popitem()
print(d)
print("\nremoved item=",e)

#del will delete the item
d3={"emp1":{"name":"Anuraag", "role":"jdev"},
   "emp2":{"name":"Mahesh", "role":"sdev"},
   "emp3":{"name":"Yashu", "role":"dev"}}
del d3["emp3"]
print("\nd3=",d3)

#dict using zip() method
id=["emp1","emp2","emp3"]
empInfo=[{"name":"Anuraag", "role":"dev"},
         {"name":"Mahesh", "role":"dev"},
         {"name":"Yashu", "role":"dev"}]
a=dict(zip(id,empInfo))
print("\na=",a)

#dict using fromkeys() method
id=["emp1","emp2","emp3"]
defaults={"name":" ", "role":" "}
b=dict.fromkeys(id,defaults)
print("\n",b)