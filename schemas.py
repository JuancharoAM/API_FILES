from pydantic import BaseModel
from typing import Optional

class ImageUploadRequest(BaseModel):
    nombre_archivo: str
    archivo: str  # Base64 encoded string
    tipo: Optional[str] = "OTROS"

class ImageUploadResponse(BaseModel):
    success: bool
    message: str
    path: Optional[str] = None
