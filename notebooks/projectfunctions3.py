def PieChart1(filepath):
    import pandas as pd
    import numpy as np
    
    data1 = pd.read_csv(filepath)
    data1_clean = (
    data1
        .dropna(axis=0)
        .sort_values(by = 'yearID', ascending = True)
    )
    AwardPlayer = pd.read_csv(filepath)
    AwardPlayer_clean = (
    AwardPlayer
        .drop(['lgID','tie','notes'],axis=1)
        .dropna(axis = 0)
    )
    merged = data1_clean.merge(AwardPlayer_clean, on="playerID", how="outer")
    merged_clean = (
    merged
        .dropna(axis=0)
    )
    
    new_df = merged_clean.loc[merged_clean['awardID'].isin(['TSN All-Star','Gold Glove','Silver Slugger','Most Valuable Player ','TSN Pitcher of the Year','Cy Young Award','Rookie of the Year','TSN Fireman of the Year','TSN Player of the Year']
    )]
    
    return new_df

def PieChart2(filepath):
    import pandas as pd
    import numpy as np
    
    data1 = pd.read_csv(filepath)
    data1_clean = (
    data1
        .dropna(axis=0)
        .sort_values(by = 'yearID', ascending = True)
    )
    HallofFame = pd.read_csv(filepath)
    HallofFame_clean = (
    HallofFame
        .drop(['votedBy','needed_note','category'],axis=1)
        .dropna(axis = 0)
    )
    merged = data1_clean.merge(HallofFame_clean, on="playerID", how="outer")
    merged_clean = (
    merged
        .dropna(axis=0)
    )
    new_df = merged_clean.loc[merged_clean['teamID'].isin(['BRO','SLN','PIT','BSN','CHN','CIN','WS1','TEX','NYA'])]
    
    return new_df2

def PieChart3(filepath):
    import pandas as pd
    import numpy as np
    
    AwardPlayer = pd.read_csv(filepath)
    AwardPlayer_clean = (
    AwardPlayer
        .drop(['lgID','tie','notes'],axis=1)
        .dropna(axis = 0)
    )
    Salaries = pd.read_csv(filepath)
    Salaries_clean = (
    Salaries
        .drop(['lgID'],axis=1)
        .dropna(axis = 0)
    )
    merged = AwardPlayer_clean.merge(Salaries_clean, on="playerID", how="outer")
    merged_clean = (
    merged
        .dropna(axis=0)
    )
    new_df = merged_clean.loc[merged_clean['awardID'].isin(['TSN Player of the Year','Pitching Triple Crown','Triple Crown','Rookie of the Year','TSN All-Star','Hutch Award','Gold Glove','World Series MVP']
    )]
    
    return new_df3

def Plotgraph1(filepath):
    import pandas as pd
    import numpy as np
    
    data1 = pd.read_csv(filepath)
    old_games = data1[data1['yearID'] < 1891]
    new_games = data1[data1['yearID'] > 2000]
    new_games = new_games.dropna().reset_index(drop=True)
    new_games.head()
    
    return new_df4