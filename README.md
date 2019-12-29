# ICSD website Scrapper
[![PyPI version](https://badge.fury.io/py/icsd-scraper.svg)](https://badge.fury.io/py/icsd-scraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c1f9032ce0a94d5faf42007adf8dd087)](https://www.codacy.com/manual/CheatModeON/icsd-scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CheatModeON/icsd-scraper&amp;utm_campaign=Badge_Grade)
![PyPI - License](https://img.shields.io/pypi/l/icsd-scraper)

#### Author: [Achilleas Papakonstantinou] (http://www.icsd.aegean.gr/
#### Date: 26 Dec. 2019
#### ICSD website Scrapper v.0.0.1

## About
Scrapping professors and courses from [ICSD website](http://www.icsd.aegean.gr/icsd/).

This package is very useful for thesis work or other academic projects.

Original idea by [Yannis Alexiou](https://github.com/yannisalexiou). 
Check his implementation in NodeJS [here](https://www.npmjs.com/package/icsd-scraper)

## Usage
Install package:
````
pip install icsd-scraper
````
Import main library:
````
import PapaScrap
````
Retrieve object like so:
````
professors = PapaScrap.getProfessors()

for obj in professors:
    print obj.name
````
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

**⚠️Ιmportant:** `getAdvancedCourses` doesn't always work properly due to lack of consistency of ICSD site. So it's better to use the `getBasicCourses` to retrieve basic course information.
