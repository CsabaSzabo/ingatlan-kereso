# ingatlan-kereso
Ingatlan.com scraper to list and store 

It's a personal apartment search tool, which helps you to search and track apartments.

# How to setup your environment
- Make sure you installed python3 on OS X - [howto](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
- You install the dependencies with `pip install -r requirements.txt`

# How to access Google Sheets programatically

To programmatically access your spreadsheet, you’ll need to create a service account and OAuth2 credentials from the Google API Console. If you’ve been traumatized by OAuth2 development before, don’t worry; service accounts are way easier to use.

- Go to the [Google APIs Console](https://console.developers.google.com/).
- Create a new project.
- Click *Enable API*. Search for and enable the Google Drive API.
- *Create credentials* for a *Web Server* to access *Application Data*.
- Name the service account and grant it a *Project* Role of *Editor*.
- Download the JSON file.
- Copy the JSON file to your code directory and rename it to `client_secret.json`

HowTo GIF: https://www.twilio.com/blog/wp-content/uploads/2017/02/google-developer-console.gif


# How to run
- you create a `client_secret.json` from Google (it's added to .gitignore) - howto
- you copy this Google Sheets template, share it and get the ID of it
- you copy `ingatlan_kereso_secrets-template.py` to `ingatlan_kereso_secrets.py` and fill the API keys and IDs
- run the script with `python ingatlan-kereso.py`

