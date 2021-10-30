import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Still need to add docstrings to these functions

def batting_load_and_process(file_path):
    batting_clean = (
                pd.read_csv(file_path)
                .fillna(0)
                .assign(
                    PA = lambda x: x["AB"] + x["BB"] + x["HBP"] + x["SH"] + x["SF"]
                )
        )
    bat_clean_year = (
                batting_clean.groupby("yearID").sum()
                .drop(["stint", "SH", "SF", "G"], axis = 1)
                .assign(
                    BA = lambda x: x['H'] / x['AB'],
                    OBP = lambda x: (x['H'] + x['BB'] + x['HBP']) / x['PA'],
                    SLG = lambda x: ((x['H'] - x['2B'] - x['3B'] - x['HR']) + 2 * x['2B'] + 3 * x['3B'] + 4 * x['HR']) / x['AB'],
                    OPS = lambda x: x['OBP'] + x["SLG"]
                )
        )
    return bat_clean_year


def pitching_load_and_process(file_path):
    pitching_clean = (
                pd.read_csv('../data/raw/Pitching.csv')
                .fillna(0)
        )
    pitch_clean_year = (
            pitching_clean.groupby('yearID').sum()
            .drop(["stint", "BK", "GF", "SH", "SF", "GIDP", "BAOpp", "ERA", "W", "L", "G", "GS", "BFP"], axis = 1)
            .assign(
                ERA = lambda x: (9 * x['ER']) / (x['IPouts'] / 3)
            )
        )
    return pitch_clean_year


def merge_batting_pitching(bat, pitch):
    diff_cols = pitch.columns.difference(bat.columns)
    data_clean = pd.merge(bat, pitch[diff_cols], on = ['yearID'])
    return data_clean