import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Graph1(filepath):
    data1 = pd.read_csv(filepath)
    data1_clean = (data1
                .dropna(axis=0)
                .sort_values(by = "city", ascending = True)
               )