from typing import Any

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.datastructures import URL
from starlette.requests import Request

from app import app

templates = Jinja2Templates(directory="../templates")

def https_url_for(request: Request, name: str, **path_params: Any) -> URL:

    http_url = request.url_for(name, **path_params)
    http_url_str = str(http_url)
    # Replace 'http' with 'https'
    return http_url_str.replace("http", "https", 1)

templates.env.globals["https_url_for"] = https_url_for

app.mount("/static", StaticFiles(directory="../static"), name="static")

def render_template(name, **kwargs):
    return templates.TemplateResponse(name, kwargs)



