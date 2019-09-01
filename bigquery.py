from google.oauth2 import service_account
import pandas_gbq
import pandas as pd
import numpy as np
from jinjasql import JinjaSql

bq_schema = [
    {
        "name": "code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "name", 
        "type": "STRING",
        "mode": "REQUIRED"
    }, 
    {
        "name": "symbol",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "length",
        "type": "INTEGER",
        "mode": "REQUIRED"
    },
    {
        "name": "width_2140",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "length_homestretch",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "is_openstretch",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "is_angledwing",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    }
]

projectid = 'travtech'

def __query_from_file(filename):
    with open(filename, 'r') as file:
        query=file.read()
    return query

def upload_outdata(df, name):
    print(df)
    pandas_gbq.to_gbq(
        df,
        name,
        project_id=projectid,
        table_schema=bq_schema,
        if_exists='replace'
    )
