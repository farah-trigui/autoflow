import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("AutoFlow FSI Report").sheet1


df = pd.read_csv('data/cleaned_fsi.csv')
sheet.clear()

sheet.update([df.columns.values.tolist()] + df.values.tolist())
