from emailSndr import sendMail
import webScrpr
import threading
import time

banner_text = """
--------------------------------------------------------------------
   __      _ _                        
  / _|    | | |                       
 | |_ ___ | | | _____      _____ _ __ 
 |  _/ _ \| | |/ _ \ \ /\ / / _ \ '__|
 | || (_) | | | (_) \ V  V /  __/ |   
 |_| \___/|_|_|\___/ \_/\_/ \___|_|   

ThomannFollower v1.0                                      

--------------------------------------------------------------------
"""

threads = []
emails = list()

class Email:
    def __init__(self, recipients, subject, body):
        self.recipients = recipients
        self.subject = subject
        self.body = body

    def __str__(self):
        return ("to " + str(self.recipients) +  ", Subject: " + self.subject)

    def send(self):
        sendMail(user, password, self.recipients, self.subject, self.body)




def emailPrintLine():
    for email in emails:
        print(email)

def emailLineManager():
    while(1):
        if(len(emails) > 0):
            emails[0].send
            print(emails[0])
            del(emails[0])


def getRecipients():
    recipients = []
    more = True
    while(more):
        user = input("Input the recipient email: ")
        recipients.append(user)
        temp = input("Do you have more recipients? (y/n): ")
        if(temp == 'y' or temp == 'Y'):
            more = True
        else:
            more = False
        
    return recipients


def record(url, recipients, name, subject):
    try:
        price = webScrpr.scrapePrice(url)
        print("request sent succesfully")
        print(" -> base price: " + price)
        while(1):
            time.sleep(120)
            newPrice = webScrpr.scrapePrice(url)

            if(newPrice == price):
                print('no change on ' + name)
            else:
                print(price + ' -> ' + newPrice)
                emails.append(Email(recipients, 
                'price change on '+ name + ' on Thomann.de',
                'price for' + name +' has changed from ' + price + ' to ' + newPrice
                ))
                price = newPrice
        
    except:
        print("Something went wrong while scraping")



def follow():
    #specific info
    url = input("URL you want to follow: ")
    name = webScrpr.getName(url)
    print("Following -> " + name)
    print("\n")

    recipients = getRecipients()

    subject = 'Item subscription on ' + name

    #------------------------------------------------------------------------------------------------------------------------------
    mail = Email(recipients, subject,
    """Hello there,

    You have subscribed to follow""" + name +  """from , you will recieve a mail every time selected item changes price.
    """)
    #-------------------------------------------------------------------------------------------------------------------------------
    emails.append(mail)

    print("\n\n")

    record(url, recipients, name, subject)




#code
#***********************************************************************************************************************************
if __name__ == "__main__":
    print(banner_text)
    print("Enter your server mail details first.")
    user = input("Your email username: ")
    password = input("Your user password: ")
    emailSnd = threading.Thread(target=emailLineManager)
    emailSnd.start()
    # print("\nYou can set a new follow with typing 'New'")

    # while(1):
    #     wait = input()
    #     if(wait == 'New'):
    #         follow()
    #     else:
    #         print("not a command")






#**********************************************************************************************************************************