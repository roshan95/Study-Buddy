from bs4 import BeautifulSoup  # Needed to fetch and analyze html
from selenium.webdriver import Firefox  # Needed to emulate webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # Needed to set webdriver options
import time  # Needed to use sleep()
import csv  # Needed to export links to .csv, if desired
import random  # Needed to randomize wait times between browser requests
import re  # Needed for Regex operations
from decimal import Decimal  # Needed to do percentage calculation

# Set driver options
options = FirefoxOptions()
# Uncomment the following line if browser should open in background
# options.add_argument("--headless")
driver = Firefox()
driver.set_page_load_timeout(60)

# Define column names for data CSV export
column_names = ["is_list", "major_name", "major_description", "studycheck_link", "university_link", "category",
                "subcategory", "major_category", "university", "location", "degree_type", "degree_label", "language",
                "duration_of_study", "rating_amount", "rating", "recommendation_rate"]

# Create new data file with column headers
with open("../data/raw_data.csv", "a", encoding="utf-8") as output:
    writer = csv.writer(output, delimiter=',', lineterminator='\n')
    writer.writerow(column_names)

# Pre-populated list of major categories for first level scraping (from one time study domain scraping below)
main_links = ['https://www.studycheck.de/studium/medizin-gesundheitswesen/seite-',
              'https://www.studycheck.de/studium/medien-kommunikation/seite-',
              'https://www.studycheck.de/studium/wirtschaft-recht/seite-',
              'https://www.studycheck.de/studium/technik-ingenieurwissenschaft/seite-',
              'https://www.studycheck.de/studium/gesellschaftswissenschaften/seite-',
              'https://www.studycheck.de/studium/naturwissenschaften-mathe/seite-',
              'https://www.studycheck.de/studium/sprach-kulturwissenschaften/seite-',
              'https://www.studycheck.de/studium/kunst-gestaltung-musik/seite-',
              'https://www.studycheck.de/studium/informatik-mathematik/seite-',
              'https://www.studycheck.de/studium/agrar-forstwissenschaften/seite-']
# Testing purposes:
# main_links = ['https://www.studycheck.de/studium/agrar-forstwissenschaften/seite-',
# 'https://www.studycheck.de/studium/naturwissenschaften-mathe/seite-']

# List of links for second level scraping
secondary_links = []
with open('../data/secondary_links.csv', newline='') as f:
    for row in csv.reader(f):
        secondary_links.append(row[0])
# Testing purposes:
# secondary_links = ["https://www.studycheck.de/studium/informatik/studiengaenge",
#                    "https://www.studycheck.de/studium/clinical-research",
#                    "https://www.studycheck.de/studium/chirurgie",
#                    "https://www.studycheck.de/studium/counseling"]

# List of links for third level scraping (populated later)
tertiary_links = []
# Testing purposes:
# tertiary_links = ["https://www.studycheck.de/studium/betriebswirtschaftslehre-bwl/iu-mystudium-25628",
#                   "https://www.studycheck.de/studium/informatik/rfh-koeln-24566",
#                   "https://www.studycheck.de/studium/informatik/hs-schmalkalden-15717",
#                   "https://www.studycheck.de/studium/informatik/provadis-24716",
#                   "https://www.studycheck.de/studium/informatik/hs-heidelberg-10711",
#                   "https://www.studycheck.de/studium/informatik/hpi-23831",
#                   "https://www.studycheck.de/studium/informatik/hpi-23010",
#                   "https://www.studycheck.de/studium/informatik/hpi-23009",
#                   "https://www.studycheck.de/studium/architektur/frankfurtuas-11806",
#                   "https://www.studycheck.de/studium/informatik/hs-rheinmain-5714",
#                   "https://www.studycheck.de/studium/informatik/hs-stralsund-10969",
#                   "https://www.studycheck.de/studium/informatik/hs-trier-11072",
#                   "https://www.studycheck.de/studium/informatik/hs-harz-12024",
#                   "https://www.studycheck.de/studium/informatik/tu-cottbus-12131"]


# Commented out the following code, since main_links is already populated (see above).
# Can be run instead to extract anew.
# Alternative handling for a reduced dataset could be using only the top 5 majors listed under the base link for each
# category to return a smaller list of most popular majors
#####
# ----------------------------- One time only gathering of every major domain from homepage ----------------------------
# Extracts html from the opened link
# driver.get("https://www.studycheck.de/studium")
# soup = BeautifulSoup(driver.page_source, 'lxml')

# main_links = []
# for header in soup.find_all("a", {"class": "course-cnt"}, href = True):
# 	main_links.append(header["href"] + "/seite-")

# print("These are the extracted category links:", *main_links, sep = "\n")
#####


