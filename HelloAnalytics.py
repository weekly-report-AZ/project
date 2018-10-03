"""Hello Analytics Reporting API V4."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '/Users/azuev/projects/weekly_report/weekly-report-218310-8e5d9c875c02.json'
VIEW_ID = '181926962'

def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
# Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics

def get_report(analytics):
    """Queries the Analytics Reporting API V4.

    Args:
    analytics: An authorized Analytics Reporting API V4 service object.
     Returns:
    The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:source'}]
                }
            ]
        ,"dimensionFilterClauses": 
            [{"filters": 
                [{
                "dimensionName": "ga:pagePath",
                "operator": "REGEXP",
                "expressions": "keune"},
                {"dimensionName": "ga:sourceMedium",
                "operator": "EXACT",
                "expressions": ["google / organic"]}
                ]}
            ]}
    ).execute()

def print_response(response):
    print (response)

def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    print_response(response)

if __name__ == '__main__':
    main()
