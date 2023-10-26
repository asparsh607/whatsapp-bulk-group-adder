import pandas as pd
def csv_to_string(csv_path: str)-> str:
    df = pd.read_csv(csv_path)
    df = df['name'].to_numpy().tolist()
    ans = ''
    for items in df:
        ans += items
        ans += ' '
    return ans + ' '