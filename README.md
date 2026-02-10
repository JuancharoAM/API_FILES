# Image Upload API

API desarrollada con FastAPI para recibir imágenes en formato Base64 y almacenarlas de forma organizada en un volumen compartido de Docker.

## Características

-   **Clasificación Automática**: Guarda las imágenes en carpetas específicas (`receipts`, `invoices` o `Other`) según el tipo proporcionado.
-   **Docker Ready**: Configuración completa con Dockerfile y Docker Compose.
-   **Persistencia**: Uso de volúmenes de Docker para asegurar que las imágenes no se pierdan.
-   **Decodificación Base64**: Maneja imágenes enviadas directamente en el cuerpo del JSON.

## Estructura del Proyecto

```text
.
├── main.py              # Punto de entrada de la aplicación FastAPI
├── utils.py             # Lógica de guardado y procesamiento de archivos
├── schemas.py           # Definición de modelos Pydantic (Request/Response)
├── requirements.txt     # Dependencias del proyecto
├── Dockerfile           # Configuración de la imagen Docker
├── docker-compose.yml   # Orquestación de contenedores y volúmenes
└── data/                # Carpeta local vinculada al volumen (se crea automáticamente)
    ├── receipts/
    ├── invoices/
    └── Other/
```

## Requisitos

-   Docker y Docker Compose instalado.

## Instalación y Ejecución

Para levantar el servicio, simplemente ejecuta:

```bash
docker-compose up --build
```

El API estará disponible en `http://localhost:8080`.

## Uso del API

### Endpoint: Subida de Imagen

-   **URL**: `/upload`
-   **Método**: `POST`
-   **Cuerpo (JSON)**:

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `nombre_archivo` | `string` | Nombre con el que se guardará el archivo (ej: `test.jpg`). |
| `archivo` | `string` | Contenido de la imagen codificado en Base64. |
| `tipo` | `string` | (Opcional) `receipts`, `invoices`. Cualquier otro valor o ausencia guardará en `Other`. |

#### Ejemplo de Request (curl)

```bash
curl -X POST "http://localhost:8080/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre_archivo": "recibo_001.png",
    "archivo": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==",
    "tipo": "receipts"
  }'
```

### Documentación Interactiva

Puedes acceder al Swagger UI generado automáticamente por FastAPI en:
`http://localhost:8080/docs`

## Pruebas Locales (Sin Docker)

Si deseas probar la lógica de guardado sin usar Docker:

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el script de prueba: `python test_logic.py`
