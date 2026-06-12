# Serialization :- process of converting python data type to JSON format
# Deserializtion :- pricess of converting JSON to python data types

# JSON means java screept on notation

# serialization using json modul
import json

#list
L=[1,2,3,4]
with open('demo.json','w') as f:
    json.dump(L,f)
    
    
#dict

d={
    'nmae':'Miss PAI',
    'age':'1',
    'gender':'female'
}

with open('demo.json','w') as f:
    json.dump(d,f,indent=4) # use indent for gappinig 
    
with open('demo.json','r') as f:
    d=json.load(f) # load for reading JSON data
    print(d)
    