from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

CompName = []
DescriptionList = []
TechStackList = []
TopicsList = []
LinkList = []


url = 'https://summerofcode.withgoogle.com/programs/2022/organizations/'
crdriverpath = '/Users/rishipoonia/Downloads/chromedriver'
driver = webdriver.Chrome(crdriverpath)
driver.get(url)
time.sleep(5)
driver.execute_script("window.scrollTo(0,600);")
time.sleep(4)
driver.find_element(By.XPATH, '//div[@class="mat-form-field-flex ng-tns-c87-2"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//mat-option[@id="mat-option-3"]').click()
time.sleep(2)
cards = driver.find_elements(By.XPATH, '//div[@class="org-wrapper"]')
for card in cards:
    Company = card.find_element(By.CLASS_NAME, 'name').text
    Description = card.find_element(By.CLASS_NAME, 'short-description').text + ". "
    tempurl = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    tempdriver = webdriver.Chrome(crdriverpath)
    tempdriver.get(tempurl)
    time.sleep(4.5)
    Full_Descrip = tempdriver.find_element(By.XPATH, '//div[@class="bd"]').text
    if '.' in Full_Descrip:
        Description = Description + Full_Descrip[0:Full_Descrip.index(".")+1]
    else:
        Description = Description + Full_Descrip
    TechStack = tempdriver.find_element(By.XPATH, '//div[@class="tech__content"]').text
    Topics = tempdriver.find_element(By.XPATH, '//div[@class="topics__content"]').text
    Moreinfo = tempdriver.find_element(By.XPATH, '//a[@class="link"]').text
    tempdriver.quit()
    CompName.append(Company)
    DescriptionList.append(Description)
    TechStackList.append(TechStack)
    TopicsList.append(Topics)
    LinkList.append(Moreinfo)
    print(f"Company Name : {Company}")
    print(f"Brief Description : {Description}")
    print(f"Tech Stack : {TechStack}")
    print(f"Topics : {Topics}")
    print(f"For more info : {Moreinfo}\n")

driver.find_element(By.XPATH, '//button[@aria-label="Next page"]').click()
time.sleep(5)

cards = driver.find_elements(By.XPATH, '//div[@class="org-wrapper"]')
for card in cards:
    Company = card.find_element(By.CLASS_NAME, 'name').text
    Description = card.find_element(By.CLASS_NAME, 'short-description').text + ". "
    tempurl = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    tempdriver = webdriver.Chrome(crdriverpath)
    tempdriver.get(tempurl)
    time.sleep(4.5)
    Full_Descrip = tempdriver.find_element(By.XPATH, '//div[@class="bd"]').text
    Description = Description + Full_Descrip[0:Full_Descrip.index(".") + 1]
    TechStack = tempdriver.find_element(By.XPATH, '//div[@class="tech__content"]').text
    Topics = tempdriver.find_element(By.XPATH, '//div[@class="topics__content"]').text
    Moreinfo = tempdriver.find_element(By.XPATH, '//a[@class="link"]').text
    tempdriver.quit()
    CompName.append(Company)
    DescriptionList.append(Description)
    TechStackList.append(TechStack)
    TopicsList.append(Topics)
    LinkList.append(Moreinfo)
    print(f"Company Name : {Company}")
    print(f"Brief Description : {Description}")
    print(f"Tech Stack : {TechStack}")
    print(f"Topics : {Topics}")
    print(f"For more info : {Moreinfo}\n")


DataFile = pd.DataFrame({'Name': CompName, 'Description': DescriptionList, 'Tech_Stack': TechStackList, 'Topics': TopicsList, 'Link': LinkList})
DataFile.to_json("GSOC_json.txt")

driver.quit()
