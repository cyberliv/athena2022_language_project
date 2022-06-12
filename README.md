# TEAM MOD #
Project for the Athena Hackathon 2022.
# Problem #
Refugees coming to the UK may not have the cultural context or the best grasp of the English language.

## Users ##

| Username | Password |
| --- | --- |
| athena | athena |
| kiwi | tasty_kiwi |

## Expected Interactions ##
Below are interactions a user who runs a Windows 10 host should expect.
```powershell
# clone the project
git clone https://github.com/cyberliv/athena2022_language_project.git
cd athena2022_language_project
# update packages to match project requirements
py -3 -m pip install -r requirements.txt
```


# Hosting the App #
```powershell

# update db
py -3 manage.py makemigrations webApp
# make db
py -3 manage.py migrate
# run server
py -3 manage.py runserver
```