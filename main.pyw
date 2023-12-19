import subprocess
from datetime import datetime
from win10toast import ToastNotifier
import random
import time
import sys

DETACHED_PROCESS = 0x00000008


def printing():
    current_datetime = datetime.today()

    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print(formatted_date)

    random_times = random.randint(1, 5)

    for _ in range(random_times):
        with open('green.txt', 'a') as file:
            file.write('Jeremiah 29:11\n')

        time.sleep(1)

        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        subprocess.run(["git", "add", "."], creationflags=DETACHED_PROCESS,
                       startupinfo=subprocess.STARTUPINFO())
        subprocess.run(
            ["git", "commit", "-m", f"An other one {formatted_date} 👆"], creationflags=DETACHED_PROCESS,
            startupinfo=subprocess.STARTUPINFO())
        subprocess.run(["git", "push", "-u", "origin", "master"], creationflags=DETACHED_PROCESS,
                       startupinfo=subprocess.STARTUPINFO())

    with open('green.txt', 'a') as file:
        file.write('Jeremiah 29:11\n')

    def show_notification(title, message):
        toaster = ToastNotifier()
        toaster.show_toast(title, message)

    show_notification("Dear Taki",
                      "Makin' it greener (◕‿◕✿)")


if __name__ == "__main__":
    printing()
