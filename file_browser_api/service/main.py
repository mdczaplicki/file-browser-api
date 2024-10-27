from fastapi import FastAPI

from file_browser_api.browser.router import FILE_ROUTER, DIRECTORY_ROUTER

app = FastAPI(
    title="File Browser API",
    summary="Browse and edit files",
)

app.include_router(FILE_ROUTER, prefix="/file")
app.include_router(DIRECTORY_ROUTER, prefix="/directory")