

import datetime
from datetime import timedelta
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build




def create_event(title,start_date,end_date):
    service_account_email = "hfc-884@hfc-test-332904.iam.gserviceaccount.com"
    SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

    credentials = service_account.Credentials.from_service_account_file('google_calendar_credential.json')
    scoped_credentials = credentials.with_scopes(SCOPES)


    def build_service():
        service = build("calendar", "v3", credentials=scoped_credentials)
        return service


    
    service = build_service()

    event = {
    'summary': title,
    'start': {
        'dateTime': start_date.isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': end_date.isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    event = service.events().insert(calendarId='classroom111755921539691473656@group.calendar.google.com', body=event).execute()
    print(event)

title= "HFC 1"
start_date = '2021-11-28T09:00:00-07:00'
end_date = '2021-11-28T17:00:00-07:00'
create_event(title,start_date,end_date)