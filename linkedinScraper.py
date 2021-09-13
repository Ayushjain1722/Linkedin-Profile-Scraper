import requests
import random, os, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
import json

def signIn():
    browser = webdriver.Chrome('.\driver\chromedriver')
    browser.maximize_window()
    browser.get('https://www.linkedin.com/uas/login')

    #Open The file with the credentials
    file = open('./config.txt')
    lines = file.readlines()
    username = lines[0]
    password = lines[1]

    elementId = browser.find_element_by_id('username')
    elementId.send_keys(username)

    elementId = browser.find_element_by_id('password')
    elementId.send_keys(password)

    elementId.submit()

    return browser

def getProfilePage(browser):
    browser.get('https://www.linkedin.com/in/ayush1722/')
    print("Waiting for the page to load completely")


    SCROLL_PAUSE_TIME = 5
    last_height = 0
    for i in range(7):
        browser.execute_script("window.scrollTo(0, %d)"%last_height)
        last_height += 500
        time.sleep(SCROLL_PAUSE_TIME)


    src = browser.page_source
    soup = BeautifulSoup(src, 'html.parser')

    browser.close()
    return soup

def getName(soup):
    #Get the person's name
    name_div = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    name = name_div.text
    return name

def getHeadline(soup):
    #Get the person's headline
    headline_div = soup.find('div', {'class': 'text-body-medium break-words'})
    headline = " ".join(headline_div.text.split())
    return headline

def getNoOfConnections(soup):
    #Get the number of connectios of the person
    connections_div = soup.find('ul', {'class': 'pv-top-card--list pv-top-card--list-bullet display-flex pb1'})
    connections = " ".join(connections_div.li.a.span.span.text.split())
    return connections

def getSummary(soup):
    #Get the person's summary
    summary_div = soup.find('section', {'class': 'pv-profile-section pv-about-section artdeco-card p5 mt4 ember-view'})
    summary = " ".join(summary_div.div.text.split())
    summary = summary.replace(',', ' ')
    return summary

def getExperience(soup):
    #Get person's experience section
    experiences_div = soup.find_all('a', {'data-control-name': 'background_details_company'})
    experiences = []
    for experience in experiences_div:
        experiences.append((" ".join(experience.text.split())).replace(',', ' '))
    return "\t".join(experiences)

def getEducation(soup):
    #Get person's education section
    educations_div = soup.find_all('a', {'data-control-name': 'background_details_school'})
    educations = []
    for education in educations_div:
        educations.append((" ".join(education.text.split())).replace(',',' '))
    return "\t".join(educations)

def getCertificates(soup):
    #Get person's most recent certifications section
    certifications_div = soup.find_all('a', {'data-control-name': 'background_details_certification'})
    certifications = []
    for certification in certifications_div:
        certifications.append(" ".join(certification.text.split()))
    return "\t".join(certifications)

def getSkills(soup):
    #Get person's top skills section
    skills_div = soup.find_all('span', {'class': 'pv-skill-category-entity__name-text t-16 t-black t-bold'})
    skills = []
    for skill in skills_div:
        skills.append(" ".join(skill.text.split()))
    return "\t".join(skills)

# def getRecommendations(soup):
#     #Get person's recommendations
#     recommendations_div = soup.find_all('blockquote', {'class': 'pv-recommendation-entity__text relative'})
#     recommendations = []
#     print(recommendations_div)
#     return recommendations


#Get the profiles of people also viewed section


browser = signIn()
soup = getProfilePage(browser)
name = getName(soup)
headline = getHeadline(soup)
connections = getNoOfConnections(soup)
summary = getSummary(soup)
experiences = getExperience(soup)
educations = getEducation(soup)
certifications = getCertificates(soup)
skills = getSkills(soup)
# recommendations = getRecommendations(soup)

print("Name: " + name)
print("Headline: " + headline)
print("Connections: " + connections)
print("Summary: " + summary)
print("Experiences: " + str(experiences))
print("Educations: " + str(educations))
print("Certifications: " + str(certifications))
print("Skills: " + str(skills))
# print("Recommendations: " + str(recommendations))

#Store all the results in a csv file
results_csv = open(f'{name}.csv', 'w', encoding='utf-8')
results_csv.write("Name, Headline, Connections, Summary, Experiences, Educations, Certifications, Skills\n")
results_csv.write(name + "," + headline + "," + connections + "," + summary + "," + str(experiences) + "," + str(educations) + "," + str(certifications) + "," + str(skills))

#Store all the results in a JSON file
results_json = open(f'{name}.json', 'w', encoding='utf-8')
results_json.write(json.dumps({"Name": name, 
                               "Headline": headline, 
                               "Connections": connections, 
                               "Summary": summary, 
                               "Experiences": experiences, 
                               "Educations": educations, 
                               "Certifications": certifications, 
                               "Skills": skills}))