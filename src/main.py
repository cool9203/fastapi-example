#! python3
# coding: utf-8

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import utils

logger = utils.get_logger(logger_name=__name__)


app = FastAPI()
import lib

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/rapidoc", response_class=HTMLResponse, include_in_schema=False)
async def rapidoc():
    """Reference: https://github.com/tiangolo/fastapi/issues/1198"""
    return f"""<!doctype html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <script
                            type="module"
                            src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"
                        ></script>
                    </head>
                    <body>
                        <rapi-doc spec-url="{app.openapi_url}"></rapi-doc>
                    </body>
                </html>
            """


async def get_openapi_url_in_route(req: Request):
    return req.app.openapi_url


@app.get("/stoplight", response_class=HTMLResponse, include_in_schema=False)
async def stoplight():
    """Reference: https://github.com/stoplightio/elements#web-component"""
    return f"""<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <title>Elements in HTML</title>
                    <!-- Embed elements Elements via Web Component -->
                    <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
                    <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
                </head>
                <body>
                    <elements-api
                    apiDescriptionUrl="{app.openapi_url}"
                    router="hash"
                    layout="sidebar"
                    />
                </body>
                </html>
            """


app.include_router(lib.fake_db.router)
app.include_router(lib.fake_user.router)

# also can use this
# import uvicorn
# uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
