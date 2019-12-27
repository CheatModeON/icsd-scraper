#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Achilleas Papakonstantinou
# ICSD website Scrapper v.0000000001
# Scrapping professors and courses from http://www.icsd.aegean.gr/icsd/
# Original idea by Yannis Alexiou. Check his implementation in NodeJS here: https://www.npmjs.com/package/icsd-scraper

import requests
from bs4 import BeautifulSoup
import time

class Professor(object):
        def __init__(self, name, rank, link, office, tel, email, website, image_link):
                self.name = name
                self.rank = rank
                self.link = link
                self.office = office
                self.tel = tel
                self.email = email
                self.website = website
                self.image_link = image_link

class BasicCourse(object):
        def __init__(self, title, code, semester, ects, theoryHours, labHours, professor, link):
                self.title = title
                self.code = code
                self.semester = semester
                self.ects = ects
                self.theoryHours = theoryHours
                self.labHours = labHours
                self.professor = professor
                self.link = link

class AdvancedCourse(object):
        def __init__(self, contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences,
		     teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery):
                self.contentOutline = contentOutline
                self.learningOutcomes = learningOutcomes
                self.prerequisites = prerequisites
                self.basicTextbooks = basicTextbooks
                self.additionalReferences = additionalReferences
                self.teachingMethod = teachingMethod
                self.grandingMethod = grandingMethod
                self.languageOfInstruction = languageOfInstruction
                self.modeOfDelivery = modeOfDelivery
                
def getProfessors():
        html_data = ''
	resp = requests.get('http://www.icsd.aegean.gr/icsd/akadimaiko')
	if resp.ok:
		html_data = resp.text
	else:
		print ("Error! {}".format(resp.status_code))
		print (resp.text)
		
	soup = BeautifulSoup(html_data, 'html.parser')

	href_anap = []
	href_kath = []
	href_epik = []
	href_mepik = []
	
	all_anaplirotis = soup.select('.anaplirotis a')
	for a in all_anaplirotis:
		href_anap.append(a['href'])
	all_kathigitis = soup.select('.kathigitis a')
	for a in all_kathigitis:
		href_kath.append(a['href'])
	all_epikouros = soup.select('.epikouros a')
	for a in all_epikouros:
		href_epik.append(a['href'])
	all_mepikouros = soup.select('.mepikouros a')
	for a in all_mepikouros:
		href_mepik.append(a['href'])


	#print("name\t\t\t\t | rank\t\t | link\t\t | office\t\t | tel\t\t | email\t\t | website\t\t | image_link")

        professors = [] # object to return
	count_all = len(href_anap)+len(href_kath)+len(href_epik)+len(href_mepik)
	href_all = href_anap + href_kath + href_epik + href_mepik
	for i in range(0, count_all):
                
		resp = requests.get('http://www.icsd.aegean.gr/icsd/' + href_all[i])
		if resp.ok:
			html_data = resp.text
		else:
			print ("Error! {}".format(resp.status_code))
			print (resp.text)

		soup = BeautifulSoup(html_data, 'html.parser')

                #name
		name = soup.find('span', class_ = 'm-card-profile__name').get_text()
                #rank
                academicRank = soup.find("a", {"class": "m-card-profile__email"}).get_text()
                #link
		link = 'http://www.icsd.aegean.gr/icsd/' + href_all[i]
                #office
		office = soup.find_all('span', class_ = 'm-nav__link-text-leo')[2].get_text()
                #tel
		tel = soup.find_all('span', class_ = 'm-nav__link-text-leo')[1].get_text()
                #email
		email = soup.find('span', class_ = 'm-nav__link-text-leo').get_text()
                #website
                li = soup.find_all("ul", {"class": "m-nav"})[3]
                children = li.findChildren("a" , recursive=True)
                website = (children[3].attrs['href'])
		#citations
		#citations = (children[4].attrs['href'])
		#image
                img_data = soup.find("div", {"class": "m-card-profile__pic-leo"})
                image_link = img_data.find('img')['src']

                professors.append(Professor( name, academicRank, link, office, tel, email, website, image_link))
                #print("" +name+ "\t\t | " +academicRank+ "\t | "+link+"\t | "+office+"\t | "+tel+"\t | "+email+"\t | "+website+"\t | "+image_link)

        return professors

