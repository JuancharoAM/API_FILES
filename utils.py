import os
import base64
from pathlib import Path

# Base directory for storing images inside the container
BASE_STORAGE_PATH = Path("/app/data")

def save_image(nombre_archivo: str, b64_content: str, tipo: str) -> str:
    """
    Decodes a base64 string and saves it to a directory based on 'tipo'.
    Returns the absolute path of the saved file.
    """
    # Normalize 'tipo' to handle receipts, invoices, or Other
    if tipo.upper() == "COMPROBANTE":
        subfolder = "COMPROBANTE"
    elif tipo.upper() == "FACTURA":
        subfolder = "FACTURA"
    else:
        subfolder = "OTRO"

    # Create target directory if it doesn't exist
    target_dir = BASE_STORAGE_PATH / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)

    # Full file path
    file_path = target_dir / nombre_archivo

    # Decode and save
    try:
        # Remove header if present (e.g., "data:image/png;base64,")
        if "," in b64_content:
            b64_content = b64_content.split(",")[1]
            
        image_data = base64.b64decode(b64_content)
        with open(file_path, "wb") as f:
            f.write(image_data)
        
        return str(file_path)
    except Exception as e:
        raise Exception(f"Failed to save image: {str(e)}")
