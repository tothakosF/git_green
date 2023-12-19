#
# I want full green github history, but unfortunately I'm lazy af ¯\_(ツ)_/¯
#

import subprocess
from datetime import datetime

current_datetime = datetime.today()

formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)

# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", f"An other one {formatted_date} 👆"])
