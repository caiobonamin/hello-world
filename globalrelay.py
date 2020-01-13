import smtplib
import glob
import os
import sys

emlfiles = []

for file in glob.glob("extracted\\*.eml"):
    emlfiles.append(file)

for msg in emlfiles:
    if not os.path.isfile(msg):
        print('File "' + msg + '" not found.')
        sys.exit(0)

    with open(msg) as m:
        message = m.read()

        try:
            print('File "' + msg + '" Being Processed.')
            server=smtplib.SMTP("<RELAY.domain.com>",25)
            server.set_debuglevel(1)
            server.ehlo('exoduspoint.com')
            server.starttls()
            server.login(‘<DOMAIN>\<svcUsername>’,"<PASSWORD>”)
            mailfrom = ‘<svcUsernameEmail>@exoduspoint.com'
            rcptto = "exoduspoint.com+Symphony@mailarchivespool1.globalrelay.com"
            server.sendmail(mailfrom,rcptto,message)

        except Exception as e:
            print('Failed to send mail.')
            print(str(e))

        else:
            print('Sent Message' + msg)

        finally:
            if server != None:
                server.close()