import time
import requests
import pyfiglet
from colorama import Fore, init
init(convert=True)

banner = pyfiglet.figlet_format("round#9999")
result = pyfiglet.figlet_format("999, RIP Mr. Wrld", font = "fourtops" )
print(Fore.GREEN +  banner)
print(Fore.MAGENTA + result)
print(" ")
print(" ")
print(" ")
print(" ")


msg = input(Fore.LIGHTBLUE_EX + "Please Insert Webhook Spam Message: ")
webhook = input(Fore.LIGHTYELLOW_EX + "Please Insert WebHook URL: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(Fore.RED +  'Sent' )
        except:
            print("Bad Webhook: " + webhook)
            time.sleep(5)
            exit()
sperm = 1
while sperm == 1:
    spam(msg, webhook)