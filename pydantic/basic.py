# there is no type validation and data validation in python so i need pydantic
# 1. define a padantic modle that reprsents the ideal schema of the data
#   * This includes the expected fields, there types, and any vailidation constraints (e.g. gt=0 for posetive number)

# 2. instaintiate the model with raw input data (usually a dictionary or JSON-like structure)
#   * Pydantic will automatically vailidate the data and coerce it into the correct python types (if possible)
#   * if the data doesn't meet the modlel's requarments Pydantic raises a vailidation error 

# 3. pass the vailidated modle object to function or use it throughout your codebase 
#   * This ensures that every part of your program works with clean, type-safe, and logically vailid data

from pydantic import BaseModel,Field
from typing_extensions import Annotated
from typing import List,Dict,Optional

class patient(BaseModel):
    name:Annotated[str,Field(max_length=40,title="name of the patint")]
    age:int=Field(gt=0, lt=120)
    weight:Annotated[float,Field(gt=0, strict=True)] # here use strict so type conversion is not allowed
    maried:bool
    alergies:Optional[List[str]]=None # here alergies is optional and also use optional = none becouse it have bydefault value is none
    contact:Dict[str,str]
    
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

patient_info={"name":"Ankit","age":23,"weight":45.5,"maried":False,"alergies":['fiver','dust'],"contact":{'email':'abc@gmail.com','phone':'1234567890 '}}
patient_info2={"name":"missPai","age":18,"weight":45.5,"maried":False,"alergies":['fiver','dust'],"contact":{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=patient(**patient_info)
patient2=patient(**patient_info2)

insert_patient_data(patient1)
update_patient_data(patient2)
