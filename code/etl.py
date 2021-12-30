import pandas as pd
from itertools import combinations


def read_csv(path):
    df = pd.read_csv(path)
    
    df["Distance_To_Hydrology"] = df["Horizontal_Distance_To_Hydrology"]**2 + df["Vertical_Distance_To_Hydrology"]**2
    df["diff_roadways_and_hydrology"] = df["Horizontal_Distance_To_Roadways"] - df["Horizontal_Distance_To_Hydrology"]
    
    hillshade_columns = [
        "Hillshade_9am",
        "Hillshade_Noon",
        "Hillshade_3pm"
    ]
    df["sum_Hillshade"] = df[hillshade_columns].sum(axis=1)
    for col0, col1 in combinations(hillshade_columns, 2):
        df[f"diff_{col0}_{col1}"] = df[col0] - df[col1]
    
    wilderness_columns = [f"Wilderness_Area{i}" for i in range(1, 5)]
    df["sum_Wilderness"] = df[wilderness_columns].sum(axis=1)
    
    soil_columns = [f"Soil_Type{i}" for i in range(1, 41)]
    df["sum_Soil"] = df[soil_columns].sum(axis=1)
    
    important_soil_columns = [f"Soil_Type{i}" for i in (11, 13, 22, 23, 24, 31, 32, 33, 35, 36, 37, 38, 39, 40)]
    df["important_sum_Soil"] = df[important_soil_columns].sum(axis=1)
    
    return df


def load_train_data():
    df = read_csv('../input/train.csv')
    return df


def load_test_data():
    df = read_csv('../input/test.csv')
    return df