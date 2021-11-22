import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Graph1(filepath):
    
    data1 = pd.read_csv(filepath)
    data1_clean = (data1
                .dropna(axis=0)
                .sort_values(by = "city", ascending = True)
                .rename({'park.name': "Park Name", 'park.alias': "Park Alias", 'city': "City", 'state': "State"}, axis = 1)
                .reset_index()
                .drop(['index'], axis = 1)
                .drop(["Country"], axis = 1)
               )
    
    labels = ['OH', 'CA', 'IL', 'NY', 'PA', 'MA', 'MO', 'MI', 'IN', 'TX', 'QC', 'MD', 'IA', 'FL', 'CT', 'AZ', 'WA', 'ON', 'DC']
    
    new_df = data1_clean.loc[data1_clean['State'].isin(['OH', 'CA', 'IL', 'NY', 'PA', 'MA', 'MO', 'MI', 'IN', 'TX', 'QC', 'MD','IA','FL', 'CT', 'AZ', 'WA', 'ON', 'DC'])]
    
    return new_df

def Graph2(filepath):
    
    fielding = pd.read_csv(filepath)
    
    fielding1_clean = (fielding
                .sort_values(by = "G", ascending = False)
                [fielding["yearID"] > 1999]
                .drop(["stint", "WP", "GS", "ZR", "lgID", "E", "DP", "InnOuts", "PO", "A", "PB", "SB", "CS", "yearID", "POS"], axis =1)
                .rename({'playerID': "Player ID", 'yearID': "Year", 'teamID': "Team", 'G': "Games Played"}, axis = 1)
                .reset_index().drop(['index'], axis = 1)
                .dropna(axis = 0)
                [fielding["Games Played"] > 150]
             )
    
    labels = ['PHI', 'SEA', 'ATL', 'BAL', 'LAN', 'NYA', 'CHN', 'KCA', 'OAK', 'FLO', 'COL', 'TEX', 'MIL', 'CIN', 'ARI', 'SDN', 'HOU', 'TOR', 'CHA', 'DET', 'BOS', 'WAS', 'PIT', 'SLN', 'NYN', 'CLE', 'MON', 'SFN', 'ANA', 'LAA', 'MIA', 'TBA', 'MIN']
    
     Team_clean = fielding1_clean.loc[fielding1_clean['Team'].isin(['PHI', 'SEA', 'ATL', 'BAL', 'LAN', 'NYA', 'CHN', 'KCA', 'OAK', 'FLO', 'COL', 'TEX', 'MIL', 'CIN', 'ARI', 'SDN', 'HOU', 'TOR', 'CHA', 'DET', 'BOS', 'WAS', 'PIT', 'SLN', 'NYN', 'CLE', 'MON', 'SFN', 'ANA', 'LAA', 'MIA', 'TBA', 'MIN']
)]
        return fielding1_clean
    
def Graph3(filepath):
    
    fielding2_clean = (fielding
                [fielding["yearID"] > 1999]
                .sort_values(by = "PO", ascending = False)
                .drop(["stint","SB","teamID",'yearID',"WP","GS","PB","WP","SB","CS","ZR","A","E","DP","InnOuts","G","lgID"], axis = 1)
                .rename({'playerID': "Player ID", 'yearID': "Year", 'lgID': "League", 'G': "Games Played"}, axis = 1)
                .reset_index()
                .drop(['index'], axis = 1)
                [fieldingSS2_clean["PO"] > 0]
                       
             )
    
    return fielding2_clean