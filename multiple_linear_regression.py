import numpy as np
import pandas as pd

df = pd.read_csv('housing_data .csv')

df.corr()['total_rooms']