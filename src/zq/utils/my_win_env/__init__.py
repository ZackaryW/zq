
import datetime
import os
from zq.utils import ZQ_HOME


MY_WIN_ENV = ZQ_HOME / "my_win_env"

REPO_URL = "https://github.com/ZackaryW/my-windows-env"


def update_repo():
        
    if not MY_WIN_ENV.exists():
        os.system("git clone " + REPO_URL + " " + str(MY_WIN_ENV))
    # if modified more than 10 minutes ago, pull latest changes
    elif (os.path.getmtime(MY_WIN_ENV) + 600) < datetime.datetime.now().timestamp():
        curr_cwd = os.getcwd()
        os.chdir(str(MY_WIN_ENV))
        os.system("git pull")
        os.chdir(curr_cwd)

update_repo()