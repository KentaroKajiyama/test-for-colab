import sys
import pandas as pd

def main():
    args = sys.argv[1:]  # TEMPLATE_ID, CSVファイルのペアを取得
    if len(args) % 2 != 0:
        print("❌ 引数の数が正しくありません")
        return

    for i in range(0, len(args), 2):
        template_id = args[i]
        csv_path = args[i + 1]
        df = pd.read_csv(csv_path)

        print(f"\n📄 TEMPLATE_ID: {template_id}, ファイル: {csv_path}")
        print(df.head())  # 先頭5行を表示

if __name__ == "__main__":
    main()
