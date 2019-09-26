import pandas as pd
from bigquery import upload_outdata
import datetime
import absl
from absl import app
from absl import flags
from satellite import get_img
from storage import upload

FLAGS = flags.FLAGS
flags.DEFINE_enum('job', 'bq', ['bq', 'img'], 'which job to run')
flags.DEFINE_string('apikey', 'NA', 'google maps API key')

def load(df):
    upload_outdata(df, 'main.tracks')

def gen(df):
    for idx, row in df.iterrows():
        if row['code'] == 66:
            (image_name, image_file) = get_img(row, FLAGS.apikey)
            result = upload('trav.finsyn.se', f'tracks/{image_name}.jpg', image_file)
            print(result)

   
jobs = {
    'bq': load,
    'img': gen
}

def main(argv):
    df = pd.read_csv('tracks.csv')
    return jobs[FLAGS.job](df)

if __name__ == "__main__":
    app.run(main)
