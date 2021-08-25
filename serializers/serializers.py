from pydantic import BaseModel


class MetaSerializer(BaseModel):
    message: str
