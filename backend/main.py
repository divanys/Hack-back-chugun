import uvicorn
from backend.src.application import EduConnectApplication
from backend.configs import api_settings


if __name__ == "__main__":
    uvicorn.run(
        app=EduConnectApplication().app,
        host=api_settings.API_HOST,
        port=api_settings.API_PORT,
    )