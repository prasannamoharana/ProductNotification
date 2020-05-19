#Program to get mail notificatin when price changes to low.

import smtplib
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Kadence-Premium-Trans-Acoustic-Guitar-effects/dp/B07V5FJHYX/ref=sr_1_1?dchild=1&pf_rd_i=3677697031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=f20048b9-3dca-458a-993a-38946d53df31&pf_rd_r=ABAG01GQZM4D876JR7CW&pf_rd_s=merchandised-search-12&pf_rd_t=101&qid=1589879104&refinements=p_89%3AKadence%2Cp_85%3A10440599031%2Cp_72%3A1318477031&rps=1&s=musical-instruments&sr=1-1'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
# headers capture info about browser we can get it by my user agent in google.

def check_price():
    page = requests.get(URL, headers=headers)  # page will call
    soup = BeautifulSoup(page.content, 'html.parser')  # pull the page info
    title = soup.find(id='productTitle').get_text() #product title of goods
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[0:8]

    if (converted_price < 25000):
        send_mail()
    print(converted_price)
    print (title.strip()) # shows only title
# now we need to enable google 2 factor authentication then google app passwd & create  passwd outof it.

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)  # 587 is teh connectiin number
    server.ehlo()  # ehlo establish connection
    server.starttls()
    server.ehlo()

    server.login('prasanna@gmail.com', 'dahahahfju')  # dahahahfju is the passwd of my mail id.
    subject = 'price fell down'
    body = 'check the link https://www.amazon.in/Kadence-Premium-Trans-Acoustic-Guitar-effects/dp/B07V5FJHYX/ref=sr_1_1?dchild=1&pf_rd_i=3677697031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=f20048b9-3dca-458a-993a-38946d53df31&pf_rd_r=ABAG01GQZM4D876JR7CW&pf_rd_s=merchandised-search-12&pf_rd_t=101&qid=1589879104&refinements=p_89%3AKadence%2Cp_85%3A10440599031%2Cp_72%3A1318477031&rps=1&s=musical-instruments&sr=1-1'
    msg = f'subject: {subject}\n\n{body}'
    server.sendmail(
        'amazon mailid',
        'prasanna@gmail.com',
        msg
    )
    print('email has sent')
    server.quit()


check_price()
