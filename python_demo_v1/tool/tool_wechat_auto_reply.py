

import itchat, time, threading

@itchat.msg_register('Text')
def text_reply(msg):
    """auto reply"""
    print(msg['Text'])
    return '然后呢？'



def send():
    while True:
        author = itchat.search_friends(name = '何桂霞')[0]
        current_time = time.localtime(time.time())
        if(current_time.tm_sec == 0):
            # author.send('小姐姐')
            print(current_time.tm_hour + current_time.tm_min + current_time.tm_sec)
        time.sleep(1)


itchat.auto_login(True)


positiveSendingThread = threading.Thread(target=send)
positiveSendingThread.setDaemon(True)
positiveSendingThread.start()

itchat.run()
