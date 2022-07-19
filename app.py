import dash
import dash_bootstrap_components as dbc

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"
FA2 = "https://use.fontawesome.com/releases/v6.0.0/css/all.css"
app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.LUX, FA, FA2],
                title='AAC Insights')
