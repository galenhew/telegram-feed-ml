# telegram_ml_feed

## this bot allows you to keep track of ML runs on colab or kaggle. 
- use botfather to create bot
- get the API from botfather
- enter in config.yaml and test with import_tele.py


- use functions in callback
```    
bot_callback = botCallback(access_token, notebook_name)
plotter = Plotter(access_token, notebook_name)
callback_list = [bot_callback,
                plotter
                ]
start = time.time()

history = model.fit(x_train, y_train, 
                    steps_per_epoch = 5,
                    epochs=5,
                    validation_data= val_data,
                    callbacks=callback_list)
end = time.time()
```# telegram-feed-ml
