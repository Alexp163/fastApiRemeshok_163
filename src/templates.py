from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import app

templates = Jinja2Templates(directory="../templates")

app.mount("/static", StaticFiles(directory="../static"), name="static")

def render_template(name, **kwargs):
    return templates.TemplateResponse(name, kwargs)
