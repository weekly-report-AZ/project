# -*- coding: utf-8 -*-
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '/Users/azuev/projects/weekly_report/weekly-report-218310-8e5d9c875c02.json'
VIEW_ID = '181926962'


def initialize_analyticsreporting():
    '''инициализация api'''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    '''cоздания объекта api'''
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics


def get_report(analytics, url):
    """формирование запроса в api"""
    try:
        return analytics.reports().batchGet(
        body={
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
         }
         ).execute()
        '''обработка ошибок'''
    except TypeError as error:
        print('There was an error in constructing your query : %s' % error)

    except HttpError as error:
        print('There was an API error : %s : %s' % (error.resp.status, error.resp.reason))

#def print_response(response):
#    '''вывод количества органического трафика из Google за неделю  на страницы с вхождением ключа'''
#    k = response['reports'][0]['data']['totals'][0]['values'][0]
#    return k
#    '''сделать исключение на выход за индекс IndexError и неверный ключ KeyError'''


def main_ga(url):
    analytics = initialize_analyticsreporting()
    response = get_report(analytics, url)
    k = response['reports'][0]['data']['totals'][0]['values'][0]
    return k

if __name__ == '__main__':
    l = main_ga('keune')
    print(l)
