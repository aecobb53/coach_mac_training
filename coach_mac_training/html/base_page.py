import os

from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent
from .common import HOME_PAGE_LINK_CONTENT, DEV_HOME_PAGE_LINK_CONTENT
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


PAGE_STYLES = [
    # StyleTag(name='*', internal=f"""
    #     margin: 0px;
    #     padding: 0px;
    #     font-family: Tahoma;
    # """),
    StyleTag(name='body', internal=f"""
        margin: 0px;
        padding: 0px;
        font-family: Tahoma;
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR_ONE};
    """),
    StyleTag(name='.page-content', internal=f"""
        display: block;
        color: {TEXT_COLOR_ONE};
        margin: 10px;
    """),

]
FILTER_STYLES = [
    StyleTag(name='.filter-checkbox-input', internal=f"""
        margin: 0;
    """),
    StyleTag(name='.big-button', internal=f"""
        margin: 20px;
        padding: 5px;
        font-size: 120%;
        font-weight: bold;
        text-decoration: underline;
    """),
    StyleTag(name='.small-button', internal=f"""
        margin: 5px;
        padding: 5px;
        font-size: 100%;
        font-weight: bold;
    """),
    StyleTag(name='.submit-button', internal=f"""
        background-color: {SECONDARY_SELECTION_COLOR};
        color: {TEXT_COLOR_TWO};
    """),

    StyleTag(name='.pagination-div', internal=f"""
        display: inline-block;
        font-size: 300%;
        color: {TEXT_COLOR_ONE};
        margin: 10px;
        text-decoration: none;
        text-align: center;
        width: 100%;
    """),
    StyleTag(name='.pagination-div button', internal=f"""
        border-radius: 5px;
        margin: 5px;
        padding: 5px;
        text-decoration: none;
        font-size: 70%;
    """),
    StyleTag(name='.pagination-div button.active', internal=f"""
        color: {TEXT_COLOR_TWO};
        background-color: {SECONDARY_SELECTION_COLOR};
    """),





    StyleTag(name='.button-activated', internal=f"""
        background-color: {SECONDARY_SELECTION_COLOR};
    """),
    StyleTag(name='.button-deactivated', internal=f"""
        background-color: {PRIMARY_SELECTION_COLOR};
    """),
    StyleTag(name='.button-emulator-format', internal=f"""
        border: 2px solid black;
        color: {TEXT_COLOR_ONE};
    """),




]
TABLE_STYLES = [
        StyleTag(name='table', internal=f"""
            // width: 100%;
            height: 100%;
            border: 5px solid black;
            text-align: center;
        """),
        StyleTag(name='thead', internal=f"""
            // width: 100%;
            fontWeight: bold;
            padding: 5px;
            color: {TEXT_COLOR_ONE};
        """),
        StyleTag(name='tbody', internal=f"""
            // width: 100%;
            height: 100%;
            border: 5px solid black;
            color: {TEXT_COLOR_ONE};
        """),
        StyleTag(name='tr', internal=f"""
            padding: 5px;
        """),
        StyleTag(name='td', internal=f"""
            padding: 5px 25px;
        """),
        StyleTag(name='td a', internal=f"""
            color: {TEXT_COLOR_TWO};
        """),
        StyleTag(name='.even-row', internal=f"""
            background-color: {TABLE_BACKGROUND_COLOR_ONE};
            color: {TABLE_COLOR_ONE};
        """),
        StyleTag(name='.odd-row', internal=f"""
            background-color: {TABLE_BACKGROUND_COLOR_TWO};
            color: {TABLE_COLOR_ONE};
        """),
        StyleTag(name='.record-row', internal=f"""
            background-color: {PRIMARY_SELECTION_COLOR};
            color: {TEXT_COLOR_ONE};
            font-style: italic;
        """),
        StyleTag(name='.mens-format', internal=f"""
            color: {MEN_COLOR};
        """),
        StyleTag(name='.womens-format', internal=f"""
            color: {WOMEN_COLOR};
        """),



        StyleTag(name='.odd-content-format', internal=f"""
            background-color: {CONTENT_COLOR_ONE};
            padding: 30px;
            margin: 20px;
        """),
        StyleTag(name='.even-content-format', internal=f"""
            background-color: {CONTENT_COLOR_TWO};
            padding: 20px;
            margin: 20px;
        """),
]


