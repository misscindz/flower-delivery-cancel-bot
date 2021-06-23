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
2. Add credentials to project folder and fill in your freddies flowers login data
      ```sh
   echo -e "emailFromConfig = 'USER_NAME'\npasswordFromConfig = 'PASSWORD'" >> credentials.py
   ```