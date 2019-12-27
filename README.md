# ICSD website Scrapper
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c1f9032ce0a94d5faf42007adf8dd087)](https://www.codacy.com/manual/CheatModeON/icsd-scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CheatModeON/icsd-scraper&amp;utm_campaign=Badge_Grade)

Author: Achilleas Papakonstantinou \
Date: 26 Dec. 2019 \
ICSD website Scrapper v.0000000001

## About
Scrapping professors and courses from [ICSD website](http://www.icsd.aegean.gr/icsd/e)

Original idea by Yannis Alexiou. 
Check his implementation in NodeJS [here](https://www.npmjs.com/package/icsd-scraper)

## Usage
Run script "python PapaScrap.py"
It already includes examples of usages at the end of the code

## Functions 
### getProfessors
Returns all professors as an array of objects with the below details:
**name, academicRank, link, office, tel, email, website, image**

### getBasicCourses
Returns all courses as an array of objects with the below details:
**title, code, semester, ects, theoryHours, labHours, professor, link**

### getAdvancedCourses
Returns all courses as an array of objects with the below details:
**contentOutline, learningOutcomes, prerequisites, basicTextbooks, additionalReferences, teachingMethod, grandingMethod, languageOfInstruction, modeOfDelivery**

**⚠️Ιmportant:** getAdvancedCourses doesn't always work properly due to lack of consistency of ICSD site. So it's better to use the getBasicCourses to retrieve basic course information.
