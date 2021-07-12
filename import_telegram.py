import telegram_feed as tele

import yaml

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    access_token= data['telegram_api']['access_token']


# run me to test

notebook_name= 'telegram-colab notebook'


bot1= tele.botCallback(access_token, notebook_name)
bot1.send_message('hi dicky')


