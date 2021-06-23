# Flower Delivery Cancel Bot :bouquet:
This bot logs into your freddiesflowers.de account and unbooks all active flower deliveries of the upcoming four weeks.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [pip](https://pip.pypa.io/en/stable/installing/) (for installing python modules)
* Google Chrome browser
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
* selenium
  ```sh
  pip install selenium
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/misscindz/flower-delivery-cancel-bot
   ```
2. Add login credentials to project folder
   ```sh
   echo -e "emailFromConfig = 'INSERT_YOUR_EMAIL_HERE'\npasswordFromConfig = 'INSERT_YOUR_PASSWORD_HERE'" >> credentials.py
   ```
   Check the output of the generated file
   ```sh
   cat credentials.py

   # output should look like this
   emailFromConfig = 'INSERT_YOUR_EMAIL_HERE'
   passwordFromConfig = 'INSERT_YOUR_PASSWORD_HERE'
   ```
3. Run the bot
   ```sh
   # change file permission
   chmod u+x loginbot.py

   # execute
   ./loginbot.py
   ```