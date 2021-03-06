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

# Features
- Recommends University degrees tailored to your interest
- Filtering Options
- Interactive visuals of the results

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
The app follows the following structure:
- scraping (folder)
  - scraper.py (To scrap the website for study programs)
- data (folder)
  - raw_data.csv
  - processed_data.csv
  - secondary_links.csv
  - stopwords.pkl
  - tfidf_mat.pkl
  - vectorizer.pkl
- web (folder)
  - templates (folder)
    - base.html
    - home.html
    - results.html
  - web_app.ipnyb (Web app)
  - bar1.html
  - sc1_plot.html
- model (folder)
  - data_preparation.ipnyb  (data cleaning and formatting)
  - recommender.ipnyb  (machine learning models)
  - results.pkl (Results retrieved)
- assets (folder)
  - images (static files)

# Machine Learning Pipeline
- Machine Learning Pipeline
  - Web Scraping
    - BeautifulSoup
    - Selenium
  - Machine learning and data analysis
    - HanTa
    - Scikit learn
    - NLTK
  - Data Processing
    - Pandas
    - Pickle
    - TextHero
  - Data Visualisation
    - DataTables
    - matplotlib
    - mpld3
    - Altair

# Visualization
All Visualisation is built using:

**Interactive Table**
***DataTables and Jinja packages***
- Shows the top recommended majors (starting with the best match) and their attributes as well as the cosine similarity value
- Able to browse, sort and filter the results according to your liking
![image](/assets/images/Table.jpg)

Further Visualizations:

**Scatter Plot**
***mpld3 package***

- Shows recommended majors by overall rating and similarity
- Hover over entries or pan within the plot

![image](/assets/images/Scatterplot.jpg)


**Horizontal Bar Chart**
***Altair package***
- shows top recommended programs in an ordered manner and the corresponding cosine similarity value
- using color hue as a legend to distinguish between subcategories that the programs belong to
- Filter displayed majors by language they are taught in via a dropdown-menu
![image](/assets/images/Barchart.jpg)


# Project Deployment
First you need to install below requirements:

- [Download PyCharm(Community Edition)](https://www.jetbrains.com/pycharm/) or your preferred IDE.
- [Download latest version of Anaconda for Jupyter Notebook](https://www.anaconda.com/)
- [Download latest version of Python](https://www.python.org/downloads/)
After configuring the python inside your IDE you need to install this project from this repository.

Then you need to install below requirements on our system:

- altair == 4.2.0
- beautifulsoup4
- datapane == 0.13.2
- flask == 1.1.2
- gensim==3.8.3
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- matplotlib == 3.3.4
- mpld3 == 0.5.7
- numpy == 1.20.1
- pandas == 1.2.4
- pickle
- scikit-learn == 0.24.1
- werkzeug == 1.0.1
- HanTa
- nltk == 3.6.1
- scipy == 1.6.2
- texthero == 1.1.0
- selenium == 4.1.0

# Run Server
In the end you can simply run the web_app.ipynb file and then the server will run on you localhost. Afterwards just open Browser and access http://localhost:5000/ and enjoy the Web Application.

# Contributors
- [Hendrik Eckhoff](https://github.com/Rechtecki)
- [Yasmine Taha Mokhtar](https://github.com/yasmineataha) 
- [Nahid Hosseininezhad](https://github.com/emrys7272/) 
- [Roshan Asim](https://github.com/roshan95)

