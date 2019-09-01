import pandas as pd
from bigquery import upload_outdata
import datetime

def load():

    df = pd.read_csv('tracks.csv')
    upload_outdata(df, 'main.tracks')

if __name__ == "__main__":
    load()
