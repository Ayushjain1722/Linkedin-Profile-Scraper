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
    while('feed' not in browser.current_url):
        time.sleep(5)
    print(browser.current_url)
    return browser

def getProfilePage(browser, url):
    browser.get(url)
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
    try:
        name_div = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
        name = name_div.text.split(" ")
        return name[0] + name[1]
    except:
        return "NA"

def getHeadline(soup):
    #Get the person's headline
    try:
        headline_div = soup.find('div', {'class': 'text-body-medium break-words'})
        headline = " ".join(headline_div.text.split())
        return headline.replace(',', ' ')
    except:
        return "NA"

def getNoOfConnections(soup):
    #Get the number of connectios of the person
    try:
        connections_div = soup.find('ul', {'class': 'pv-top-card--list pv-top-card--list-bullet display-flex pb1'})
        connections = " ".join(connections_div.li.a.span.span.text.split())
        return connections
    except:
        return "NA"

def getSummary(soup):
    #Get the person's summary
    try:
        summary_div = soup.find('section', {'class': 'pv-profile-section pv-about-section artdeco-card p5 mt4 ember-view'})
        summary = " ".join(summary_div.div.text.split())
        summary = summary.replace(',', ' ')
        return summary
    except:
        return "NA"

def getExperience(soup):
    #Get person's experience section
    try:
        experiences_div = soup.find_all('a', {'data-control-name': 'background_details_company'})
        experiences = []
        for experience in experiences_div:
            experiences.append((" ".join(experience.text.split())).replace(',', ' '))
        return "\t".join(experiences)
    except: 
        return "NA"

def getEducation(soup):
    #Get person's education section
    try:
        educations_div = soup.find_all('a', {'data-control-name': 'background_details_school'})
        educations = []
        for education in educations_div:
            educations.append((" ".join(education.text.split())).replace(',',' '))
        return "\t".join(educations)
    except:
        return "NA"

def getCertificates(soup):
    #Get person's most recent certifications section
    try:
        certifications_div = soup.find_all('a', {'data-control-name': 'background_details_certification'})
        certifications = []
        for certification in certifications_div:
            certifications.append((" ".join(certification.text.split())).replace(',', ' '))
        return "\t".join(certifications)
    except:
        return "NA"

def getSkills(soup):
    #Get person's top skills section
    try:
        skills_div = soup.find_all('span', {'class': 'pv-skill-category-entity__name-text t-16 t-black t-bold'})
        skills = []
        for skill in skills_div:
            skills.append(" ".join(skill.text.split()))
        return "\t".join(skills)
    except:
        return "NA"

# def getRecommendations(soup):
#     #Get person's recommendations
#     recommendations_div = soup.find_all('blockquote', {'class': 'pv-recommendation-entity__text relative'})
#     recommendations = []
#     print(recommendations_div)
#     return recommendations


#Get the profiles of people also viewed section

# print("Name: " + name)
# print("Headline: " + headline)
# print("Connections: " + connections)
# print("Summary: " + summary)
# print("Experiences: " + str(experiences))
# print("Educations: " + str(educations))
# print("Certifications: " + str(certifications))
# print("Skills: " + str(skills))
# # print("Recommendations: " + str(recommendations))

# #Store all the results in a JSON file
# results_json = open(f'{name}.json', 'w')
# results_json.write(json.dumps({"Name": name, 
#                                "Headline": headline, 
#                                "Connections": connections, 
#                                "Summary": summary, 
#                                "Experiences": experiences, 
#                                "Educations": educations, 
#                                "Certifications": certifications, 
#                                "Skills": skills}))