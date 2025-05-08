from calendar import week
import os
from tkinter import W

from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent
from .common import HOME_PAGE_LINK_CONTENT, DEV_HOME_PAGE_LINK_CONTENT
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

workout_info = [
    {
        "date": "Mon Jun 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jun 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jun 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jun 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jun 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jun 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jun 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jun 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jun 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jun 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jun 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jun 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jun 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jun 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jun 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jun 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jun 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jun 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jun 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jun 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jun 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jun 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jul 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jul 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jul 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jul 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jul 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jul 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jul 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jul 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jul 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jul 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jul 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jul 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jul 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jul 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jul 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jul 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jul 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jul 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jul 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jul 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jul 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jul 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jul 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jul 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Jul 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Jul 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Jul 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Jul 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Jul 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Jul 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Jul 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Aug 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Aug 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Aug 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Aug 1",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Tue Aug 2",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Wed Aug 3",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Thu Aug 4",
        "focus": "Workout / Speed",
        "detail": ""
    },
    {
        "date": "Fri Aug 5",
        "focus": "Run / Drills",
        "detail": ""
    },
    {
        "date": "Sat Aug 6",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Sun Aug 0",
        "focus": "Off",
        "detail": ""
    },
    {
        "date": "Mon Aug 1",
        "focus": "Run / Drills",
        "detail": ""
    }
]

WORKOUT_PAGE_STYLES = [
    # StyleTag(name='.page-content', internal=f"""
    # """,)
    StyleTag(name='.week-tile', internal=f"""
    background-color: {SECONDARY_SELECTION_COLOR};
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
    border: 2px solid black;
    """),
    # StyleTag(name='.day-tile', internal=f"""
    # """),
    StyleTag(name='.day-date', internal=f"""
        display: inline-block;

    """),
    StyleTag(name='.day-focus', internal=f"""
        display: inline-block;

    """),
    StyleTag(name='.day-detail', internal=f"""
        display: inline-block;

    """),
    StyleTag(name='.week-header', internal=f"""
        padding: 2px;
        margin: 2px;
    """),
    
    # StyleTag(name='.home-page-content', internal=f"""
    #     color: {TEXT_COLOR_ONE};
    #     margin: 10px;
    #     padding: 0;
    # """),
    # StyleTag(name='.home-page-content h1', internal=f"""
    #     margin: 0;
    #     padding: 20px 40px;
    # """),
    # StyleTag(name='.page-group-div', internal=f"""
    #     color: {TEXT_COLOR_ONE};
    #     margin: 0;
    #     padding: 0;
    #     display: inline;
    # """),

    # StyleTag(name='.page-div', internal=f"""
    #     background-color: {PRIMARY_SELECTION_COLOR};
    #     margin: 20px;
    #     padding: 0;
    #     border: 3px solid black;
    #     border-radius: 15px;
    #     -moz-border-radius: 15px;
    #     height: 100px;
    #     width: 400px;
    #     display: inline-block;
    #     vertical-align: top;
    # """),

    # StyleTag(name='.page-link', internal=f"""
    #     color: {TEXT_COLOR_ONE};
    #     text-decoration: none;
    # """),


    # StyleTag(name='.page-header', internal=f"""
    #     margin: 10px;
    #     padding: 0;
    #     text-align: center;
    # """),
    # StyleTag(name='.page-paragraph', internal=f"""
    #     margin: 10px;
    #     padding: 0;
    #     text-align: center;
    # """),


    # StyleTag(name='.page-link h2', internal=f"""
    #     margin: 15px;
    #     padding: 0;
    # """),
    # StyleTag(name='.page-link p', internal=f"""
    #     margin: 0;
    #     padding: 0;
    # """),
]



async def workouts_page(onload_function=None):
    base_doc = await project_base_page()

    page_content = Div().add_class('page-content')

    week_tile = Div().add_class('week-tile')
    week_counter = 1
    for day in workout_info:
        day_tile = Div().add_class('day-tile')
        if day['date'].startswith('Mon'):
            page_content.add_element(week_tile)
            week_tile = Div().add_class('week-tile')
            week_tile.add_element(Header(level=3, internal=f"Week {week_counter}").add_class('week-header'))
            week_counter += 1
        day_tile.add_element(Div(day['date']).add_class('day-date'))
        day_tile.add_element(Div(day['focus']).add_class('day-focus'))
        day_tile.add_element(Div(day['detail']).add_class('day-detail'))
        week_tile.add_element(day_tile)

        # Switch to a table
    




    body_content = BodyContent(body_content=[page_content])

    # # Styles
    # for style in PAGE_STYLES:
    #     body_content.add_body_styles(style)
    # for style in FILTER_STYLES:
    #     body_content.add_body_styles(style)
    for style in WORKOUT_PAGE_STYLES:
        body_content.add_body_styles(style)

    base_doc.body_content = body_content
    return base_doc.return_document
