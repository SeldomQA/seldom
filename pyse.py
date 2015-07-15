#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import os,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

class Pyse(object):
    '''
        Pyse framework for the main class, the original 
    selenium provided by the method of the two packaging,
    making it easier to use.
    '''

    def __init__(self,browser='ff'):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome", 
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" or browser=="ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser=="ie":
            driver = webdriver.Ie()
        try:
        	self.driver = driver
        except Exception, e:
        	print "Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." %browser


    def open(self,url):
        '''
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)
        #self.driver.maximize_window()

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self,wide,high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide,high)

    def type(self,xpath,text):
        '''
        Operation input box.

        Usage:
        driver.type("//*[@id='el']","selenium")
        '''
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def click(self,xpath):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        
        Usage:
        driver.click("//*[@id='el']")
        '''
        self.driver.find_element_by_xpath(xpath).click()

    def right_click(self,xpath):
        '''
        Right click element.

        Usage:
        driver.right_click("//*[@id='el']")
        '''
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self,xpath):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("//*[@id='el']")
        '''
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self,xpath):
        '''
        double click element.

        Usage:
        driver.double_click("//*[@id='el']")
        '''
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self,el_xpath,ta_xpath):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("//*[@id='el']","//*[@id='ta']")
        '''
        element = self.driver.find_element_by_xpath(el_xpath)
        target = self.driver.find_element_by_xpath(ta_xpath)
        ActionChains(driver).drag_and_drop(element,target).perform()

    def click_text(self,text):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.click_text("新闻")
        '''
        aa = self.driver.find_elements_by_tag_name("a")
        for a in aa:
            try:
                if str(a.text) == text:
                    a.click()
            except StaleElementReferenceException, e:
                pass

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Closes the browser and shuts down the.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self,xpath):
        '''
        Submit the specified form.

        Usage:
        driver.submit("//*[@id='el']") 
        '''
        self.driver.find_element_by_xpath(xpath).submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self,script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self,xpath,attribute):
    	'''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("//*[@id='el']","type")
        '''
        return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)

    def get_text(self,xpath):
        '''
        Get element text information.

        Usage:
        driver.get_text("//*[@id='el']")
        '''
        return self.driver.find_element_by_xpath(xpath).text

    def get_display(self,xpath):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("//*[@id='el']")
        '''
        return self.driver.find_element_by_xpath(xpath).is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self,file_path):
        self.driver.get_screenshot_as_file(file_path)

    def wait(self,secs):
        '''
        implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def element_wait(self,xpath,secs):
        '''
        Waiting for an element to display.
        
        Usage:
        driver.element_wait("//*[@id='el']",10)
        '''
        for i in range(secs):
            try:
                el = self.driver.find_element_by_xpath(xpath).is_displayed()
                print el
                print type(el)
                print type(True)
                if el:
                    break
            except: pass
            time.sleep(1)
        else: print "time out"

    def accept_alert(self):
        '''
        accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.
        
        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to_alert().dismiss()

    def switch_to_frame(self,xpath):
        '''
        Dismisses the alert available.
        
        Usage:
        driver.switch_to_frame("//*[@id='el']")
        '''
        xf = self.driver.find_element_by_xpath('//*[@class="if"]')
        self.driver.switch_to_frame(xf)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to_default_content()

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to_default_content()

    def open_new_window(self,xpath):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.switch_to_frame_out()
        '''
        driver = self.driver
        original_windows = driver.current_window_handle
        driver.find_element_by_xpath(xpath).click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                driver.switch_to_window(handle)


if __name__ == '__main__':
    driver = Pyse("chrome")