

import itchat
import json
import requests
from itchat.content import *

tuling = True

def tuling_msg(msg):
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            }
        },
        "userInfo": {
            "apiKey": "5ba9610c7db546b4b63fe8ab50086ad1",
            "userId": "itchat"
        }
    }
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    res = requests.post(url, data=json.dumps(data)).json()
    return res['results'][0]['values']['text']

def qingyunke_msg(msg):
    data = {
        'msg': msg,
        'key': 'free',
        'appid': 0
    }
    url = 'http://api.qingyunke.com/api.php'
    res = requests.get(url, params=data)
    data = res.json()
    return data['content']

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    global tuling
    print('From ' + msg['FromUserName'] + ': ' + msg.text)
    if tuling:
        res = tuling_msg(msg.text)
    else:
        res = qingyunke_msg(msg.text)
        
    print('Sending to ' + msg['FromUserName'] + ': ' + res)
    msg.user.send(res)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('智障机器人1号添加了你!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    global tuling
    if msg.isAt:
        if tuling:
            res = tuling_msg(msg.text)
        else:
            res = qingyunke_msg(msg.text)
            
        msg.user.send(res)

itchat.auto_login(hotReload=True)
itchat.run()

# print(qingyunke_msg('你是谁'))
# print(tuling_msg('你是谁'))





