from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

'''
to locate the elements in selenium we use different kinds of locators namely
class name
css selector
Id
text
name
tag name
Xpath

condition for the best locator
1. unique
2. static 
3. descriptive

Avoid using 
1. link text
2. Tag name
3. Xpath

Preferabally used:
 ID, Class, name and CSs selector
'''

## path of the web driver
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

class SeleniumAutomation:
    def KeyboardAndMoueseAction(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/keypress")
        nameElement = 'name'
        name = driver.find_element(By.ID, nameElement)
        name.click()
        name.send_keys("Shreyash")

        buttonElement = 'button'
        button = driver.find_element(By.ID, buttonElement)
        button.click()

        time.sleep(4)
        driver.quit()

    def AutoComplete(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/autocomplete")

        autoCompleteId = "autocomplete"
        autoComplete = driver.find_element(By.ID, autoCompleteId)
        autoComplete.send_keys("1555 Park Blvd, Palo Alto, CA")
        autoCompleteResult = driver.find_element(By.CLASS_NAME, "pac-item")
        autoCompleteResult.click()

        time.sleep(4)
        driver.quit()

    def Scroll(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/scroll")

        nameElement = 'name'
        name = driver.find_element(By.ID, nameElement)
        actions = ActionChains(driver)
        actions.move_to_element(name)
        name.send_keys("Shreyash")

        dateElement = 'date'
        date = driver.find_element(By.ID, dateElement)
        date.send_keys("11/11/1111")

        time.sleep(4)
        driver.quit()

    def SwitchToActiveWindow(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/switch-window")

        buttonElement = "new-tab-button"
        tabButton = driver.find_element(By.ID, buttonElement)
        tabButton.click()
        all_window_handles = driver.window_handles
        driver.switch_to.window(all_window_handles[0])

        time.sleep(4)
        driver.quit()

    def SwithToAlret(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/switch-window")

        alert_button_element = "alert-button"
        alert_button = driver.find_element(By.ID, alert_button_element)
        alert_button.click()

        ## to focus driver to alert which is popped up
        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(4)
        driver.quit()

    def Modal(self):

       ## done half way
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/modal")

        modalButtonId = "modal-button"
        modal_button = driver.find_element(By.ID, modalButtonId)
        modal_button.click()

        close_button_id = "close-button"
        close_button = driver.find_element(By.ID, close_button_id)
        close_button.click()

        time.sleep(3)
        driver.quit()

    def DragAndDrop(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/dragdrop")

        imageId = "image"
        image = driver.find_element(By.ID, imageId)

        boxId = "box"
        box = driver.find_element(By.ID, boxId)

        action = ActionChains(driver)
        action.drag_and_drop(image, box).perform()

        time.sleep(4)
        driver.quit()

'''
Automating the common components
'''
class AutomatingCommonCompoenets:
    def RadioButton(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/radiobutton")

        # radio_button_id = "radio-button-1"
        # radio_button_1 = driver.find_element(By.ID,radio_button_id)
        # radio_button_1.click()

        # radio_button_value = "option2"
        # radio_button_2 = driver.find_element(By.CSS_SELECTOR, radio_button_value)
        # radio_button_2.click()

        radio_button_Xpath = "/html/body/div/div[3]/input"
        radio_button_3 = driver.find_element(By.XPATH, radio_button_Xpath)
        radio_button_3.click()

        time.sleep(3)
        driver.quit()

    def DatePicker(self):

        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/datepicker")

        date_picker_id = "datepicker"
        date_picker = driver.find_element(By.ID, date_picker_id)
        date_picker.send_keys("11/11/1998")
        date_picker.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.quit()

    def DropDown(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/dropdown")

        drop_down_id = "dropdownMenuButton"
        drop_down = driver.find_element(By.ID, drop_down_id)
        drop_down.click()

        autocomplete_id = "autocomplete"
        autocomplete = driver.find_element(By.ID, autocomplete_id)
        autocomplete.click()

        time.sleep(3)
        driver.quit()

    def FileUpload(self):
        driver =  webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/fileupload")

        file_upload_field = "file-upload-field"
        file_upload = driver.find_element(By.ID, file_upload_field)
        file_upload.send_keys("test1.png")

        time.sleep(3)
        driver.quit()

class Synchronization:
    def sync_AutoComplete_implicit_waits(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/autocomplete")

        autoCompleteId = "autocomplete"
        autoComplete = driver.find_element(By.ID, autoCompleteId)
        autoComplete.send_keys("1555 Park Blvd, Palo Alto, CA")
        # wait for specific amount of time before throwing no such element exception
        # default time is 0 sec, and does not depend on current element state just time
        driver.implicitly_wait(5)
        autoCompleteResult = driver.find_element(By.CLASS_NAME, "pac-item")
        autoCompleteResult.click()

        time.sleep(4)
        driver.quit()

    def explicite_waits(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/autocomplete")

        autoCompleteId = "autocomplete"
        autoComplete = driver.find_element(By.ID, autoCompleteId)
        autoComplete.send_keys("1555 Park Blvd, Palo Alto, CA")

        # wait for an element to be in specific condition
        # will not take up the unnecessary time
        wait = WebDriverWait(driver, 10)
        close_button = wait.until(expected_conditions.visibility_of_element_located(By.CLASS_NAME,"pac-item"))
        close_button.click()
        autoCompleteResult = driver.find_element(By.CLASS_NAME, "pac-item")
        autoCompleteResult.click()

        time.sleep(4)
        driver.quit()

class Automating_workflow:
    def WorkflowAutomation(self):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/form")

        self.submit_form(driver)

    def submit_form(self, driver):
        driver.find_element(By.ID, "first-name").send_keys("Shreyash")

        driver.find_element(By.ID, "last-name").send_keys("Patil")

        driver.find_element(By.ID, "job-title").send_keys("Engineer")
        driver.find_element(By.ID, "radio-button-1").click()
        driver.find_element(By.ID, "checkbox-1").click()

        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()

        driver.find_element(By.ID, "datepicker").send_keys("01/11/1198")

        submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

        ## to confirm the form is submitted
        wait = WebDriverWait(driver, 10)
        alert = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert alert-success")))
        try:
            assert alert.text == "The form was successfully submitted!", "Text does not match!"

        except AssertionError as e:
            print("Assertion Error:", e)

        finally:
            driver.quit()



simpleAutomation = SeleniumAutomation()
CommonComponenets = AutomatingCommonCompoenets()
Synchronization_tasks = Synchronization()
WorkFlowAutomation = Automating_workflow()
WorkFlowAutomation.WorkflowAutomation()
