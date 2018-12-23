
import poplib
from email.parser import Parser

email = 'liang_renhong@163.com'

password = 'lrh0000'

pop3_server = 'pop.163.com'

server = poplib.POP3(pop3_server)

print(server.getwelcome().decode('utf8'))

server.user(email)
server.pass_(password)

print('Message: %s. Size: %s' % (server.stat()))

resp, mails, octets = server.list()

# print(mails)

index = len(mails)

resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')

msg = Parser().parsestr(msg_content)

print(msg)

server.quit()
