import slack 
import os 
from pathlib import Path
from dotenv import load_dotenv

# this loads the environment file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# this should load the exact value from this file
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# send a message into the slack channel 
client.chat_postMessage(channel='#bots', text="Hello Hackers")
