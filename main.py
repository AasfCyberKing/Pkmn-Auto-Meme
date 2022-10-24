import os
import logging
import time

from AutoPostTelegram import auto

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

TOKEN = os.environ.get("TOKEN", None) # Your Bot's Token Get It From @Botfather
CHAT = os.environ.get("CHAT", None) # Your Group Or Channel's Username With @ Symbol Where It Post Memes
GAP = os.environ.get("GAP", None) # Time Gap Of Your Post In Second 1 min = 60 sec

# For Local Deploy:
"""
TOKEN = ""
CHAT = ""
GAP = ""
"""

app = auto(TOKEN)

while True:
    app.pkmnmeme(chat=CHAT)
    time.sleep(int(GAP)) #The Time Gap Of Your Post In Seconds
    app.pkmnmeme(chat=CHAT)
    time.sleep(GAP) #The Time Gap Of Your Post In Seconds
