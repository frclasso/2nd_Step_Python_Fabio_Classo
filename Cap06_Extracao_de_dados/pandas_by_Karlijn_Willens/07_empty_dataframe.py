#!/usr/bin/env python3

import pandas as pd
import numpy as np

df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=['A'])
print(df)