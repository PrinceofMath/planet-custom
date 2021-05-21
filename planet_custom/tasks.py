from planet import api
import sys
import os
import requests
import time
import frappe

apikey = '92e11e515ad344b386c19f0a4dce232c'
client = api.ClientV1(api_key=apikey)

item_type = ["PSScene4Band"]
asset_type = 'visual'

def create_daily_image():
    locations = frappe.db.get_list("Location")
    print(locations)