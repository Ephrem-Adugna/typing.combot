# pytypingdotcom
# A typing.com typer made with python

## **Software needed**:
* Python 3.76
* Pip installed through Anaconda
## **To run:**
1. ### Download packages via pip:
    ```bash 
    pip install selenium 
    pip install pynput
    ```
2. ### Set up the chrome driver:
    * Download the chrome driver here: https://chromedriver.chromium.org/
    * Replace line 13, or
    ```python
    browser = webdriver.Chrome(
    'Path to chrome driver', chrome_options=chrome_options)
    ```
    with the path to the chromedriver you installed.
3. ### Line 13, or where it says
     ```python
    browser.get(r'file://C:\Users\Yoseph\CSMS\Projects\PyTyping\SchoolBots\typing.combot\typing.html')
    ```
    ### everything from C:\Users\Yoseph\CSMS\Projects\PyTyping\SchoolBots\ should be replaced to the path where you have the bot. 
4. ### Run! (If you encounter any issues, make an issue and it should be fixed.)

## P.S. Keep in mind the bot takes a bit of time to run, so please be patient. 

## How to make the bot faster or slower:
* You can change the delay integer to a smaller or larger number to make the delay between every letter typed shorter or longer.