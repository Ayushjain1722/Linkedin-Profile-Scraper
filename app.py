from flask import Flask, render_template, request, send_file
import linkedinScraper as lScraper
import json
import time

app = Flask(__name__)
url = ""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=["GET", "POST"])
def getURL():
    global url
    if request.method == "POST":
        url = request.form.get('url')

        browser = lScraper.signIn()
        soup = lScraper.getProfilePage(browser, url)
        name = lScraper.getName(soup)
        headline = lScraper.getHeadline(soup)
        connections = lScraper.getNoOfConnections(soup)
        summary = lScraper.getSummary(soup)
        experiences = lScraper.getExperience(soup)
        educations = lScraper.getEducation(soup)
        certifications = lScraper.getCertificates(soup)
        skills = lScraper.getSkills(soup)

        # print("Name: " + name)
        # print("Headline: " + headline)
        # print("Connections: " + connections)
        # print("Summary: " + summary)
        # print("Experiences: " + str(experiences))
        # print("Educations: " + str(educations))
        # print("Certifications: " + str(certifications))
        # print("Skills: " + str(skills))

        results_csv = open(f'outputs/{name}.csv', 'w', encoding='utf-8')
        results_csv.write("Name, Headline, Connections, Summary, Experiences, Educations, Certifications, Skills\n")
        results_csv.write(name + "," + headline + "," + connections + "," + summary + "," + str(experiences) + "," + str(educations) + "," + str(certifications) + "," + str(skills))
        time.sleep(5)
        file_to_be_sent = open(f"outputs/{name}.csv", 'rb')
        return send_file(file_to_be_sent, attachment_filename=f'{name}.csv', as_attachment=True)
        # results_json.write(json.dumps({"Name": name, 
        #                                "Headline": headline, 
        #                                "Connections": connections, 
        #                                "Summary": summary, 
        #                                "Experiences": experiences, 
        #                                "Educations": educations, 
        #                                "Certifications": certifications, 
        #                                "Skills": skills}))

        # #Give the download file
        # return send_file(f'outputs/{name}.json', attachment_filename=f'{name}.json', as_attachment=True)



    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)