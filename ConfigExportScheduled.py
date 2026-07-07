import requests
import json
import pandas as pd

app_host = 'https://wayfd.sce.manh.com'
auth_host = 'https://wayfd-auth.sce.manh.com'
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyT3JncyI6WyJVUzI1Il0sInVzZXJfbmFtZSI6ImhmZW5kZXIiLCJ1c2VyTG9jYXRpb25zIjpbeyJsb2NhdGlvbklkIjoiVVMyNSIsImxvY2F0aW9uVHlwZSI6ImR1bW15In1dLCJsb2NhbGUiOiJlbi1DQSIsImV4Y2x1ZGVkVXNlckJ1c2luZXNzVW5pdHMiOltdLCJhdXRob3JpdGllcyI6WyJST0xFX2FkbWluQFVTMjUiLCJST0xFX1VTRVIiXSwiY2xpZW50X2lkIjoib21uaWNvbXBvbmVudC4xLjAuMCIsInVzZXJUaW1lWm9uZSI6bnVsbCwiZWRnZSI6MCwic2NvcGUiOlsib21uaSIsImNvbXBvbmVudCJdLCJvcmdhbml6YXRpb24iOiJVUzI1IiwiYWNjZXNzdG9BbGxCVXMiOmZhbHNlLCJ0ZW5hbnRJZCI6ImNjaGlzcHIxMW8iLCJleHAiOjE2ODM2ODI1NjgsInVzZXJEZWZhdWx0cyI6W10sImp0aSI6IjgwZWJjYjNhLTAzNjItNDdkOC05MzJmLTJiY2I5MDAxZmYwYSIsInVzZXJCdXNpbmVzc1VuaXRzIjpbXX0.HfV130_A72LSqsEyLuL21WQ8jCfenfXET0Rq1v-58gW7D9yXLhBq3AmQ8mmnoX2ROM77uPYjvpno6mPxfbw4t1YdpVEwy8K9t9flbzdhBhj1Ujzo_g8_RW8lnvxTCYPsZppFc3zgU2iVebTzKwg91LlGZkprk1AAVJpD-FL8diLUAOEugXXAfXINKBZXdF8TrjwT8WTsB5XVm0VtkKQ1I-tenh_UDcVCJFLjmGS6499PjhrkC47omYDCgL8wXN9vaIISk9VYhLwzZh3c46xPf980uCBa2AkwMMP1OUhYtzCe1Xxf4Wpbx_PHzSaY2VFp7EskaJ6yAAGJw_24qeUAXQ'
auth_token = 'b21uaWNvbXBvbmVudC4xLjAuMDpiNHM4cmdUeWc1NVhZTnVu'

auth_url = auth_host + '/oauth/token'
auth_user = 'hfender_guest@wayfair.com'
auth_password = 'P@ssword5'
auth_data = {'grant_type': 'password',
             'username': auth_user,
             'password': auth_password}
auth_headers = {'Authorization': 'Basic ' + auth_token,
                'Content_Type': 'application/x-www-form-urlencoded'}

##Authenticate user credentials##
auth_response = requests.post(auth_url, data=auth_data, headers=auth_headers)

if auth_response.status_code == 200:
    auth_json = auth_response.json()
    access_token = auth_json['access_token']
    # Use the access token to make API requests
else:
    print('Error: authentication request failed')

print(auth_response)

headers = {'Authorization': f'Bearer {access_token}',
            'selectedOrganization':'WAY-ABERDEEN',
            'selectedLocation':'WAY-ABERDEEN'}

##Specify URL for orders##
configdirector_url = app_host + '/cfg/api/configDirector/exportByProfile'
data = {
    "Qualifier": None,
    "ProfileId": "WAY-ABERDEEN",
    "MasterDataRequired": False,
    "Notes": "PYTHON RUN",
    "Components": [
        {
            "ComponentName": "workrelease",
            "Entities": []
        }
    ],
    "ProfilePurposes": [],
    "FunctionalGroups": [],
    "ExcludeProfilePurposes": [],
    "ExcludeFunctionalGroups": [],
    "StatusMessageType": ""
}

##POST for Order IDs##
configdirector_response = requests.post(configdirector_url, json=data, headers=headers)
configdirector_json = configdirector_response.json()