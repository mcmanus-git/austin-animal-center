import pandas as pd
import os


def get_intake_outcomes_data():
    intakes = pd.read_feather(f'{os.getcwd()}/data/full/Austin_Animal_Center_Intakes_7_17_2022.ftr')
    outcomes = pd.read_feather(f'{os.getcwd()}/data/full/Austin_Animal_Center_Outcomes_7_17_2022.ftr')

    return intakes, outcomes
