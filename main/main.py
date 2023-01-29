from config import utelegram_config
from config import wifi_config
from ExcelWrite import ReadDocument

import utelegram
import network
import utime

debug = True

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

if debug: print('WAITING FOR NETWORK - sleep 20')
utime.sleep(20)
    

def get_message(message):
    #bot.send(message['message']['chat']['id'], message['message']['text'].upper())
    bot.send(message['message']['chat']['id'], '/add Add value\n/del Delete last\n/start Init message')
    
def append_values(message):
    val= message['message']['text']
    if len(val) > 4:
        if val[4] == " " and len(val) > 5: 
            finalvalue= val[4:].replace(" ", "")
            bot.send(message['message']['chat']['id'], finalvalue)
        else:
            print('No valid value')
    else:
        print('No valid value')

def reply_ping(message):
    bot.send(message['message']['chat']['id'], 'pong')

if sta_if.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/ping', reply_ping)
    bot.register('/add', append_values)
    bot.register('/start',get_message)
    bot.set_default_handler(get_message)

    print('BOT LISTENING')
    bot.listen()
else:
    print('NOT CONNECTED - aborting')