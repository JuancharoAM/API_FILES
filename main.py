from fastapi import FastAPI, HTTPException
from schemas import ImageUploadRequest, ImageUploadResponse
from utils import save_image

app = FastAPI(title="Image Upload API")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
