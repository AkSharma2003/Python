
from pydantic import BaseModel,Field,field_validator,model_validator
from typing_extensions import Annotated
from typing import List,Dict

# you can operat field operator in two mood after and befor andk it have bydefault after

class patient(BaseModel):
    name:str
    email:str
    age:int
    weight:float
    maried:bool
    alergies:List[str]
    contact:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def emial_validator(cls,value):
        vailid_doman=['hdfc.com','iiitvadodara.ac.in','icici.com']
        doman_name=value.split('@')[-1]
        
        if doman_name not in vailid_doman:
            raise ValueError('not a vailid doman')
        
        return value
        
    @field_validator('name')
    @classmethod
    def update_name(cls,value):
        return value.upper()
    
def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.maried)
    print(patient.alergies)
    print(patient.contact)
    print("patient data inserted successfull")
    
def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.maried)
    print(patient.alergies)
    print(patient.contact)
    print("patient data update successfull")

patient_info={"name":"Ankit",'email':'abc@hdfc.com',"age":23,"weight":45.5,"maried":False,"alergies":['fiver','dust'],"contact":{'phone':'1234567890 '}}
patient_info2={"name":"missPai",'email':'abc@icici.com',"age":18,"weight":45.5,"maried":False,"alergies":['fiver','dust'],"contact":{'phone':'1234567890'}}

patient1=patient(**patient_info)
patient2=patient(**patient_info2)

insert_patient_data(patient1)
update_patient_data(patient2)

from pydantic import BaseModel,Field,field_validator
from typing_extensions import Annotated
from typing import List,Dict

# you can operat field operator in two mood after and befor andk it have bydefault after
