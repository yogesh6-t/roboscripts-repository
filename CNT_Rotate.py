#print('Hello world\n')
import webbrowser

url = 'http://docs.python.org/'
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
firefox_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)
#webbrowser.get(firefox_path).open(url)
