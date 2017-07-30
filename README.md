# ingatlan-kereso
Ingatlan.com scraper to list and store 

It's a personal apartment search tool, which helps you to search and track apartments.

# How to setup and run

### 1. Setup your environment

- Make sure you installed python3 on OS X - [howto](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
- You install the dependencies with `pip install -r requirements.txt`

### 2. Get Google Sheets access

To programmatically access your spreadsheet, you’ll need to create a service account and OAuth2 credentials from the Google API Console. If you’ve been traumatized by OAuth2 development before, don’t worry; service accounts are way easier to use.

- Go to the [Google APIs Console](https://console.developers.google.com/).
- Create a new project.
- Click *Enable API*. Search for and enable the Google Drive API.
- *Create credentials* for a *Web Server* to access *Application Data*.
- Name the service account and grant it a *Project* Role of *Editor*.
- Download the JSON file.
- Copy the JSON file to your code directory and rename it to `client_secret.json`

HowTo GIF: https://www.twilio.com/blog/wp-content/uploads/2017/02/google-developer-console.gif

### 3. Get Google Distance Matrix API key

- Open [Distance Matrix API page](https://developers.google.com/maps/documentation/distance-matrix/)
- Click *GET A KEY* and select your project which you created in Step2
- Copy `ingatlan_kereso_secrets-template.py` to `ingatlan_kereso_secrets.py` and add this API key to `GOOGLE_MAPS_DISTANCE_MATRIX_API_KEY`
- Fill `WORK_PLACE` with your workplace location

### 4. Create a Google Sheet for the results

- Copy [this template](https://docs.google.com/spreadsheets/d/1amDZaunjAGld6JRCoIpNg4sxNu-mHLQkDGbHmVx5_iY/edit?usp=sharing) and rename to `ingatlan-kereso`

![ScreenShot](https://raw.githubusercontent.com/CsabaSzabo/ingatlan-kereso/master/readme-images/ingatlan-kereso-template.jpg)

- Add new searches to *Keresések* sheet
  - *Column A* defines the index of the sheet in the `ingatlan-kereso` file
  - *Column B* defines the ingatlan.com search URL
  - *Column C* defines the name of the search
  - *Column D* defines if it's a flat or a house (haz/lakas), it needed for data parsing
- You could add a 3rd search if you add a new row and you create a new sheet into the file which is the 4th sheet in the file (the order of the sheets are important)

### 5. Run the script
Run the script with `python3 ingatlan-kereso.py`, read the output and check your Google Sheet results :)
