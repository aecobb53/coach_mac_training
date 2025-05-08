import json

from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent
from .common import HOME_PAGE_LINK_CONTENT, DEV_HOME_PAGE_LINK_CONTENT
from datetime import datetime, timedelta
import os
from .base_page import (
    project_base_page,
    # BACKGROUND_COLOR,
    # SECONDARY_COLOR,
    # ACCENT_COLOR,
    # TEXT_COLOR_1,
    # TEXT_COLOR_2,
    # ROW_BACKGROUND_COLOR_1,
    # ROW_BACKGROUND_COLOR_2,
    PAGE_STYLES,
    FILTER_STYLES,
    TABLE_STYLES,
    )

# from .env import (
#     SEASON_YEAR,
#     BACKGROUND_COLOR,
#     SECONDARY_COLOR,
#     ACCENT_COLOR,
#     TEXT_COLOR_ONE,
#     TEXT_COLOR_TWO,
#     ROW_BACKGROUND_COLOR_1,
#     ROW_BACKGROUND_COLOR_2,
# )
from .env import (
    SEASON_YEAR,
#     COLOR_ONE,
#     COLOR_TWO,
#     COLOR_THREE,
#     COLOR_FOUR,
#     COLOR_FIVE,
)
from .env import (
    BACKGROUND_COLOR,
    WHITE_COLOR,
    BLACK_COLOR,
    MEN_COLOR,
    WOMEN_COLOR,
)
from .env import (
    BODY_BACKGROUND_COLOR,
    NAVIGATION_BACKGROUND_COLOR,
    PRIMARY_SELECTION_COLOR,
    SECONDARY_SELECTION_COLOR,
    TABLE_BACKGROUND_COLOR_ONE,
    TABLE_BACKGROUND_COLOR_TWO,
    TABLE_COLOR_ONE,
    CONTENT_COLOR_ONE,
    CONTENT_COLOR_TWO,
    TEXT_COLOR_ONE,
    TEXT_COLOR_TWO,
)



async def info_page(context, info_dict):
    base_doc = await project_base_page()

    page_content = Div().add_class('page-content')

    page_content.add_element(Header(level= 1, internal='Info Page'))

    page_content.add_element(Paragraph(f"""
        Server start time: {context.init_time.strftime("%Y-%m-%d %H:%M:%S")}.
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
