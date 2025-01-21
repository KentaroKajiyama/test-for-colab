from test_for_colab.output import output
import pandas as pd

def load_csv_files(file_paths):
  """
  渡されたCSVファイルのパスリストを受け取り、
  各CSVをDataFrameに変換し、ファイル名をキーとした辞書を返す。
  """
  dataframes = {}

  for file_path in file_paths:
    try:
      # ファイル名をキーとして辞書に格納（拡張子なし）
      file_name = file_path.split("/")[-1].replace(".csv", "")
      df = pd.read_csv(file_path)
      dataframes[file_name] = df
      print(f"✅ {file_name} を DataFrame に変換完了")
    except Exception as e:
      print(f"❌ {file_path} の読み込みに失敗: {e}")
  
  output()

  return dataframes