CSV_STYLES = [
        StyleTag(name='.csv-input', internal=f"""
            width: 100%;
            height: 100%;
            padding: 0;
            margin: 0;
            color: {TEXT_COLOR_ONE};
            background-color: {BACKGROUND_COLOR};
        """),
        StyleTag(name='td', internal=f"""
            padding: 0;
            margin: 0;
        """),
        StyleTag(name='.data-div', internal=f"""
            padding: 10px 10px;
            margin: 10px 10px;
        """),
        StyleTag(name='.data-div span', internal=f"""
            padding: 0;
            margin: 0;
        """),
        StyleTag(name='.data-div label', internal=f"""
            font-size: 200%;
        """),
        StyleTag(name='.data-div input', internal=f"""
            font-size: 200%;
        """),





        StyleTag(name='.meet-table', internal=f"""
            padding: 0;
            margin: 0;
            display: block;
        """),
        StyleTag(name='.meet-row', internal=f"""
            padding: 0;
            margin: 0;
            display: inline-block;
            width: 100%;
            height: 100%;
            border: 1px solid black;
        """),
        StyleTag(name='.meet-item', internal=f"""
            padding: 0;
            margin: 0;
            display: inline-block;
            height: 100%;
        """),
        StyleTag(name='.meet-multiline-item', internal=f"""
            padding: 0;
            margin: 0;
            display: block;
        """),

        # StyleTag(name='.col-width', internal=f"""
        #     width : 100px
        # """),
        StyleTag(name='.col-width-time input, .col-width-time div', internal=f"""
            width: 55px;
        """),
        StyleTag(name='.col-width-event input, .col-width-event div', internal=f"""
            width: 135px;
        """),
        StyleTag(name='.col-width-athlete input, .col-width-athlete div', internal=f"""
            width: 170px;
        """),
        StyleTag(name='.col-width-heat input, .col-width-heat div', internal=f"""
            width: 130px;
        """),
        StyleTag(name='.col-width-seed input, .col-width-seed div', internal=f"""
            width: 65px;
        """),
        StyleTag(name='.col-width-result input, .col-width-result div', internal=f"""
            width: 65px;
        """),
        StyleTag(name='.col-width-place input, .col-width-place div', internal=f"""
            width: 35px;
        """),
        StyleTag(name='.col-width-pr div', internal=f"""
            width: 65px;
            height: 22px;
            padding: 0px 10px;
        """),
        StyleTag(name='.col-width-points div', internal=f"""
            width: 35px;
            height: 22px;
            padding: 0px 10px;
        """),
        StyleTag(name='.col-width-button button, .col-width-button div', internal=f"""
            margin: 0px;
            padding 0px;
        """),

        StyleTag(name='.validated', internal=f"""
            background-color: #a5ffa5;
        """),
        StyleTag(name='.partially-validated', internal=f"""
            background-color: yellow;
        """),
]

HOME_PAGE_STYLES = [
    StyleTag(name='.home-page-content', internal=f"""
        color: {TEXT_COLOR_ONE};
        margin: 10px;
        padding: 0;
    """),
    StyleTag(name='.home-page-content h1', internal=f"""
        margin: 0;
        padding: 20px 40px;
    """),
    StyleTag(name='.page-group-div', internal=f"""
        color: {TEXT_COLOR_ONE};
        margin: 0;
        padding: 0;
        display: inline;
    """),

    StyleTag(name='.page-div', internal=f"""
        background-color: {PRIMARY_SELECTION_COLOR};
        margin: 20px;
        padding: 0;
        border: 3px solid black;
        border-radius: 15px;
        -moz-border-radius: 15px;
        height: 100px;
        width: 400px;
        display: inline-block;
        vertical-align: top;
    """),

    StyleTag(name='.page-link', internal=f"""
        color: {TEXT_COLOR_ONE};
        text-decoration: none;
    """),


    StyleTag(name='.page-header', internal=f"""
        margin: 10px;
        padding: 0;
        text-align: center;
    """),
    StyleTag(name='.page-paragraph', internal=f"""
        margin: 10px;
        padding: 0;
        text-align: center;
    """),


    StyleTag(name='.page-link h2', internal=f"""
        margin: 15px;
        padding: 0;
    """),
    StyleTag(name='.page-link p', internal=f"""
        margin: 0;
        padding: 0;
    """),
]

