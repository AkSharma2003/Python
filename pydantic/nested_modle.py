from pydantic import BaseModel


class address(BaseModel):
    city:str
    state:str
    pin:str
    
class patient(BaseModel):
    name:str
    gender:str
    age:int
    address:address
    
add_dict={'city':'Aurangabad','state':'bihar','pin':'824102'}
address1=address(**add_dict)

p_dict={'name':'Ankit Kumar Sharma','gender':'Male','age':23,'address':address1}
patient1=patient(**p_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
    
# why should use nested modle :-
# 1. batter organization of related data
# 2. reusablity :- use vitals in multipal modle
# 3. Vailidation :- Nested models are valideted automatically-no extra needed

temp=patient1.model_dump() # convert into dictionary & it have also include and exclud option modle(include['name',...])
print(temp)
print(type(temp))

temp=patient1.model_dump_json() # convert into json file & it have also include and exclud option modle(include['name',...])
print(temp)
print(type(temp)) 


# exlude_unset=true is a method who dont retuen bydefault value or jo set nahi kiya gya ho

