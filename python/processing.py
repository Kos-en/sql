from sqlalchemy import create_engine
import pandas as pd

# Establish the connection
engine = create_engine('postgresql://postgres:3884@localhost:5432/Tableau')

# Define your queries and corresponding file names
queries = [
    
    {
        'query': """
        SELECT
            state,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS median_house_price
        FROM
            data_project
        GROUP BY
            state;
        """,
        'file_name': '/Users/joe/Desktop/sql/data/Median_Prices.xlsx'
    },
    
    {
        'query': """
        SELECT
            state,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY house_size) AS median_house_size
        FROM
            data_project
        GROUP BY
            state
        ORDER BY
            median_house_size DESC
        """,
        'file_name': '/Users/joe/Desktop/sql/data/Top_10_Largest_Median_House_Sizes.xlsx'
    },
    
    {
        'query': """
        SELECT
            state,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY acre_lot) AS median_land_size
        FROM
            data_project
        GROUP BY
            state
        ORDER BY
            median_land_size DESC
        """,
        'file_name': '/Users/joe/Desktop/sql/data/Top_10_Largest_Median_Land_Sizes.xlsx'
    },

    {
        'query': """
        SELECT
            state,
            COUNT(*) AS houses_sold
        FROM
            data_project
        WHERE
            status = 'sold'
        GROUP BY
            state
        ORDER BY
            houses_sold DESC;
        """,
        'file_name': '/Users/joe/Desktop/sql/data/States_With_Highest_Sold_Houses.xlsx'
    },
]

# Function to execute multiple queries and save each result to an Excel file
def execute_queries_and_save(queries, engine):
    for q in queries:
        df = pd.read_sql_query(q['query'], engine)
        df.to_excel(q['file_name'], index=False)

# Call the function with the list of queries and the database engine
execute_queries_and_save(queries, engine)

