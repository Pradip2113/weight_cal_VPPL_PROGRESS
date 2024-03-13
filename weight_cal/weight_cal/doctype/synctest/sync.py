import requests
import frappe
import json

site1_url = 'http://192.168.1.10:82'
site1_api_key = '0ac6978c7eead65'
site1_api_secret = 'b5a9bc086f70429'

site2_url = 'http://vppluatpp2.erpdata.in'
site2_api_key = '3185eb51e17259e'
site2_api_secret = '41404704f8d7200'


endpoint = '/api/resource/SyncTest'

# Retrieve the list of records from each site.
site1_records = requests.get(site1_url + endpoint, auth=(site1_api_key, site1_api_secret)).json()
site2_records = requests.get(site2_url + endpoint, auth=(site2_api_key, site2_api_secret)).json()

# Compare the two lists and determine which records need to be synced.
site1_record_ids = set(r['name'] for r in site1_records['data'])
site2_record_ids = set(r['name'] for r in site2_records['data'])

def sync_new_record(doc,method):

    records_to_sync = []
    for record_id in site1_record_ids - site2_record_ids:
        record = next(r for r in site1_records['data'] if r['name'] == record_id)
        record_details = requests.get(site1_url + endpoint + '/' + record_id, auth=(site1_api_key, site1_api_secret)).json()
        record['doc'] = record_details['data']

        records_to_sync.append(record)

    for record_id in site2_record_ids - site1_record_ids:
        record = next(r for r in site2_records['data'] if r['name'] == record_id)
        record_details = requests.get(site2_url + endpoint + '/' + record_id, auth=(site2_api_key, site2_api_secret)).json()
        record['doc'] = record_details['data']

        records_to_sync.append(record)

    # Create a new record on the target site for each record that needs to be synced.
    for record in records_to_sync[::-1]:
        if record['name'] in site1_record_ids:
            # Sync the document to site2
            data = {'data': record['doc']}
            requests.post(site2_url + endpoint, json=data, auth=(site2_api_key, site2_api_secret))

        else:
            # Sync the document to site1
            data = {'data': record['doc']}
            requests.post(site1_url + endpoint, json=data, auth=(site1_api_key, site1_api_secret))

    # Update the synced records with the appropriate data.
    for record in records_to_sync[::-1]:
        if record['name'] in site1_record_ids:
            # Update the document in site2
            data = {'data': record['doc']}
            requests.put(site2_url + endpoint + '/' + record['name'], json=data, auth=(site2_api_key, site2_api_secret))

        else:
            # Update the document in site1
            data = {'data': record['doc']}
            requests.put(site1_url + endpoint + '/' + record['name'], json=data, auth=(site1_api_key, site1_api_secret))



def sync_del_record(doc,method):

    temp=str(doc.uin)
    
    url = f"http://vppluatpp2.erpdata.in/api/resource/SyncTest?filters=[[\"uin\",\"=\",\"{temp}\"]]"

    payload = {}
    headers = {
    'Authorization': 'token 3185eb51e17259e:41404704f8d7200',
    'Cookie': 'full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    restemp=str(response.text)
    
    
    
    data = json.loads(restemp)

    name = data['data'][0]['name']

    url = f"http://vppluatpp2.erpdata.in/api/resource/SyncTest/{name}"

    payload = {}
    headers = {
    'Authorization': 'token 3185eb51e17259e:41404704f8d7200',
    'Cookie': 'full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image='
    }

    
    response = requests.request("DELETE", url, headers=headers, data=payload)
    
    # records_to_delete =  site1_record_ids ^ site2_record_ids

    # for record_id in records_to_delete:
    #     if record_id in site1_record_ids:
    #         # Delete the record from site1
    #         requests.delete(site1_url + endpoint + '/' + record_id, auth=(site1_api_key, site1_api_secret))

    #     if record_id in site2_record_ids:
    #         # Delete the record from site2
    #         requests.delete(site2_url + endpoint + '/' + record_id, auth=(site2_api_key, site2_api_secret))


# def sync_update_record(doc,method):
#     for record_id in site1_record_ids.union(site2_record_ids):
#         if record_id in site1_record_ids:
#             # Get the record from site1
#             response = requests.get(site1_url + endpoint + '/' + record_id, auth=(site1_api_key, site1_api_secret))
#             if response.status_code == 200:
#                 # Update the record on site2
#                 requests.put(site2_url + endpoint + '/' + record_id, json=response.json(), auth=(site2_api_key, site2_api_secret))
#         else:
#             # Get the record from site2
#             response = requests.get(site2_url + endpoint + '/' + record_id, auth=(site2_api_key, site2_api_secret))
#             if response.status_code == 200:
#                 # Update the record on site1
#                 requests.put(site1_url + endpoint + '/' + record_id, json=response.json(), auth=(site1_api_key, site1_api_secret))