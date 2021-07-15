import requests

def unlock():
    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/unlock"

    payload = {}
    files = {}
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': f'Bearer {access_token}',
        'api-version': '2020-06-01',
        'callback-url': '{{callback-url}}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response


def lock():
    """POST REQUEST"""

    import requests
    import json

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/lock"

    payload = {}
    files = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': 'Bearer null',
        'api-version': '2020-06-01'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response


def start_engine():
    """POST REQUEST"""

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/startEngine"

    payload = {}
    headers = {
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': 'Bearer null',
        'api-version': '2020-06-01'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def stop_engine():
    """POST REQUEST"""

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/stopEngine"

    payload = {}
    headers = {
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': 'Bearer null',
        'api-version': '2020-06-01'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def wake():
    """POST REQUEST"""

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/wake"

    payload = {}
    headers = {
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': f'Bearer {access_token}',
        'api-version': '2020-06-01'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def vehicle_status():

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/statusrefresh/b597f4c6-f4be-4746-8fcb-d19469ab554e"

    payload = {}
    files = {}
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': f'Bearer {access_token}',
        'api-version': '2020-06-01',
        'callback-url': '{{callback-url}}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    return response


def vehicle_info():
    import requests

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a"

    payload = {}
    headers = {
        'Application-Id': 'afdc085b-377a-4351-b23e-5e1d35fb3700',
        'Authorization': f'Bearer {access_token}',
        'api-version': '2020-06-01'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def location():
    import requests

    url = "https://api.mps.ford.com/api/fordconnect/vehicles/v1/8a7f9fa878849d8a0179579d2f26043a/location"

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

    url = "https://dah2vb2cprod.b2clogin.com/914d88b1-3523-4bf6-9be4-1b96b4f6f919/oauth2/v2.0/token?p=B2C_1A_signup_signin_common"

    payload = {'grant_type': 'refresh_token',
               'refresh_token': 'eyJraWQiOiI2cjIzQ2FTeTF4cFdUUFBxYVRtX01Vc2RKZGo1RWlDTnRtME4yVTAxNTdFIiwidmVyIjoiMS4wIiwiemlwIjoiRGVmbGF0ZSIsInNlciI6IjEuMCJ9.TkcBX-dLijNz3Bwpdiv52mwf1I59VgWEkvncGuROYcbBpE_-swRxNlR6h_ZeEY7tN00o2vrKmqClWo7YiU38QawfoNHZCHuVXBTRhBeFa4B0VwIrslG9qo6k5JRZtWtTNVjz3-i7ZraNMHTafqOz2oy_EHNx9oSL540L6NSjTcfiCsUaGtmYRGr0WKxk_dgBCkdM_wFtSNC5wQZ3q11H4mv6cL4JRfMHV6Ay-x5AABAHrw67KAZK13bPSBvSKz-cj2wP_fmU3ssGaLpN0IJmmNYQ2WBR3xxDnEWbsQ8woCROH-vsPrTnfb-fu7r4c6roypCYL_IdV0ulxJiR2FBzcQ.06_IsaYaXvc9YQPP.1YvTasPLhEz3sxkJ6Zd6DDyG7xaPh-p21aiG0toh-VXptjUUObJSfeBz-iWrofEtSn1mUEV-RYw4HAzuqiB-NguEqQ14cr-STW7f3E6ShAzZDX-4LJcrFl07mhogWUBxOuf3EU-AeU1NF_vRPU3ryG8pXnJWVm_Av-qLjCPBGKK4GKF0eW6fjkN7Tl_9eQhaPvXpypfdrMmwT9zB2cAsAT6VCWU40RFLv5wPZhikQ8IS8pWsuLsYaCsYDhkdZIvikS3MICouIVTJV4eOebi1Ew-hLkVkT55i9XX3X0ZZYRATHr1ABTEg1jMVYTj4QX9BSZjRMGd9yhxrjNQYXBLj81mxcq_lITfLGvWwge9N6D6C0o1oxuycsyk9jCIbHTWOA6FgOlyIAgSb8G3AQJnt_PXosSMtNYbTcq4rc3XjUVRxBrBa6aCyvoK8_-ebhs4-F-dXw3dIZVSjeMz1G6gfCAAWfNZ3NtpxufEkrggphunxvjcEuwtrhYs7tQh_8SynP-S1v8QIE5VCi-cIlEMFIVmS5Y6PqByS2Qx03atWkrG-zALPu-3fRLY7BrYjEITekDf4BTzEQ13wRl7FBuLG2Sd5AMoK61CX7PqQe3SK4yOD_AvsQK2cmJMemYYpor_ICVCik1cLC1ElUBMiKR1mEFLFZR74TUoYX9wxSNhLMcIjoHdBhMmMdNylLqfQDqmfkxmzSeTeEpC6ijR2_gqnWliFZrNQnDslT1zjzHNkl94azGah-DWD0ka-1Lnx5_hSLSRWUfmnPntqNYB_Vk2EEATEMBwmHWU091G30Pq_jMgpB2p9xOzhXIyj5wHgPbgnAXYURbXwWNogLgQ4.ZykCIWn3Vnyt_I3TJrtLAg',
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

access_token = refresh_token().json()['access_token']
print('parsed info here')
info = parse(vehicle_info().json())

import time
import os
import json

prev_time = time.time() * 1000
while True:
    path = os.getcwd()

    if time.time()*1000 - prev_time >= 5000:
        info = parse(vehicle_info().json())

        with open(f'{path}/api.json', 'w') as f:
            json.dump(info, f)
            prev_time = time.time() * 1000