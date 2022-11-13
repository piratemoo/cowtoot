""" In your profile settings, when you add an app on Mastodon, you receive
1. A client key
2. A client secret
3. Your access token

We only need your access token in order for this script to work

Add it into the config.toml

"""

import toml

try:
    with open('config.toml', 'r') as f:
        config = toml.loads(f.read())
except FileNotFoundError:
    print('Couldn\'t find the config file! Read the README.md for instructions on setting this up')
except Exception as e:
    print('Something went wrong loading the config file: {e}')
