import requests
from bs4 import BeautifulSoup
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# step-1: Getting required pages from the web. 
url1 = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&ref_=adv_prv"
url2 = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt"
pth = "Imdb_challenge\chromedriver.exe"
driver = webdriver.Chrome(pth)

page1 = requests.get(url1)
#print(page1)
soup1 = BeautifulSoup(page1.content,'html.parser')


page2 = requests.get(url2)
#print(page2)
soup2 = BeautifulSoup(page2.content,'html.parser')

# step-2: scraping movie names
def movie_name(x):
    m_name = x.find_all('div', class_ = "lister-item-content")
    movie_name_list = []
    for i in m_name:
        name = i.a.text.strip()
        movie_name_list.append(name)
    return(movie_name_list)

first50_movie_names = movie_name(soup1)
second50_movie_names = movie_name(soup2)

total100_movie_names = first50_movie_names+second50_movie_names
#print(len(total100_movie_names))

# step-3: Scraping movie description
def movie_description(x):
    m_description = x.find_all('p',class_ = "text-muted")
    movie_description_list = []
    for i in m_description:
        description = i.text.strip()
        movie_description_list.append(description)

    movie_description_list =  movie_description_list[1::2] 
    return movie_description_list
    

first50_movie_descriptions = movie_description(soup1)
second50_movie_descriptions = movie_description(soup2)

total100_movie_descriptions = first50_movie_descriptions+second50_movie_descriptions
#print(total100_movie_descriptions[50])

# step-4: Scraping Release Dates by selenium.
driver.get(url1)
link_class = driver.find_element_by_class_name("lister-item-header")
date_link_tags_50 = link_class.find_element_by_tag_name("a")
new_link1 = date_link_tags_50.click()
driver.implicitly_wait(5)
date_page = new_link1.find_element_by_class_name("ipc-inline-list__item")
rel_test_date = date_page.find_element_by_tag_name("a")
print(rel_test_date.text)
# real_date = driver.
# print(real_date.text)
# # r_date_f = real_date.text
# print(r_date_f)





# def movie_release_dates(x):
#     driver.get(x)
#     release_date_list = []
#     initial_date_links = []
#     link1 = driver.find_elements_by_class_name("lister-item-header")
#     for i in link1:
#         date_link_tag = i.find_elements_by_tag_name("a")
#         for j in date_link_tag:
#             initial_date_links.append(j.get_attribute("href"))
#     driver.implicitly_wait(10)
    
#     for k in initial_date_links:
#         k.click()
#         rel_dates = driver.find_elements_by_xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[11]/div[2]/ul/li[1]/div/ul/li/a/text()")
#         release_date_list.append(rel_dates)
#     return release_date_list

# first_dates = movie_release_dates(url1)
# print(first_dates)

#     link1 = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[1]/div[3]/h3/a')
#     for i in link1:
#         i.click()
#         rd_link = driver.find_element_by_xpath('/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[11]/div[2]/ul/li[1]/div/ul/li/a')
#         rd_link.click()
#         rd_final = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody/tr[10]/td[2]')
#         r_dates = rd_final.text
#         release_date_list.append(r_dates)
#         driver.back()
#         driver.back()
#     return(release_date_list)
# first50_release_dates = movie_release_dates(url1)
# print(first50_release_dates)



