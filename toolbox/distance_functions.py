
import numpy as np
import pandas as pd

def minkowski_distance(df, p):
    x1, y1 = df["pickup_longitude"], df["pickup_latitude"]
    x2, y2 = df["dropoff_longitude"], df["dropoff_latitude"]
    res = df.copy()
    res["distance"] = ((abs(x2 - x1) ** p) + (abs(y2 - y1)) ** p) ** (1 / p)
    return res[["distance"]]
