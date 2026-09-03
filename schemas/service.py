from pydantic import BaseModel


class NeedBase(BaseModel):
    family_id: str
    title_ar: str
    title_en: str
    category: str
    target_amount: float


class NeedCreate(NeedBase):
    pass


class NeedResponse(NeedBase):
    id: str
    raised_amount: float
    status: str

    class Config:
        from_attributes = True

# TODO: Add NeedUpdate and progress schemas
