
from selenium import webdriver

chromedriver = "C:/node/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_elements_by_css_selector('span._19RFN[title="{}"]'.format(name))[0]
print(user)
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()