def getBasicCourses():
        resp = requests.get('http://www.icsd.aegean.gr/icsd/pps')
	if resp.ok:
		html_data = resp.text
	else:
		print ("Error! {}".format(resp.status_code))
		print (resp.text)

	soup = BeautifulSoup(html_data, 'html.parser')
        tables = soup.find_all( "table", {"class":"lessontable"} )

        courses_href = []
        for table in tables:
                for row in table.findAll("tr"):
                        wow = row.findChildren()[1]
                        if(wow.findChild("a" , recursive=True) is not None):
                                courses_href.append(wow.findChild("a" , recursive=True).attrs['href'])

        
	#print("title\t\t\t\t | code\t\t | semester\t\t | ects\t\t | theoryHours\t\t | labHours\t\t | professor\t\t | link")

        basic_courses = []; #object to return
        for i in range(0, len(courses_href)):
                
                resp = requests.get('http://www.icsd.aegean.gr/icsd/'+courses_href[i])
                if resp.ok:
                        html_data = resp.text
                else:
                        print ("Error! {}".format(resp.status_code))
                        print (resp.text)

                soup = BeautifulSoup(html_data, 'html.parser')

                table = soup.find( "table", {"class":"table m-table m-table--head-separator-primary table-bordered table-hover"} )

                all_data = table.findAll("tr")
                
                title = all_data[0].findChildren()[2].text
                
                code = all_data[1].findChildren()[2].text
                
                semester = all_data[2].findChildren()[2].text
                
                ects = all_data[3].findChildren()[2].text
                
                theoryHours = all_data[4].findChildren()[2].text
                
                labHours = all_data[5].findChildren()[2].text
                
                professor = all_data[6].findChildren()[2].text
                            
                link = 'http://www.icsd.aegean.gr/icsd/'+courses_href[i]

                basic_courses.append(BasicCourse(title, code, semester, ects, theoryHours, labHours, professor, link))
                #print("" +title+ "\t\t | " +code+ "\t | "+semester+"\t | "+ects+"\t | "+theoryHours+"\t | "+labHours+"\t | "+professor+"\t | "+link)

        return basic_courses

def getAdvancedCourses():
        resp = requests.get('http://www.icsd.aegean.gr/icsd/pps')
	if resp.ok:
		html_data = resp.text
	else:
		print ("Error! {}".format(resp.status_code))
		print (resp.text)

	soup = BeautifulSoup(html_data, 'html.parser')
        tables = soup.find_all( "table", {"class":"lessontable"} )

        courses_href = []
        for table in tables:
                for row in table.findAll("tr"):
                        wow = row.findChildren()[1]
                        if(wow.findChild("a" , recursive=True) is not None):
                                courses_href.append(wow.findChild("a" , recursive=True).attrs['href'])


        advanced_courses = []; #object to return
        for href in courses_href:
                
                resp = requests.get('http://www.icsd.aegean.gr/icsd/'+href)
                if resp.ok:
                        html_data = resp.text
                else:
                        print ("Error! {}".format(resp.status_code))
                        print (resp.text)

                soup = BeautifulSoup(html_data, 'html.parser')

                #table = soup.find( "table", {"class":"table m-table m-table--head-separator-primary table-bordered table-hover"} )

                #all_data = table.findAll("tr")
                
                #title = all_data[0].findChildren()[2].text
                
                #code = all_data[1].findChildren()[2].text
                
                #semester = all_data[2].findChildren()[2].text
                
                #ects = all_data[3].findChildren()[2].text
                
                #theoryHours = all_data[4].findChildren()[2].text
                
                #labHours = all_data[5].findChildren()[2].text
                
                #professor = all_data[6].findChildren()[2].text
                
                #link = 'http://www.icsd.aegean.gr/icsd/'+courses_href[i]
                
                #print("" +title+ "\t\t | " +code+ "\t | "+semester+"\t | "+ects+"\t | "+theoryHours+"\t | "+labHours+"\t | "+professor+"\t | "+link)

                
                #courseWebsite = 'http://www.icsd.aegean.gr/icsd/'+courses_href[i]

                divs = soup.find_all( "div", {"class":"m-portlet__body"} )
                
                contentOutline = ''
                children = divs[1].findChildren()
                for child in children:
                        contentOutline = contentOutline + (child.text)

                learningOutcomes = ''
                children = divs[2].findChildren()
                for child in children:
                        learningOutcomes = learningOutcomes + (child.text)
                        
                prerequisites = divs[3].text

                basicTextbooks = ''
                children = divs[4].findChildren()
                for child in children:
                        basicTextbooks = basicTextbooks + (child.text)
                
                additionalReferences = ''
                children = divs[5].findChildren()
                for child in children:
                        additionalReferences = additionalReferences + (child.text)

                teachingMethod = ''
                children = divs[6].findChildren()
                for child in children:
                        teachingMethod = teachingMethod + (child.text)

                grandingMethod = ''
                children = divs[7].findChildren()
                for child in children:
                        grandingMethod = grandingMethod + (child.text)

                languageOfInstruction = ''
                children = divs[8].findChildren()
                for child in children:
                        languageOfInstruction = languageOfInstruction + (child.text)

                modeOfDelivery = ''
                children = divs[9].findChildren()
                for child in children:
                        modeOfDelivery = modeOfDelivery + (child.text)

                advanced_courses.append(AdvancedCourse(contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences,
						       teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery))

                #print('________________________________________________________________________\n')

        return advanced_courses


# TESTIN'

start_time = time.time()

# test professors
print('\n______________ Professors Test ______________')
professors = getProfessors()

for obj in professors:
    print obj.name


# test basic courses
print('\n______________ Basic Courses Test ______________')
basic_courses = getBasicCourses()

for obj in basic_courses:
    print obj.title


# test advanced courses
print('\n______________ Advanced Courses Test ______________')
#advanced_courses = getAdvancedCourses()

#for obj in advanced_courses:
#    print obj.contentOutline


elapsed_time = time.time() - start_time

print("Elapsed Time:" + str(elapsed_time))


