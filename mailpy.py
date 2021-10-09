
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendMail(option, data, process):

    # create message object instance
    msg = MIMEMultipart()

    if option == 1:
        message = f'Data download: \n\n {data}'
        subject = f'Process successful 😎 {process}'
    else:
        message = f'Error: \n\n {data}'
        subject = f'Process error 💩 {process}'

    # setup the parameters of the message
    password = config('password', default='') 
    msg['From'] = config('email_from', default='') 
    msg['To'] = config('email_to', default='') 
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    print('envio de mail')

    server.quit()

def run():
    process_name = 'Test process'
    
    try:
        for i in 12:
            i
        sendMail(1, 'Completo', process_name)

    except Exception as e:
        print(f'Envio mail con error {e}')
        sendMail(0, e, process_name)

if __name__=='__main__':
    run()