# ####
# # ---------------------------- First level of scraping (major categories for each domain) ----------------------------
#
# # Iterates over every study domain
# for link in main_links:
#     # Counter variable is used to iterate search result pages
#     counter = 1
#     # Sleep timer between requests to minimize risk of automatic IP blocking
#     time.sleep(random.randint(2, 3))
#     # Opens link and extracts html
#     driver.get(link + str(counter) + "?o=2")
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     time.sleep(random.randint(2, 3))
#     # Iterates the search result pages until no results (i.e. 404 error page, end of results) are found
#     # (find_all() returns list; empty list equals False)
#     while soup.find_all("div", {"class": "course-count"}):
#         # List to print new links from each results page
#         new_links = []
#         # Appends every link on the search result page to a list
#         for secondary_link in soup.find_all("div", {"class": "course-count"}):
#             secondary_links.append(secondary_link.findChild("a")["href"])
#             new_links.append(secondary_link.findChild("a")["href"])
#         # Prints scraped links and loads next page of search results
#         print("\n\nScraped links of page", str(counter) + ":")
#         print(*new_links, sep="\n")
#         counter += 1
#         time.sleep(random.randint(4, 8))
#         driver.get(link + str(counter) + "?o=2")
#         soup = BeautifulSoup(driver.page_source, 'lxml')
#         # Appends scraped links to .csv file
#         with open('../data/secondary_links.csv', 'a') as output:
#             writer = csv.writer(output, delimiter=',', lineterminator='\n')
#             for item in new_links:
#                 writer.writerow([item])
#
#     print("\n\n--------------- Finished scraping this category. Continuing with next category. ---------------")
#
# # Prints resulting list of majors once scraping loop is finished
# print("\n\nDone with scraping. Exiting.", "This is the resulting list of majors:\n", *secondary_links, sep="\n")
# ####

####
#------------------------ Second and third levels of scraping (majors for each major category) -----------------------

