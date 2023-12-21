import subprocess
from datetime import datetime
from win10toast import ToastNotifier
import random
import time

DETACHED_PROCESS = 0x00000008


def printing():
    with open('green.txt', 'a') as file:
        file.write('Jeremiah 29:11\n')

    formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subprocess.run(["git", "add", "."], creationflags=DETACHED_PROCESS,
                   startupinfo=subprocess.STARTUPINFO())
    subprocess.run(
        ["git", "commit", "-m", f"An other one {formatted_date} 👆"], creationflags=DETACHED_PROCESS,
        startupinfo=subprocess.STARTUPINFO())
    subprocess.run(["git", "push", "-u", "origin", "master"], creationflags=DETACHED_PROCESS,
                   startupinfo=subprocess.STARTUPINFO())

    def show_notification(title, message):
        toaster = ToastNotifier()
        toaster.show_toast(title, message)

    show_notification("Dear Taki",
                      "Makin' it greener (◕‿◕✿)")


if __name__ == "__main__":
    printing()

    while (True):
        rnd = random.randint(2000, 6000)

        with open('green.txt', 'a') as file:
            file.write('Jeremiah 29:11\n')

        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        subprocess.run(["git", "add", "."], creationflags=DETACHED_PROCESS,
                       startupinfo=subprocess.STARTUPINFO())
        subprocess.run(
            ["git", "commit", "-m", f"An other one {formatted_date} 👆"], creationflags=DETACHED_PROCESS,
            startupinfo=subprocess.STARTUPINFO())
        subprocess.run(["git", "push"], creationflags=DETACHED_PROCESS,
                       startupinfo=subprocess.STARTUPINFO())

        time.sleep(rnd)
