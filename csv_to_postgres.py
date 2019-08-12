#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob
from sqlalchemy import create_engine

marketing_df = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/marketing_*.csv')], ignore_index = True)
user_df = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/user_*.csv')], ignore_index = True)

# Connect to database 
engine = create_engine("postgresql://postgres:password@localhost/postgres")
con = engine.connect()

## makes tables out of dataframes, this is amazing
marketing_df.to_sql('marketing', con=engine)
user_df.to_sql('users', con=engine)
con.close()