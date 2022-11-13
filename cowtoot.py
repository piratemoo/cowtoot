#!/usr/bin/env python3

from mastodon import Mastodon
from cowlogo import logo
from config import token
import requests

print(logo)

mastodon = Mastodon(
        access_token=token,
        api_base_url='https://infosec.exchange'
    )

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

reports = mastodon.admin_reports(0)
#print(len(reports))

for report in reports:
    category = report['category']

    target_account = report['target_account']
    target_username = target_account['username']
    target_email = target_account['email']

    report_date = report['created_at']
    comment = report['comment']

    moderator_assigned = report['assigned_account']
    moderator_action = report['action_taken']

    print(f'''
        Category: {str(category).capitalize()}
        Account Reported: {target_username} ({target_email})
        Report Date: {str(report_date)[:10]} 
        Reporter Comments: {comment}
        Moderator assigned: {moderator_assigned}
        Action Taken: {report['action_taken']}
    ''')

    if report['action_taken']:
        print("yup they did something")

#print(reports[0])

