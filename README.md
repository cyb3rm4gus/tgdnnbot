# Telegram deanonymization & ip logging toolkit

based on https://github.com/lamer112311/Dnnme2

how to use:
for each bot (Dnnme2, dnn_filemaker_bot) install requirements:

pip install -r requirements.txt

create .env file for both folders & populate it with data:

ID="your_tg_id"
TOKEN="your_bot_token"

edit sample.html, populate it with your data, add your ip logger pixel and optional scripts and rename it (both file & reference in main.py)

launch the bot & text it anything, it'll send you the file

then stop this bot & lauhch Dnnme2 version that suits your SE strategy and forward the file from bot to target account
