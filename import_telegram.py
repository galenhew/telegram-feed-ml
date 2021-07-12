import telegram_feed as tele

import yaml

keys_file = 'config.yaml'

with open(keys_file) as yamlfile:
    try:
      data=yaml.safe_load(yamlfile)
      access_token= data['telegram_api']['access_token']
    except yaml.YAMLError as exc:
        print(exc)
# run me to test

notebook_name= 'telegram-colab notebook'


bot1= tele.botCallback(access_token, notebook_name)
bot1.send_message('hi dicky')


