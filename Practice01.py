import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Supervised Learning

cols = ["fLength", "fWidth", "fHeight", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist"]
df = pd.read_csv("magic04.data", names=cols)

df["class"] = (df["class"] == "g").astype(int)
print(df.head())

