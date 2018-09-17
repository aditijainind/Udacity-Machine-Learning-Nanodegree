# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:49:25 2017

@author: aditi
"""


import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames

import visuals as vs

titanicData = pd.read_csv('titanic_data.csv') 

display(titanicData.head())