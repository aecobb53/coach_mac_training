import os
import json

from datetime import datetime
from tkinter import E
from fastapi import FastAPI, Query, Request, HTTPException, Body
from fastapi.responses import HTMLResponse, ORJSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from models import (
    ResponseTypes,
    RestHeaders,
    ContextSingleton)
# from handlers import DatabaseHandler, init_logger
from handlers import init_logger
from html import project_home_page, unimplemented_page, unimplemented_dev_page

from html import (
    project_base_page,
    project_home_page,
    # project_about,
    unimplemented_page,
    broken_page,
    workouts_page,
    info_page,
)


# Can delete after done testing rest calls from different sources
from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent
from html import project_base_page


# Service Info
with open(os.path.join(os.path.dirname(os.getcwd()), 'info.json'), 'r') as jf:
    app_info = json.load(jf)
FAVICON_PATH = '../Coach-Mac-Training-Emblem.ico'
ROBOTS_PATH = 'robots.txt'


app = FastAPI(
    title=app_info['service_name'],
    description=app_info['description'],
    version=app_info['version'],
)

# Setting up CORS and who can access the API
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # db = DatabaseHandler()
    # db.create_tables()
    context = ContextSingleton()
    # context.database = db
    context.logger = init_logger()


# Root
@app.get('/', status_code=200)
@app.get('/home', status_code=200)
async def root(request: Request):
    context = ContextSingleton()
    page = await project_home_page()
    try:
        page = await project_home_page()
        return HTMLResponse(content=page)
    except Exception as e:
        context.logger.warning(f"Error generating project page: {e}")
        page = await broken_page()
        return HTMLResponse(content=page, status_code=500)

# Workouts
@app.get('/workouts', status_code=200)
async def workouts(request: Request):
    context = ContextSingleton()
    try:
        page = await workouts_page()
        return HTMLResponse(content=page)
    except Exception as e:
        context.logger.warning(f"Error generating project page: {e}")
        page = await broken_page()
        return HTMLResponse(content=page, status_code=500)

# About
@app.get('/about', status_code=200)
async def about(request: Request):
    # TODO: Add an actual About
    context = ContextSingleton()
    try:
        page = await unimplemented_page()
        return HTMLResponse(content=page)
    except Exception as e:
        context.logger.warning(f"Error generating project page: {e}")
        page = await broken_page()
        return HTMLResponse(content=page, status_code=500)

# Info
@app.get('/info', status_code=200)
@app.get('/service-info', status_code=200)
async def info(request: Request):
    context = ContextSingleton()
    try:
        info_dict = {
            'version': app_info['version']
        }
        page = await info_page(context, info_dict)
        return HTMLResponse(content=page)
    except Exception as e:
        context.logger.warning(f"Error generating project page: {e}")
        page = await broken_page()
        return HTMLResponse(content=page, status_code=500)

# Favicon
@app.get('/static/favicon.ico', include_in_schema=False)
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)

# Robots
@app.get('/static/robots.txt', include_in_schema=False)
@app.get('/robots.txt', include_in_schema=False)
async def robots():
    return FileResponse(ROBOTS_PATH)

# Emblem
@app.get('/static/emblem.ico', include_in_schema=False)
@app.get('/emblem.ico', include_in_schema=False)
async def emblem():
    return FileResponse(FAVICON_PATH)
