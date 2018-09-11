import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

# Errbot will start in text mode (console only mode) and will answer commands from there.
# BACKEND = 'Text'
BACKEND = 'Slack'

BOT_DATA_DIR = r'/Users/soichiro_yoshimura/workspace/slackonline/data'
BOT_EXTRA_PLUGIN_DIR = r'/Users/soichiro_yoshimura/workspace/slackonline/plugins'

BOT_LOG_FILE = r'/Users/soichiro_yoshimura/workspace/slackonline/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

# slack botのBot User OAuth Access Tokenを記載
BOT_IDENTITY = {
    'token': 'xoxb-00000000000000000000000000000000000000000000000000000'
}

# !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!
# BOT_ADMINS = ('@CHANGE_ME', )
BOT_ADMINS = ('@sifue', )
