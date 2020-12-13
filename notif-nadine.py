#!pip install selenium
#!apt-get update # to update ubuntu to correctly run apt install
#!apt install chromium-chromedriver
#!cp /usr/lib/chromium-browser/chromedriver /usr/bin

# config starts here #
username = '' # fill with nadine username
password = '' # fill with nadine password
pushbullet_token = '' # fill with pushbullet.com token
# end of config #

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from datetime import datetime
from pytz import timezone

# Pushbullet
def pushbullet_message(title, body):
    import requests
    msg = {"type": "note", "title": title, "body": body}
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + pushbullet_token,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent') 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get("https://office.kemenkeu.go.id/")
driver.implicitly_wait(5) # seconds
assert "Login" in driver.page_source, "Link login gak ketemu boss"

driver.find_element_by_xpath("//a[contains(text(), 'Login')]").click()
# implisit wait tidak konsisten, kadang error kadang sukses
assert "login100-form" in driver.page_source, "Login form gak ketemu boss"
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('button').click()
driver.implicitly_wait(5) # seconds
driver.get("https://office.kemenkeu.go.id/api/Absensi/daily")
pre = driver.find_element_by_tag_name("pre").text
data = json.loads(pre) # get first key of dict
print(data)
tanggal = next(iter(data))
print(tanggal)
if data[tanggal]['In'] == None:
    jam_masuk = 'belum absen'
else:
    jam_masuk = data[tanggal]['In']['CreatedAt'].split('T')[1]

if data[tanggal]['Out'] == None:
    jam_pulang = 'belum absen'
else:
    jam_pulang = data[tanggal]['Out']['CreatedAt'].split('T')[1]

pushbullet_message("Cek Nadine", "Tgl " + tanggal + ": Absen pagi jam " + jam_masuk + ", absen pulang jam " + jam_pulang)
