#
# I want full green github history, but unfortunately I'm lazy af ¯\_(ツ)_/¯
#

import subprocess
from datetime import datetime
from win10toast import ToastNotifier
import random
import time

current_datetime = datetime.today()

formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)

random_times = random.randint(1, 5)

for _ in range(random_times):
    formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"An other one {formatted_date} 👆"])
    subprocess.run(["git", "push", "-u", "origin", "master"])

    time.sleep(5)


def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message)


show_notification("Dear Taki",
                  "Makin' it greener (◕‿◕✿)")
