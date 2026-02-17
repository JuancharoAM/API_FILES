from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from schemas import ImageUploadRequest, ImageUploadResponse
from utils import save_image
from pathlib import Path
import os

app = FastAPI(title="Image Upload API")

# Base storage path
BASE_STORAGE_PATH = Path("/app/data")

@app.post("/upload", response_model=ImageUploadResponse)
async def upload_image(request: ImageUploadRequest):
    try:
        saved_path = save_image(
            nombre_archivo=request.nombre_archivo,
            b64_content=request.archivo,
            tipo=request.tipo
        )
        return ImageUploadResponse(
            success=True,
            message="Image saved successfully",
            path=saved_path
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/files/{tipo}/{filename}")
async def serve_file(tipo: str, filename: str):
    """Serve an uploaded file by type and filename."""
    # Sanitize inputs to prevent path traversal
    safe_tipo = tipo.replace("..", "").replace("/", "").replace("\\", "")
    safe_filename = filename.replace("..", "").replace("/", "").replace("\\", "")
    
    file_path = BASE_STORAGE_PATH / safe_tipo / safe_filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    # Determine media type
    ext = file_path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
    }
    media_type = media_types.get(ext, "application/octet-stream")
    
    return FileResponse(str(file_path), media_type=media_type)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
