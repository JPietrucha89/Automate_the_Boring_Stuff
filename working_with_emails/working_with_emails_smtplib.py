import smtplib
import credentials

# create connection object
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
print(conn)

# connect to server using .helo() function
conn.ehlo()

# start TLS encryption for safety reasons
conn.starttls()

# logging-in which unfortunately doesn't work :P
conn.login(credentials.username, credentials.password)

# sending mail
conn.sendmail('elpietruch@gmail.com', 'elpietruch@gmail.com',
              'Subject: Testowa wysyłka...\n\nDrogi Kubo, osiągnąłeś kolejny krok w procesie zostania leniwą kluchą. Umiesz wysyłać maile z Pythona :O\n\nOby tak dalej :D')

# closing connection
conn.quit()
