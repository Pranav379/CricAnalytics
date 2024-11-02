
import pandas as pd


df = pd.read_csv("C:/Users/ananth/PycharmProjects/pythonProject/ipl-hawkeye-data.csv")


def calculate_10_ball_sr(df, batter_name):
    batter_data = df[df['bat'] == batter_name]
    if 'batruns' not in batter_data.columns:
        return "Column 'batruns' not found in data."
    
    first_10 = batter_data.head(10)

    total_runs = first_10['batruns'].sum()

    if len(first_10) < 10:
        return None
    else:
        strike = (total_runs/10)*100
        return strike
    

batter_name = input("Enter a batter's name (must be in the format: Firstname Lastname): ")
strike = calculate_10_ball_sr(df, batter_name)
print(f'10-ball SR for {batter_name}: {strike}')
