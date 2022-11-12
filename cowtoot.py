#!/usr/bin/env python3

print('''      
                    _              _   
   ___ _____      _| |_ ___   ___ | |_ 
  / __/ _ \ \ /\ / / __/ _ \ / _ \| __|
 | (_| (_) \ V  V /| || (_) | (_) | |_ 
  \___\___/ \_/\_/  \__\___/ \___/ \__|

     _(__)_        V
    '-e e -'__,--.__)` *
     (o_o)        ) ` *
      \. /___.  |  *`
       ||| _)/_)/
   gnv //_(/_(/_(

A mastodon moderation script                                       
                                                    ''')

from mastodon import Mastodon

# Enter access token from the development section under the settings/applications link
token = 'put your access token in here'

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

    moderator_assigned = report['assigned_account']['username']
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

