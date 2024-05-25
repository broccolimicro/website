#!/usr/bin/python3

from pyhtml.html import *
from common import getPOST
import gspread
from google.oauth2.service_account import Credentials

if __name__ == "__main__":
	# Path to your service account key file
	SERVICE_ACCOUNT_FILE = '/var/data/broccolimicro/sheets.json'

	# The scope for the Google Sheets API
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

	# Authenticate using the service account key file
	credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
	client = gspread.authorize(credentials)

	# The ID and range of the spreadsheet
	SPREADSHEET_ID = '1kOBHUaJfbbGvxMB5r0EH5a5racnWcZgxfBFO9tJdcDQ'
	SHEET_NAME = 'Sheet1'  # Change this to your sheet name

	# Open the spreadsheet and the specific sheet
	spreadsheet = client.open_by_key(SPREADSHEET_ID)
	sheet = spreadsheet.worksheet(SHEET_NAME)

	post = getPOST()
	if "first" in post and "last" in post and "email" in post:
		sheet.append_rows([[post["first"], post["last"], post["email"]]])
		print(Document() << [])
	else:
		print("")
