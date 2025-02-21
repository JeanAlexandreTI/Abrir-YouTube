# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# %%

driver = webdriver.Chrome()

#Abrir Youtube
driver.get('https://www.youtube.com/')


#Pesquisar o nome de um canal
sleep(2)
open_youtube = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/form/input')
open_youtube.click()
sleep(3)
open_youtube.send_keys('Mundo 3 de Python - Guanabara Curso em Video')
sleep(2)
search = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/button/yt-icon/span/div')
search.click()
sleep(2)

start_video = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/yt-lockup-view-model[1]/div/a/yt-collection-thumbnail-view-model/yt-collections-stack/div/div[3]/yt-thumbnail-view-model/div/img')
start_video.click()