#!/usr/bin/env python3

from mastodon import Mastodon
from datetime import datetime
from cowlogo import logo
from config import token

print(logo)

mastodon = Mastodon(
    access_token=token,
    api_base_url='https://infosec.exchange'
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
def audit_reports(max_pages=2, per_page=50):
    last_id = None
#Handles pagination issues
    for page_number in range(0, max_pages):
        reports = mastodon.admin_reports(resolved=True, max_id=last_id, limit=per_page)

        if reports is None:
            return

        for report in reports:
            report_category = report['category']
            last_id = report['id']

            target_account = report['target_account']
            target_username = target_account['username']
            target_email = target_account['email']
            report_date = report['created_at'].strftime("%A, %B %d %Y")

            comment = report['comment']

            if report['assigned_account']:
                moderator_assigned = report['assigned_account']['username']
            else:
                moderator_assigned = 'Unassigned'

            moderator_action = report['action_taken']

            print(f'''
                Category: {str(report_category).capitalize()}
                Account Reported: {target_username} ({target_email})
                Report Date: {report_date}
                Reporter Comments: {comment}
                Moderator assigned: {moderator_assigned}
                Action Taken: {report['action_taken']}
                ''')


instance_information()
audit_reports()
