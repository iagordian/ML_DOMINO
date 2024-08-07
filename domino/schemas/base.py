
from pydantic import BaseModel, ConfigDict

class Model(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='allow', ser_json_bytes='base64', protected_namespaces=())