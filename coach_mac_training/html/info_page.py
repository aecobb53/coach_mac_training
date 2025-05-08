import json

from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent
from .common import HOME_PAGE_LINK_CONTENT, DEV_HOME_PAGE_LINK_CONTENT
from datetime import datetime, timedelta
import os
from .base_page import (
    project_base_page,
    )

async def info_page(context, info_dict):
    base_doc = await project_base_page()

    page_content = Div().add_class('page-content')

    page_content.add_element(Header(level= 1, internal='Info Page'))

    page_content.add_element(Paragraph(f"""
        Server start time: {context.init_time.strftime("%Y-%m-%dT%H:%M:%S")}Z.
    """))

    page_content.add_element(Paragraph(f"""
        Server uptime: {context.server_uptime}.
    """))

    page_content.add_element(Paragraph(f"""
        Software Version: {info_dict['version']}
    """))

    if os.environ.get('LOGICAL_ENV') == 'DEV':
        page_content.add_element(Paragraph(f"""
            Environment: Development
        """))
        page_content.add_element(Paragraph(f"""
            Workers: 1
        """))
    elif os.environ.get('LOGICAL_ENV') == 'PROD':
        page_content.add_element(Paragraph(f"""
            Environment: Production
        """))
        page_content.add_element(Paragraph(f"""
            Workers: 4
        """))

    body_content = BodyContent(body_content=[page_content])

    base_doc.body_content = body_content
    return base_doc.return_document
