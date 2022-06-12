# TEAM MOD #
Project for the Athena Hackathon 2022.
# Problem #
Refugees coming to the UK may not have the cultural context or written English skillset to succeed in job applications. We created a platform to allow refugees to post questions and have volunteers with whom they share a common language help them. 

Since we cannot assume refugees have access to external technology, we aim to make a website that can be accessed on public infrastructure, such as a library computer. Standard account creation mechanisms require an email address within the process, which refugees may not have. For our platform, we provide a selection of charities with an invite code and bank of simple username-password pairs which they provide to the refugees as a signposting tool. Volunteers can register with an email account, since they are likely to have this kind of technology available.

Since refugees are often multi-lingual, we recognise the opportunity for voluntees to communicate with them in a common other language. This broadens the bank of volunteers who can help the refugees. 

Refugees are vulnerable. It is therefore crucial that the messages are moderated by a trusted set of users to prevent any explitation that could occur from a totally free platform.

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
