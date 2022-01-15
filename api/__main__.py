import uvicorn

from .app import create_app
from .settings import deploy_settings

app = create_app()

uvicorn.run(
    "__main__:app",
    host=deploy_settings.HOST,
    port=deploy_settings.PORT,
    debug=deploy_settings.DEBUG,
    reload=deploy_settings.RELOAD,
    access_log=deploy_settings.ACCESS_LOG,
)
