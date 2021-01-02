#!/usr/bin/env python

import os
import logging
from flask import Flask
from flask import request
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('tracking')

# Get sheets id from environment variables

GOOGLE_SHEETS_ID = "1DnV0dNazOS51bCMnAYo2Zj21ek2PbTfVZs11QVS-nNQ"
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by key and open the first sheet


app = Flask(__name__)


@app.route("/send", methods=["GET"])
def send():
    from_ad = request.args.get('from')
    # id = request.args.get('id')
    # url = request.args.get('url')
    gid = request.args.get('gid')
    created = datetime.utcnow()
    logger.info(gid)
    sheet = get_sheet(request)
    dict__values__pop = list(request.args.to_dict().values())
    dict__values__pop.pop(0)
    dict__values__pop.insert(0,created.isoformat())
    logger.info(f'request: {dict__values__pop}')
    sheet.append_row(dict__values__pop)
    data = {'status': True, 'from':from_ad}
    return data, 200

# logger.info(f'{id}: value: {val} -> {url}')

def get_sheet(request):
    gid = request.args.get('gid')
    logger.info(f'gid: {gid}')
    logger.info(f'gid empty: {not gid}')
    logger.info(f'gid null: {gid is not None}')
    if gid is not None :
        sheet_id = gid
    else:
        sheet_id = GOOGLE_SHEETS_ID

    logger.info(f'sheet:{sheet_id}')
    sheet = client.open_by_key(sheet_id).sheet1

    return sheet


if __name__ == '__main__':
    app.run()
