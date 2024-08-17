import pandas as pd
from sqlalchemy import create_engine

# Read Parquet file into DataFrame
df_loaded = pd.read_parquet('/Users/joe/Desktop/sql/data/cleaned_data.parquet', engine='fastparquet')

# Database connection parameters
engine = create_engine('postgresql://postgres:3884@localhost:5432/Tableau')

# Save DataFrame to SQL
df_loaded.to_sql('data_project', engine, if_exists='replace', index=False)
