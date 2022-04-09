import smtplib

gmail_user = 'elvishenry2402@gmail.com'
gmail_pwd = 'rpwdynumgwfkjdit'

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

to = input(str("To : "))
subject = input(str("Subject : "))
msg = input(str("Message : "))
numberSended = input(str("How many : "))

smtpserver.ehlo()
smtpserver.starttls()

smtpserver.login(gmail_user, gmail_pwd)

newMsg = 'To : ' + to + '\n' + 'From : ' + gmail_user + '\n' + f'Subject: {subject} \n' + msg

for i in range(int(numberSended)):
    smtpserver.sendmail(gmail_user, to, newMsg)

print('done!')
smtpserver.close()
