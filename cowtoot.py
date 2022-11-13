#!/usr/bin/env python3

from mastodon import Mastodon
from datetime import datetime, timedelta
from cowlogo import logo
from config import config
import pytz

print(logo)

mastodon = Mastodon(
    access_token=config['accessToken'],
    api_base_url=config['serverURL']
)


def instance_information():
    # Print basic server information/stats
    server = mastodon.instance()
    server_title: str = server['title']
    server_des: str = server['short_description']

    server_cont: str = server['contact_account']
    server_admin: str = server_cont['username']
    server_email: str = server['email']

    curr_version: str = server['version']
    max_toot: str = server['max_toot_chars']

    print(f'''
         Title: {server_title}
        Description: {server_des}
        Server Admin: {str(server_admin.capitalize())}
        Email Contact: {server_email}
        Version: {curr_version}
        Toot Character Limit: {max_toot}
        ''')

#Change the values to maximize the results you'd like
def get_reports(reportsSince, maxPages=10):
    reports = []

    i = 0
    while True:
        if not reports:
            reportPage = mastodon.admin_reports(resolved=True)
        else:
            reportPage = mastodon.fetch_next(reportPage)
        
        if reportPage is None:
            break

        reports.extend(reportPage)

        if is_last_page(reportsSince, reportPage):
            break

        i += 1
        if i >= maxPages:
            print("WARNING: max pages reached, reports list will not be accurate")
            break
    
    reportsFiltered = []
    # Filter the array of reports
    for report in reports:
        if report['created_at'] > reportsSince:
            reportsFiltered.append(report)
    
    return reportsFiltered
        
    


def is_last_page(reportsSince, reports):
    report_date = reports[-1:][0]['created_at']
    return report_date < reportsSince



def print_report_stats(since):
    
    reports = get_reports(since)

    print(f'Since {since.strftime("%Y-%m-%d %H:%M:%S")} UTC, there were {len(reports)} resolved reports.')

    return

def print_all_reports(since):
    reports = get_reports(since)
    for report in reports:
        report_category = report['category']

        target_account = report['target_account']
        target_username = target_account['username']
        target_email = target_account['email']
        report_date = report['created_at'].strftime("%A, %B %d %Y")

        comment = report['comment']

        if report['assigned_account']:
            moderator_assigned = report['assigned_account']['username']
        else:
            moderator_assigned = 'Unassigned'

        #moderator_action = report['action_taken']

        print(f'''
            Category: {str(report_category).capitalize()}
            Account Reported: {target_username} ({target_email})
            Report Date: {report_date}
            Reporter Comments: {comment}
            Moderator assigned: {moderator_assigned}
            Action Taken: {report['action_taken']}
            ''')


instance_information()
lastDay = pytz.UTC.localize(datetime.now() - timedelta(days=3))
print_report_stats(lastDay)
