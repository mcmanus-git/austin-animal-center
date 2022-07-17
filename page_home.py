from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to home page!')

icon_card = dbc.Card(
    dbc.CardBody(
        [
            html.I(className="fas fa-spinner fa-spin fa-2x"),
            html.I(className="fas fa-dog fa-2x"),
            html.I(className="fas fa-cat fa-2x"),
        ]
    )
)

tab1_content = html.Div(
    [html.Br(),
     dbc.Card(
         dbc.CardBody(
             [
                 html.Br(),
                 html.H4("Check out some dogs"),
                 dcc.Markdown("You can look by category by clicking a link below or see a list of my "
                              "coolest portfolio projects [here](/portfolio-highlights)."
                              ),
                 # html.Br(),
                 # cards_row_1,
                 # html.Br(),
                 # cards_row_2,
                 # html.Br()
             ]
         )
     )
     ]
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            # create_tab_resume()
            'Kitties stuff here'
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("My Most Recent Blog Posts"),
            dcc.Markdown("For a full list of my previous blog posts, check out the [blog page](/blog)."),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        # dbc.Tab(tab1_content, label="Portfolio"),
        dbc.Tab(tab1_content, labelClassName="fas fa-dog fa-4x"),
        dbc.Tab(tab2_content, labelClassName="fas fa-cat fa-4x"),
        dbc.Tab(tab3_content, labelClassName="fas fa-spinner fa-spin fa-2x"),
    ]
)


def create_page_home():
    layout = html.Div([
        nav,
        html.Div(
            [
                header,
                icon_card,
                tabs
            ], style={'margin': '5% 5% 5% 5%'}
        )
    ])
    return layout
