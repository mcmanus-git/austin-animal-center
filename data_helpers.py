import pandas as pd
import os


def get_intake_outcomes_data():
    intakes = pd.read_csv(f'{os.getcwd()}/data/full/Austin_Animal_Center_Intakes_7_17_2022.csv')
    intakes['Date'] = pd.to_datetime(pd.to_datetime(intakes['DateTime']).dt.strftime('%Y-%m-%d'))

    outcomes = pd.read_csv(f'{os.getcwd()}/data/full/Austin_Animal_Center_Outcomes_7_17_2022.csv')
    outcomes['Date'] = pd.to_datetime(pd.to_datetime(outcomes['DateTime']).dt.strftime('%Y-%m-%d'))

    return intakes, outcomes
