import json

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

with open('../etc/workout_plan.json', 'r') as jf:
    workout_plan = json.load(jf)

WORKOUT_PAGE_STYLES = [
    # StyleTag(name='.page-content', internal=f"""
    # """,)
    StyleTag(name='.week-tile', internal=f"""
    background-color: {CONTENT_COLOR_ONE};
    padding: 10px;
    margin: 10px;
    border-radius: 15px;
    border: 2px solid black;
    """),
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
    StyleTag(name='.week-table', internal=f"""
        padding: 2px;
        margin: 2px;
    """),

    StyleTag(name='.table-data', internal=f"""
        margin: 2px;
        // border: 2px solid black;
    """),
    StyleTag(name='.table-data-date', internal=f"""
        padding: 2px 10px;
    """),
    StyleTag(name='.table-data-focus', internal=f"""
        padding: 2px 10px;
    """),
    StyleTag(name='.table-data-detail', internal=f"""
        padding: 2px 50px;
    """),
]

def create_table_object(columns):
    week_table = Table().add_class('week-table')
    header_row = TableRow().add_class('odd-row')
    for column_name, column_options in columns.items():
        header_item = TableHeader(internal=column_name)
        header_row.add_element(header_item)
    week_table.add_element(header_row)
    return week_table


async def workouts_page(onload_function=None):
    base_doc = await project_base_page()

    page_content = Div().add_class('page-content')

    workout_expectations = Div().add_class('workout-expectations')
    workout_expectations.add_element(Header(level=2, internal='Summer Focus'))
    workout_expectations.add_element(Paragraph(internal="""
We are here to take the foundations of the season and improve so we can try to make state this next season. We want to focus on the following:
    """))

    workout_expectations.add_element(Paragraph(internal='BUY IN - We want to you buy all the way in. We are here for you to improve but it has to start with you and a hunger.'))
    workout_expectations.add_element(Paragraph(internal='HONE YOUR BODY - We want to improve your speed, strength, and power endurance.'))
    workout_expectations.add_element(Paragraph(internal='BUILD A TEAM - We want to have team comradery and foster team spirit.'))
    workout_expectations.add_element(Paragraph(internal='EXAMPLE - example'))
    workout_expectations.add_element(Paragraph(internal='EXAMPLE - example'))
    workout_expectations.add_element(Paragraph(internal="""
Every practice will start with team warmups. This is to get your body ready for the day. The workouts will vary for different athletes. At the end of the workout all athletes will come back together for team stretching. This is important for building a cohesive team.
"""))
    page_content.add_element(workout_expectations)

    week_table_columns = {
        'Date': {},
        'Focus': {},
        'Detail': {},
    }


    for week_index, week in enumerate(workout_plan):
        week_tile = Div().add_class('week-tile')
        week_tile.add_element(Header(level=3, internal=week['tile_header']).add_class('week-header'))
        if week.get('tile_info_1'):
            week_tile.add_element(Paragraph(internal=week['tile_info_1']).add_class('week-info-1'))
        week_table = create_table_object(week_table_columns)
        for day_index, day in enumerate(week['day_data']):
            if day_index % 2 == 1:
                data_row = TableRow().add_class('odd-row')
            if day_index % 2 == 0:
                data_row = TableRow().add_class('even-row')
            data_data = TableData(internal=day['date']).add_class('table-data').add_class('table-data-date')
            data_row.add_element(data_data)
            data_data = TableData(internal=day['plan']).add_class('table-data').add_class('table-data-focus')
            data_row.add_element(data_data)
            data_data = TableData(internal=day['detail']).add_class('table-data').add_class('table-data-detail')
            data_row.add_element(data_data)
            week_table.add_element(data_row)
        week_tile.add_element(week_table)
        if week.get('tile_info_2'):
            week_tile.add_element(Paragraph(internal=week['tile_info_2']).add_class('week-info-2'))
        page_content.add_element(week_tile)

    body_content = BodyContent(body_content=[page_content])

    # Styles
    for style in TABLE_STYLES:
        body_content.add_body_styles(style)
    for style in WORKOUT_PAGE_STYLES:
        body_content.add_body_styles(style)

    base_doc.body_content = body_content
    return base_doc.return_document
