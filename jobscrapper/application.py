import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# my job information to put into fields
APPLICANT_INFO = {
    "first_name": "Zachary",
    "last_name": "Montague",
    "resume": "Resume-Zachary-Montague.pdf",
    "resume_textfile": "Resume-Zachary-Montague.txt",
    "linkedin": "https://www.linkedin.com/in/thelinuxcowboy",
    "github": "https://github.com/Zmontague",
    "location": "Saint Louis, Missouri, United States",
    "grad_month": '05',
    "grad_year": '2026',
    "university": "Saint Louis University",
    "email": "zrmontague@protonmail.com",
    "phone": "xxx-xxx-xxxx",
    "org": "Saint Louis University School of Medicine"
}
def greenhouse(driver):

    driver.find_element_by_id('first_name').send_keys(APPLICANT_INFO['first_name'])
    driver.find_element_by_id('last_name').send_keys(APPLICANT_INFO['last_name'])
    driver.find_element_by_id('email').send_keys(APPLICANT_INFO['email'])
    driver.find_element_by_id('phone').send_keys(APPLICANT_INFO['phone'])

    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(APPLICANT_INFO['location'])
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        time.sleep(2)

    except NoSuchElementException:
        pass

    driver.find_element_by_css_selector("[data-source='paste']").click()
    resume_area = driver.find_element_by_id('resume_text')
    resume_area.click()
    with open(APPLICANT_INFO["resume_textfile"]) as f:
        lines = f.readlines()
        for line in lines:
            resume_area.send_keys(line.decode('utf-8'))

    # LinkedIn
    try:
        driver.find_element_by_xpath("//label[contains(.,'LinkedIn)]").send_keys(APPLICANT_INFO['linkedin'])
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//label[contains(.,'LinkedIn)]").send_keys(APPLICANT_INFO['linkedin'])
        except  NoSuchElementException:
            pass

