from pydantic import BaseModel

class UserDetails(BaseModel):
    name : str
    age : int