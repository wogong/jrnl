import os
import datetime
import requests

def main():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = '/home/xxx/Dropbox/Dat/jrnl/'
    filename = path + date + '.txt'
    if not os.path.exists(filename):
        content = 'no data'
    else:
        with open(filename, 'r') as f:
            content = f.read()
    send_mailgun(content, date)

def send_mailgun(msg, subject):
    url = "https://api.mailgun.net/v3/xxx.net"+"/messages"
    key = 'key-xxx'
    data = {
            'from': 'Notify <notify.mg@xxx.net>',
            'to': 'journal-xxx@dayone.email',
            'subject': subject,
            'text': msg
            }
    r = requests.post(url, auth=('api', key), data=data)

if __name__ == '__main__':
    main()
