import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def aac_color(color_string):
    aac_color_dict = {'green': '#3AB02C',
                      'red': '#D23137',
                      'yellow': '#FFA708',
                      'orange': '#F89521',
                      'purple': '#211552',
                      'blue': '#187FA3',
                      'black': '#1E1E1E'
                      }

    return aac_color_dict[color_string.lower()]


def create_intake_animal_type_count_hbar(intakes, aac_color):
    earliest_year = pd.to_datetime(intakes['DateTime']).dt.year.min()
    fig = px.bar(intakes['Animal Type'].value_counts().reset_index().sort_values('Animal Type', ascending=True),
                 x='Animal Type',
                 y='index',
                 template='plotly_white',
                 orientation='h',
                 labels={'Animal Type': 'Number of Animals', 'index': ''},

                 )

    fig.update_traces(marker_color=aac_color)
    fig.update_layout(title_text=f'Number of Animals Given Shelter Since {earliest_year}', title_x=0.5)
    return fig