"""

font-style: normal|italic|oblique|initial|inherit;

old mens
07006b
new mens
0b00ab



body text
font-family: Arial, Helvetica, sans-serif;
font-family: Tahoma, sans-serif;


background #9f9f9f
text Black

background #ffb4b4
text black

Record background
ffdda1
text black


text-align: center;










efc9ff








"""


async def project_base_page(onload_function=None):
    # Navigation
    # page_image = Image().add_style({'display': 'inline'})
    # page_image.add_src('static/emblem.ico')
    # page_name = Header(level=2, internal='Coach Mac Training').add_style({'display': 'inline'})
    # webpage_name = Span(internal=[
    #     page_image,
    #     page_name,
    #     ])
    webpage_name = Div(internal=[
        'Coach Mac Training',])
    navigation_content = NavigationContent(
        webpage_name=webpage_name,
        webpage_name_link='/',
        background_color=NAVIGATION_BACKGROUND_COLOR,
        text_color=TEXT_COLOR_TWO,
        )
    navigation_content.add_navigation_link('Workouts', '/workouts')

    if onload_function:
        doc = MyBaseDocument(
            navigation_content=navigation_content,
            document_style=PAGE_STYLES,
            onload_function=onload_function,
        )
    else:
        doc = MyBaseDocument(
            navigation_content=navigation_content,
            document_style=PAGE_STYLES,
        )
    return doc


async def project_home_page():
    base_doc = await project_base_page()

    # Body
    page_content = Div().add_class('home-page-content')

    body_image = Image()
    body_image.add_src('/static/emblem.ico')
    page_content.add_element(body_image)

    # TODO: These paragraphs need to be indented and formatted
    # TODO: Change the header names and level

    page_content.add_element(Header(level=1, internal="Summer 2025 Track and Field Training Plan"))
    page_content.add_element(Paragraph(internal="""
Coach Mac Training is a private coaching service dedicated to providing professional
coaching and development to young athletes. I also provide training, rehabilitation, and
athletic preparation for competition. I offer athletes who want to improve their fitness with
mentorship, performance enhancing techniques and guidance necessary to achieve their
desired results.
Athletes utilizing this service will learn how to properly train for their specific athletic goals
using techniques and workout plans designed for each individual athlete. The ultimate
objective is to motivate each athlete to develop an improved, healthy lifestyle and training
schedules that will lead them to a successful athletic career.
What I offer is to prepare the athletes for their careers in athletics as well as to reach their
goals in being the best athlete they can be for their respective teams and sport.
    """))

    page_content.add_element(Header(level=1, internal="Mission"))
    page_content.add_element(Paragraph(internal="""
To encourage, teach, and prepare young athletes to maximize their athletic potential
working to develop, improve, and introduce mental toughness and life skills to ultimately
live productive and healthy lives.
    """))

    page_content.add_element(Header(level=1, internal="Vision"))
    page_content.add_element(Paragraph(internal="""
We strive to connect and build athletes up through dynamic coaching and training. We are
always improving new techniques and training practice with the ultimate goal of helping
athletes be the best version of themselves in their athletic endeavors. We are driven by our
passion in coaching and our strive to make a difference.
    """))

    body_content = BodyContent(
        body_content=[page_content],
        body_styles=PAGE_STYLES,)
    for style in HOME_PAGE_STYLES:
        body_content.add_body_styles(style)

    base_doc.body_content = body_content

    phtml_doc = base_doc.return_phtml
    phtml_doc.add_favicon('favicon.ico')

    return phtml_doc.return_document

