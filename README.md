# TEAM MOD #
Project for the Athena Hackathon 2022.
# Problem #
Refugees coming to the UK may not have the cultural context or the best grasp of the English language.

# Users #

| Username | Password | Type |
| --- | --- | --- |
| athena | athena | administrator (superuser) |
| kiwi | tasty_kiwi | refugee |

# Expected Interactions #
Below are interactions a user who runs a Windows 10 host should expect.

## Environment Setup ##
Client downloads most recent versions of Python, pip, and git. They run the commands from Powershell (note: Command Line should also work).
```powershell
# clone the project
git clone https://github.com/cyberliv/athena2022_language_project.git
cd athena2022_language_project
# update packages to match project requirements
py -3 -m pip install -r requirements.txt
```

## Hosting the App ##
```powershell

# update db
py -3 manage.py makemigrations webApp
# make db
py -3 manage.py migrate
# run server
py -3 manage.py runserver
```
Navigate to `127.0.0.1` on a browser to interact with the landing page.

To stop the server, either close powershell with the GUI, or press `ctrl + c`.