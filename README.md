# Linkedin-Profile-Scraper
Small Description: This is a service that scrapes a given linkedin profile for data.

## Welcome to the Linkedin Profile Scraper!


## Novelty:
1. Designed the Frontend and backend for the complete project.
2. Generation of dataset in terms of different fields/categories as obtained from the Profile.
3. Can be used as a micro-service which can fetch data in an analysis software where different profiles are gathered and can be analysed.
4. Can save the data for different persons as csv/JSON files. This can be connected to any database where the data can be stored on the cloud as well.

## Technologies Used: 
1. Flask (Backend) 

![image](https://user-images.githubusercontent.com/42894689/133317407-dc868f47-fbcb-4799-be73-b25313e65b0d.png)

2. HTML (Frontend)  

![image](https://user-images.githubusercontent.com/42894689/133317464-d798e31b-8622-46be-909c-a264e34b7d31.png)

3. CSS (Frontend) 

![image](https://user-images.githubusercontent.com/42894689/133317498-05875c94-9f66-47c4-b2d3-bc5a09d1361b.png)

4. Libraries: BeautifulSoup, Selenium 

![image](https://user-images.githubusercontent.com/42894689/133317874-649fff8e-8acc-48b9-b067-69989eff6c4d.png)
![image](https://user-images.githubusercontent.com/42894689/133317537-b10937d7-5dd2-4748-afff-1b09abe8ab4f.png)


5. Heroku (Hosting wensite)

![image](https://user-images.githubusercontent.com/42894689/133317602-42753fcb-f12e-45b5-8983-715964902754.png)



## Steps Involved:
1. User clicks the Get Started button. 
2. User enters the Linkedin Profile URL. 
3. The scraper will then gather the data for various fields.
4. Finally put the output as a csv file which the user can download.



## UI Screenshots:
![image](https://user-images.githubusercontent.com/42894689/133317187-35e2d357-61e5-4fb6-8236-8bf41a140640.png)
![image](https://user-images.githubusercontent.com/42894689/133317236-7d0d9cfb-5c8e-43c9-95ab-76bd105699d9.png)


## GIF showing the process for a dummy profile link:



## Input example:

![image](https://user-images.githubusercontent.com/42894689/133318495-0a047e95-81f6-43f1-bf17-322cb6063c70.png)


## Output example: 

![image](https://user-images.githubusercontent.com/42894689/133318739-a1a2642e-5024-4893-bf07-2a720f58c758.png)

## Challenges:
1. Completed a 20-hour course on web scraping from Jetbrains.
2. Text cleaning required because the output file was not getting created accurately. Eg: ','s in the csv file seperated the single column entry into different columns. "\n" made single column entry into new row in the excel sheet. 
3. Hosting issue due to selenium's webdriver which was required as a different Heroku specific version. 
4. Needed to read through all the source code of the Profie page's HTML code to find the tags specific to the field we need to extract data to.

## Future Scope:
1. Check for corner case such as wrong profile URL.
2. Extend for different types of browser instead of just Google Chrome.
3. Allow user to input multiple Profile links and output them in a single file.


## Course(s) Undertaken for this project / References:
1. JetBrains NLP Project: Web Scraping using BeautifulSoup (~20 hours project for scraping news articles from a website).
2. BeautifulSoup Documentation


## Recommended Requirements:
1. Good internet conection (about 1 Mbps speed)

## Minimum Requirements:
1. Chrome browser
2. Internet connection (about 2-3 Mbps speed)
3. A working LinkedIn Account
