from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

now = datetime.now()
hacker_news_url = 'https://news.ycombinator.com'
br = '--------------------------------'

SERVER = 'smtp.gmail.com'
PORT = 587


def get_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cnt = '<b>Top Stories for Today</b><br>' + '-'*50 + '<br>'*3
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += (str(i+1) + '::' + tag.text +
                '<br>'*2) if tag.text != 'More' else ''
    return cnt


def create_msg(content, to, from_):
    msg = MIMEMultipart()
    msg['Subject'] = 'Top News Stories HN [Automated Message] - ' + \
        str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    msg['From'] = from_
    msg['To'] = to

    msg.attach(MIMEText(content, 'html'))

    return msg


def send_message(msg, to, from_, password):
    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    print(br, 'Logging In', br)
    server.login(from_, password)
    server.sendmail(from_, to, msg.as_string())
    print(br, 'Email Sent to', to, br)
    server.quit()


def main():
    FROM = '##############@gmail.com'
    TO = ['##########@gmail.com', '############@gmail.com']
    PASS = '****************'
    content = ''
    content += get_content(hacker_news_url)
    content += '<br>----------------------<br><br><br>End of Message'

    for recepient in TO:
        msg = create_msg(content, recepient, FROM)
        print(br, 'Sending Message to', recepient, br)
        send_message(msg, recepient, FROM, PASS)


if __name__ == '__main__':
    main()
