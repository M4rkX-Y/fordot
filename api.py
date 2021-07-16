def vehicle_info():
    import requests

    url = f"{domain}/api/fordconnect/vehicles/v1/{vehicle_id}"

    payload = {}
    headers = {
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': f'Bearer {access_token}',
        'api-version': '2020-06-01'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def refresh_token():
    import requests

    url = f"{domain}/oauth2/v2.0/token?p=B2C_1A_signup_signin_common"

    payload = {'grant_type': 'refresh_token',
               'refresh_token': f'{token}',
               'client_id': '30990062-9618-40e1-a27b-7c6bcb23658a',
               'client_secret': 'T_Wk41dx2U9v22R5sQD4Z_E1u-l2B-jXHE'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response

def parse(data):
    #oil, odometer, location, lock, tire, charge/gase
    info = {}

    info['fuel_value'] = data['vehicle']['vehicleDetails']['fuelLevel']['value']
    info['fuel_distance_to_empty'] = data['vehicle']['vehicleDetails']['fuelLevel']['distanceToEmpty']

    info['location_longitude'] = data['vehicle']['vehicleLocation']['longitude']
    info['location_latitude'] = data['vehicle']['vehicleLocation']['latitude']
    info['speed'] = data['vehicle']['vehicleLocation']['speed']
    info['direction'] = data['vehicle']['vehicleLocation']['direction']

    info['door_unspecified_front_door'] = data['vehicle']['vehicleStatus']['doorStatus'][0]['value']
    info['door_unspecified_front_role'] = data['vehicle']['vehicleStatus']['doorStatus'][0]['vehicleOccupantRole']

    info['engine_status'] = data['vehicle']['vehicleStatus']['remoteStartStatus']['status']
    info['engine_duration'] = data['vehicle']['vehicleStatus']['remoteStartStatus']['duration']

    info['tire_warning'] = data['vehicle']['vehicleStatus']['tirePressureWarning']

    info['charge_value'] = data['vehicle']['vehicleStatus']['chargingStatus']['value']
    info['charge_start'] = data['vehicle']['vehicleStatus']['chargingStatus']['chargeStartTime']
    info['charge_end'] = data['vehicle']['vehicleStatus']['chargingStatus']['chargeEndTime']

    info['ignition_status'] = data['vehicle']['vehicleStatus']['ignitionStatus']['value']

    info['battery_value'] = data['vehicle']['vehicleDetails']['batteryChargeLevel']['value']
    info['battery_distanceToEmpty'] = data['vehicle']['vehicleDetails']['batteryChargeLevel']['distanceToEmpty']

    info['mileage'] = data['vehicle']['vehicleDetails']['mileage']
    info['odometer'] = data['vehicle']['vehicleDetails']['odometer']
    info['charge_plug_value'] = data['vehicle']['vehicleStatus']['plugStatus']['value']

    return info


import time
import os
import json

open(f'{os.getcwd()}/token.json').close()

running = True
while running:
    with open(f'{os.getcwd()}/token.json', 'r') as f:
        data = json.load(f)
        if 'domain' in data.keys():
            if 'token' in data.keys():
                if 'vehicle_id' in data.keys():
                    domain = data['domain']
                    token = data['token']
                    vehicle_id = data['vehicle_id']
                    running = False
                    
access_token = refresh_token().json()['access_token']

prev_time = time.time() * 1000
while True:
    path = os.getcwd()

    if time.time()*1000 - prev_time >= 5000:
        info = parse(vehicle_info().json())
        print(info)

        with open(f'{path}/api.json', 'w') as f:
            json.dump(info, f)
            prev_time = time.time() * 1000