import uvicorn

from api.app import create_app
from api.settings import deploy_settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=deploy_settings.HOST,
        port=deploy_settings.PORT,
        debug=deploy_settings.DEBUG,
        reload=deploy_settings.RELOAD,
        access_log=deploy_settings.ACCESS_LOG,
    )
