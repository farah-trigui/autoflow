import pandas as pd
import os

downloaded_files = os.listdir('downloads')
filename = downloaded_files[0]
filepath = os.path.join('downloads', filename)
df = pd.read_excel(filepath)

df.dropna(axis=1, how='all', inplace=True)

df = df[df['Country'].notna()]

if 'Total' in df.columns:
    df.sort_values(by='Total', ascending=False, inplace=True)

columns_to_keep = ['Country', 'Total', 'Rank', 'Year']
df = df[columns_to_keep]

output_path = os.path.join('data', 'cleaned_fsi.csv')
df.to_csv(output_path, index=False)