async def broken_page():
    base_doc = await project_base_page()

    # Body
    page_content = Div().add_class('home-page-content')
    page_content.add_element(Header(level=1, internal="Page broken, check back later"))


    body_content = BodyContent(
        body_content=[page_content],
        body_styles=PAGE_STYLES,)

    base_doc.body_content = body_content

    return base_doc.return_document


async def project_about():
    base_doc = await project_base_page()

    # Body
    page_content = Div().add_class('home-page-content')
    page_content.add_element(
        Paragraph(internal=f"""
        This project is pretty simple in that it tracks data from Milesplit.com so that other coaches and athletes can 
        view progress or stats as the season goes on. It is also used as a full stack project for employment purposes.
        """)
    ).add_style({'font-size': '2.0em', 'margin': '30px', 'padding': '0'})

    body_content = BodyContent(body_content=[page_content])

    base_doc.body_content = body_content

    return base_doc.return_document

# DEV
async def project_dev_base_page():
    # Navigation
    navigation_content = NavigationContent(
        webpage_name="Fairview Track Results - Development Pages",
        webpage_name_link='/html/dev',
        background_color=NAVIGATION_BACKGROUND_COLOR,
        text_color=TEXT_COLOR_TWO,
        )
    navigation_content.add_navigation_link('Dev Home', '/html/dev/home')

    doc = MyBaseDocument(
        navigation_content=navigation_content,
        document_style=PAGE_STYLES
    )
    return doc

async def project_dev_home_page():
    base_doc = await project_dev_base_page()

    # Body
    page_content = Div().add_class('home-page-content')

    for grouping, pages in DEV_HOME_PAGE_LINK_CONTENT.items():
        grouping_div = Div(Header(level=1, internal=grouping)).add_class('page-group-div')

        for page, details in pages.items():
            content = [
                Div(internal=Header(level=2, internal=page)).add_class('page-header'),
                Div(internal=Paragraph(internal=details['description'])).add_class('page-paragraph'),
            ]
            page_link = Link(internal=content, href=f"/html/{details['endpoint']}").add_class('page-link').add_class('page-div')
            grouping_div.add_element(page_link)
        page_content.add_element(grouping_div)

    body_styles = [
        StyleTag(name='.home-page-content', internal=f"""
            color: {TEXT_COLOR_ONE};
            margin: 10px;
            padding: 0;
        """),
        StyleTag(name='.home-page-content h1', internal=f"""
            margin: 0;
            padding: 20px 40px;
        """),
        StyleTag(name='.page-group-div', internal=f"""
            color: {TEXT_COLOR_ONE};
            margin: 0;
            padding: 0;
            display: inline;
        """),

        StyleTag(name='.page-div', internal=f"""
            background-color: {PRIMARY_SELECTION_COLOR};
            margin: 20px;
            padding: 0;
            border: 3px solid black;
            border-radius: 15px;
            -moz-border-radius: 15px;
            height: 100px;
            width: 400px;
            display: inline-block;
            vertical-align: top;
        """),

        StyleTag(name='.page-link', internal=f"""
            color: {TEXT_COLOR_ONE};
            text-decoration: none;
        """),


        StyleTag(name='.page-header', internal=f"""
            margin: 10px;
            padding: 0;
            text-align: center;
        """),
        StyleTag(name='.page-paragraph', internal=f"""
            margin: 10px;
            padding: 0;
            text-align: center;
        """),


        StyleTag(name='.page-link h2', internal=f"""
            margin: 15px;
            padding: 0;
        """),
        StyleTag(name='.page-link p', internal=f"""
            margin: 0;
            padding: 0;
        """),
    ]

    body_content = BodyContent(
        body_content=[page_content],
        body_styles=PAGE_STYLES,)
    for style in body_styles:
        body_content.add_body_styles(style)

    base_doc.body_content = body_content

    return base_doc.return_document
