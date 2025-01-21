import pandas as pd
import numpy as np
from rich.progress import track
import time

def output():
  # np.random.seed(42)
  # df = pd.DataFrame({
  #   'ID': range(1, 11),
  #   'Name': [f'Item_{i}' for i in range(1, 11)],
  #   'Category': np.random.choice(['A', 'B', 'C'], size=10),
  #   'Price': np.random.randint(100, 1000, size=10),
  #   'Stock': np.random.randint(1, 100, size=10),
  #   'Rating': np.round(np.random.uniform(1, 5, size=10), 1)
  # })
  # for row in track(zip(*[df[col] for col in df.columns]), description="test progress", total=len(df)):
  #   df_row = dict(zip(df.columns, row))
  #   print(df_row)
  #   time.sleep(2)
  
  print("テスト成功じゃ！")
  
if __name__ == "__main__":
  output()