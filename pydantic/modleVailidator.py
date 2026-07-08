
from pydantic import BaseModel,Field,field_validator,model_validator,computed_field
from typing_extensions import Annotated
from typing import List,Dict

# you can operat field operator in two mood after and befor andk it have bydefault after

class patient(BaseModel):
    name:str
    email:str
    age:int
    weight:float 
    height:float
    maried:bool
    alergies:List[str]
    contact:Dict[str,str]
    
    @model_validator(mode='after')
    # @classmethod
    def validate_emargency_contact(self):
        if self.age>60 and 'emargency' not in self.contact:
            raise ValueError('patient greater than 60 so please provide emargency contact')
        return self
    
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
    
    @computed_field
    @property
    def create_bmi(self)->float:
        return round(self.weight / (self.height ** 2), 2)
        
    
def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.maried)
    print(patient.alergies)
    print(patient.contact)
    print("BMI=",patient.create_bmi)
    print("patient data inserted successfull")
    
def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print("BMI=",patient.create_bmi)
    print(patient.maried)
    print(patient.alergies)
    print(patient.contact)
    print("patient data update successfull")

patient_info={"name":"Ankit",'email':'abc@hdfc.com',"age":80,"weight":45.5,"height":1.75,"maried":False,"alergies":['fiver','dust'],"contact":{'phone':'1234567890','emargency':'1234'}}
patient_info2={"name":"missPai",'email':'abc@icici.com',"age":18,"weight":45.5,"height":1.65,"maried":False,"alergies":['fiver','dust'],"contact":{'phone':'1234567890'}}

patient1=patient(**patient_info)
patient2=patient(**patient_info2)

insert_patient_data(patient1)
update_patient_data(patient2)

from pydantic import BaseModel,Field,field_validator
from typing_extensions import Annotated
from typing import List,Dict

# you can operat field operator in two mood after and befor andk it have bydefault after
   