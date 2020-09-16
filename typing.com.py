from selenium import webdriver              
from pynput.keyboard import Key, Controller
import time                 
keyboard = Controller()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


def split(word):
    return [char for char in word]
delay = .2
browser = webdriver.Chrome(
    'Path to chrome driver', chrome_options=chrome_options)
typeoftest = input("""What type of test is it?
  1. Horizontal letters
  2. Paragraph Typing 
  3. Falling Letters 
  4. Just Type
  Please type the number you want.""")
Html_file = open("typing.html", "w")
Html_file.close()
if typeoftest != '4':
    done = input(
        '''Please inspect the typing.com assignment,
        and past the html inside a file called typing.html.
        Type done when you are done: ''')
if typeoftest == '2':
    fin = open("typing.html", "r", errors='ignore')
    data = fin.read()
    data = data.replace('&nbsp;', ' ')
    fin.close()
    fin = open("typing.html", "wt", errors='ignore')
    fin.write(data)
    fin.close()
if typeoftest != '4':
    browser.get(r'file://C:\Users\Yoseph\CSMS\Projects\PyTyping\SchoolBots\typing.combot\typing.html')


if typeoftest == '1':

    print('Starting...3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    typing = browser.find_elements_by_class_name('letter--intro')
    amount = len(typing)
    for x in range(amount):
        word = typing[x].get_attribute('innerText')
        if word == '':
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else:
            keyboard.type(word)
        time.sleep(delay)
elif typeoftest == '3':

    print('Starting...3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    typing = browser.find_elements_by_class_name('screenFalling-letter')
    typing.reverse()
    amount = len(typing)
    for x in range(amount):
        keyboard.type(typing[x].get_attribute('innerText'))
        time.sleep(delay)
elif typeoftest == '2':

    print('Starting...3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    typing = browser.find_elements_by_class_name('screenBasic-letter')
    amount = len(typing)

    for x in range(amount):
        wordTotype = typing[x].get_attribute('innerText')
        if wordTotype == '':
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else:
            keyboard.type(wordTotype)
        time.sleep(delay)
elif typeoftest == '4':
    letters = input('Please type what you want to be typed: ')
    print('Starting...3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    letters = split(letters)
    amount = len(letters)

    for x in range(amount):
        keyboard.type(letters[x])
        time.sleep(delay)