for secondary_link in secondary_links:
    # Counter variable is used to iterate search result pages
    counter = 1
    # Sleep timer between requests to minimize risk of automatic IP blocking
    time.sleep(random.randint(2, 3))
    # Opens link and extracts html
    # Example link: https://www.studycheck.de/studium/medizin/studiengaenge?o=3&fsid=&pi=1
    driver.get(secondary_link + "/seite-" + str(counter) + "?o=3&fsid=&pi=1")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print("\n\nNow scraping:", secondary_link + "/seite-" + str(counter) + "?o=3&fsid=&pi=1\n\n")
    time.sleep(random.randint(1, 2))

    # Iterates the search result pages until no results (i.e. 404 error page) are found (find_all() returns list;
    # empty list equals False)
    while soup.find_all("div", {"class": "rfv1-col-8"}):
        # Create lists of each variable to populate columns in the data file
        # New links from each results page to print
        new_links = []
        # First, second and third level categories to store website's study program structure
        categories = []
        subcategories = []
        major_categories = []
        # University of the major
        universities = []
        # City the major is offered in
        locations = []
        # Full name of the major
        major_names = []
        # Type of degree, e.g. "B.Sc." or "M.Eng."
        degree_types = []
        # Textual description of the courses offered in the major (NLP relevant)
        major_descriptions = []
        # Boolean for whether or not the description is stored in bullet point format or free text
        is_list = []
        # Approx. duration of study in number of semesters
        duration_of_study = []
        # Languages the major is taught in
        languages = []
        # Label of degree, e.g. "Bachelor of Science" or "Master of Engineering"
        degree_labels = []
        # Link to the StudyCheck major page
        studycheck_links = []
        # Link to the university major page
        university_links = []
        # Public rating for the major on a 5-star basis
        ratings = []
        # Amount of public ratings
        rating_amounts = []
        # Proportion of people who recommend the major
        recommendation_rates = []

        # Default value for when no categories are found (prevents rare bug)
        categories_string = "NA"
        subcategories_string = "NA"
        major_categories_string = "NA"

        # Extracts latter half of the menu navigation header
        for found in soup.find_all("li", {"class": re.compile("^rfv1-breadcrumbs__item rfv1-js-breadcrumbs-item.*")}):
            if found.find(content="3"):
                categories_string = found.find(itemprop="name").text.strip()
                print(found.find(itemprop="name").text.strip())
            elif found.find(content="4"):
                subcategories_string = found.find(itemprop="name").text.strip()
            elif found.find(content="5"):
                major_categories_string = found.find(itemprop="name").text.strip()

        # Iterates over every page of search results
        for major_detail in soup.find_all("div", {
            "class": "rfv1-media-layout__row rfv1-media-layout__row--relative rfv1-display--flex"}):
            # Checks if majors are listed in div container of search results, skips following code if finished
            if (
                    major_detail.find("div",
                                      {"class": "rfv1-sponsor-tag rfv1-sponsor-tag--no-gap rfv1-font-style--small"})):
                continue

            # Appends categories to lists
            categories.append(categories_string)
            subcategories.append(subcategories_string)
            major_categories.append(major_categories_string)

            # Appends new links to lists
            tertiary_links.append(major_detail.findChild("a")["href"])
            new_links.append(major_detail.findChild("a")["href"])
            # Extracts university + location (same String)
            university_location_string = major_detail.findChild("div", {"class": "rfv1-font-style--small"}).text.strip()
            # Splits String and appends university to list
            universities.append(university_location_string.rpartition(" (")[0])
            # Splits String and appends location to list
            locations.append(university_location_string.rpartition(" (")[-1].strip(")"))
            # Extracts major name + shortened degree (same String)
            name_degree_string = major_detail.findChild("a", {"class": "rfv1-font-style--none"}).text.strip()
            # Splits String and appends major name to list
            major_names.append(name_degree_string.rpartition(" (")[0])
            # Splits String and appends degree type to list
            degree_types.append(name_degree_string.rpartition(" (")[-1].strip(")"))

        # Prints scraped data from this search results page
        print("\n\nScraped contents of search page", str(counter) + ":")
        for a, b, c, d, e in zip(new_links, universities, locations, major_names, degree_types):
            print(a, b, c, d, e, "", sep="\n")

        # Iterates over every individual major link found in the specific search results page
        for tertiary_link in new_links:
            time.sleep(random.randint(1, 3))
            # Opens tertiary link and fetches html
            driver.get(tertiary_link)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            time.sleep(random.randint(1, 2))

            # Appends StudyCheck link to list
            studycheck_links.append(tertiary_link)
            # Extracts university link and appends to list
            university_links.append(soup.find("a", {"class": "institute-link"}, href=True)["href"])
            # Removes unnecessary parts of links
            if "?utm_source=" in university_links[-1]:
                university_links[-1] = university_links[-1].rpartition("?utm_source=")[0]
            # Extracts rating and appends to list
            if soup.find("div", {"class": "rating-value"}):
                ratings.append(soup.find("div", {"class": "rating-value"}).text.strip())
            else:
                ratings.append("NA")
            # Extracts recommendation rate and appends to list in form of proportion between 0 - 1
            if soup.find("span", {"class": "recommendation"}):
                recommendation_rates.append(float(
                    Decimal(" ".join(soup.find("span", {"class": "recommendation"}).text.split()).rpartition(" %")[
                                0]) / 100))
            else:
                recommendation_rates.append("NA")
            # Extracts rating amount and appends to list
            if soup.find("span", {"class": "report-count"}):
                rating_amounts.append(soup.find("span", {"class": "report-count"}).text.strip())
            else:
                rating_amounts.append("NA")

            # Tracks if the following variables are found
            found_duration = False
            found_language = False
            found_degree = False
            for element in soup.find_all("div", {"class": "card-row card-row--no-border"}):
                # Extracts duration of study and appends to list
                if element.find("span", {"class": "icon icon-course-clock"}):
                    duration_of_study.append(" ".join(element.findChild("div", class_="card-row-content").text.split()))
                    found_duration = True
                # Extracts languages and appends to list
                if element.find("span", {"class": "icon icon-course-language"}):
                    languages.append(element.findChild("div", class_="card-row-content").text.strip())
                    found_language = True
                # Extracts degree labels and appends to list
                if element.find("span", {"class": "icon icon-course-mortarboard"}):
                    degree_labels.append(element.findChild("div", class_="card-row-content").text.strip())
                    found_degree = True
            # Appends NA if variables were not found
            if not found_duration:
                duration_of_study.append("NA")
            if not found_language:
                languages.append("NA")
            if not found_degree:
                degree_labels.append("NA")

            # Extracts description and appends to list
            details = soup.find("div", class_="card-row contents js-toggle-sections card-row--no-border")
            if details:
                description = details.findChild("div", {"class": "card-row-content"})
                # Strips html structure from text on appendage
                major_descriptions.append(description.get_text(separator=" "))
                if description.find_all("li"):
                    is_list.append(True)
                else:
                    is_list.append(False)
            else:
                major_descriptions.append("NA")
                is_list.append("NA")

            # Prints scraped variables for last scraped individual major
            print("\n ### Scraped data of infoprofile " + tertiary_link + ":", str(major_descriptions[-1]),
                  "Rating: " + str(ratings[-1]), "Rating amount: " + str(rating_amounts[-1]),
                  "Rec Rate: " + str(recommendation_rates[-1]), str(degree_labels[-1]), str(duration_of_study[-1]),
                  str(university_links[-1]), str(languages[-1]), "Is list: " + str(is_list[-1]), sep="\n")

        counter += 1
        time.sleep(random.randint(1, 2))

        # Writes all scraped variables to data file
        with open('../data/raw_data.csv', 'a', encoding="utf-8") as output:
            writer = csv.writer(output, delimiter=',', lineterminator='\n')
            writer.writerows(
                zip(is_list, major_names, major_descriptions, studycheck_links, university_links, categories,
                    subcategories, major_categories, universities, locations, degree_types, degree_labels, languages,
                    duration_of_study, rating_amounts, ratings, recommendation_rates))

        # Fetches next search results page's html and prints progress
        driver.get(secondary_link + "/seite-" + str(counter) + "?o=3&fsid=&pi=1")
        print("\n\nNow scraping:", secondary_link + "/seite-" + str(counter) + "?o=3&fsid=&pi=1\n\n")
        soup = BeautifulSoup(driver.page_source, 'lxml')
####

# Quits the webdriver-session at the end of the scraping
driver.quit()
