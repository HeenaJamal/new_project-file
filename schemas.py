from pydantic import BaseModel
from pydantic import BaseModel, Field, ConfigDict

class SignupRequest(BaseModel):
    name: str
    mobile: str
    email: str
    profession: str
    city: str

class LoginRequest(BaseModel):
    mobile: str
    otp: str

class UserResponse(BaseModel):
    name: str
    role: str

#from pydantic import BaseModel

class DataSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    A: str
    B: str
    C: str
    D: str
    E: str
    F: str
    G: str
    H: str
    I: str
    J: str
    K: str
    L: str
    M: str
    N: str
    O: str
    P: str
    Q: str
    R: str
    S: str
    T: str
    U: str
    V: str
    
'''    class Config:
        orm_mode = True'''




   
    # Define your fields here

