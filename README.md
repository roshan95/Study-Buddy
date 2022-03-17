# Table of content
- [StudyBuddy](https://github.com/roshan95/Study-Buddy#study-buddy)
- [Dataset Description](https://github.com/roshan95/Study-Buddy#dataset-description)
- [Implementation Technologies](https://github.com/roshan95/Study-Buddy#implementation-technologies)
- [App Structure](https://github.com/roshan95/Study-Buddy#app-structure)
- [Code Description](https://github.com/roshan95/Study-Buddy#app-structure)
- [Machine Learning Pipeline](https://github.com/roshan95/Study-Buddy#app-structure)
- [To deploy the project](https://github.com/roshan95/Study-Buddy#machine-learning-pipeline)
- [Visualization](https://github.com/roshan95/Study-Buddy#visualization)
- [Project Deployment](https://github.com/roshan95/Study-Buddy#project-deployment)
- [Contributors](https://github.com/roshan95/Study-Buddy#contributors)

[A Youtube video shows a demo](https://youtu.be/C1BQCV-eyvs)
# Study Buddy
![image](/assets/images/logo.png)
The tool recommends degrees from different universities across Germany to students in pursuit of a bachelor’s or master’s degree. It takes your interest in account along with your preference of language of instruction, degree type, and rating score. All you need to do is type in a word or two and the tool recommends programs that best matches what you like. You can view details of the programs, including a description. Additionally, you can get more insights about the recommendation through interactive visuals.

This project was submited as a final project for  [Learning Analytics](https://www.uni-due.de/soco/teaching/overview.php) course under [Social Computing department](https://www.uni-due.de/soco/) at [Duisburg-Essen University](https://www.uni-due.de).
# Dataset Description
- Multivariate dataset
- It consists of 18 attributes in csv format
- There are 2264 study majors
-The source of dataset is [HERE](https://studycheck.de)
# Implementation Technologies
The project is based on following technologies:
- Front-End
  - Website
    - HTML
    - CSS
    - Jinja

- Back-End
  - Web Server
    - Python
    - Flask


# App Structure


# Machine Learning Pipeline
- Machine Learning Pipeline
  - Web Scraping
    - BeautifulSoup
  - Machine learning and data analysis
    - Scikit learn
  - Data Processing
    - Pandas
  - Data Visualisation
    - matplotlib
    - mpld3
    - Altair
# Visualization
All Visualisation is built using:

- Datatable is provided to show the list of the recommended programs
Example: Recommendation function: To recomment the study programs according to the interest of the user

![image](/assets/images/graphs2.png)

- Scatterplot graph to show recommended majors by overall rating and similarity

![image](/assets/images/graphs1.png)

# Project Deployment
First you need to install below requirements:

- [Download PyCharm(Community Edition)](https://www.jetbrains.com/pycharm/) or your preferred IDE.
- [Download latest version of Python](https://www.python.org/downloads/)
After configuring the python inside your IDE you need to install this project from this repository.

Then you need to install below requirements on our system:

- sci-kit learn == 0.22.1
- Flask == 1.1.1
- Numpy == 1.17.4
- Pandas == 0.25.2
- html5lib == 1.0.1
- pymongo == 3.8.0
- dnspython == 1.16.0

# Run Server
In the end you can simply run the server.py file and then server will run on you localhost. Then just open Browser and access http://localhost:5000/ and enjoy the Web Application.
# Contributors
- [Hendrik Eckhoff](https://github.com/Rechtecki)
- [Yasmine Taha Mokhtar]() 
- [Nahid Hosseininezhad]() 
- [Roshan Asim](https://github.com/roshan95)

