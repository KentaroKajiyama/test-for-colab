import pandas as pd
from test_for_colab.output import output
from dotenv import load_dotenv
import os

def main(INDEX=0, df_DICT=None):
  
  load_dotenv("./config/.env")
  
  print(f"INDEX: {INDEX}")
  if df_DICT:
    print("df_DICTが正しく読み込まれていません！")
  else:
    for key, value in df_DICT.items():
      df = value[key]
      print(f"df.head():{df.head()}")
  
  ENV = os.getenv("INDEX")
  
  print(f"ENV:{ENV}")
  
  output()      