# -*- coding: utf-8 -*-
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = ''
VIEW_ID = '181926962'


def initialize_analyticsreporting():
    # инициализация api
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    # cоздания объекта api
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics


def get_report(analytics, url):
    # формирование запроса в api
        return analytics.reports().batchGet(body={
            'reportRequests':
                [
                    {
                        'viewId': VIEW_ID,
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'yesterday'}],
                        'metrics': [{'expression': 'ga:sessions'}],
                        'dimensions': [{'name': 'ga:source'}],
                        "dimensionFilterClauses":
                            [
                                {
                                    "filters":
                                        [
                                            {
                                                "dimensionName": "ga:pagePath",
                                                "operator": "REGEXP",
                                                "expressions": [url]
                                            }
                                        ]
                                },
                                {
                                    "filters":
                                        [
                                            {
                                                "dimensionName": "ga:sourceMedium",
                                                "operator": "EXACT",
                                                "expressions": ["google / organic"]
                                            }
                                        ]
                                }
                            ]
                    }
                ]
         }).execute()


def main_ga(url):
    analytics = initialize_analyticsreporting()
    response = get_report(analytics, url)
    result = int(response['reports'][0]['data']['totals'][0]['values'][0])
    return result


if __name__ == '__main__':
    main = main_ga('keune')
    print(main)
