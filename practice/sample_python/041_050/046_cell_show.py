SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SHEET_ID = '1I2lByQ7i2VG_OicooQskam91vhaSivW_zA9QbGVK4Gc'
CREDENTIALS_FILE = 'credentials.json'

def prepare_credentials():
    import pickle
    import os
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    return service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SCOPES
            )

from googleapiclient.discovery import build

creds = prepare_credentials()
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

cell_range = sheet.values().get(spreadsheetId=SHEET_ID, range='A1:C2').execute()
print(cell_range.get('values'))