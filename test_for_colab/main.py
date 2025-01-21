import pandas as pd
from test_for_colab.output import output
from dotenv import load_dotenv
import os
import sys
from test_for_colab.load_csv import load_csv_files


def main():
  # `sys.argv[1:]` で渡されたすべてのCSVファイルのパスを取得
  csv_files = sys.argv[1:]
  if not csv_files:
    print("⚠️ CSVファイルが指定されていません")
    return

  print(f"📂 処理対象のCSVファイル: {csv_files}")

  # CSVをDataFrameに変換
  data_dict = load_csv_files(csv_files)

  # 確認用: 各DataFrameの情報を表示
  for file_name, df in data_dict.items():
    print(f"\n📄 {file_name}:")
    print(df.info())  # DataFrameの情報を表示
    print(df.head())  # 最初の5行を表示
  
  load_dotenv("./config/.env")
  
  ENV = os.getenv("INDEX")
  
  print(f"ENV:{ENV}")
  
  output()

if __name__ == "__main__":
  main()
