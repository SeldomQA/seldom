"""
test case runing model
"""
from time import sleep
from seldom.running.config import Seldom


def runing_model(elem):
    # Show the elements of the operation
    style_red = 'arguments[0].style.border="2px solid #FF0000"'
    style_blue = 'arguments[0].style.border="2px solid #00FF00"'
    style_null = 'arguments[0].style.border=""'
    if Seldom.debug is True:
        for _ in range(3):
            Seldom.driver.execute_script(style_red, elem)
            sleep(0.2)
            Seldom.driver.execute_script(style_blue, elem)
            sleep(0.2)
        Seldom.driver.execute_script(style_blue, elem)
        sleep(2)
        Seldom.driver.execute_script(style_null, elem)
    else:
        for _ in range(2):
            Seldom.driver.execute_script(style_red, elem)
            sleep(0.1)
            Seldom.driver.execute_script(style_blue, elem)
            sleep(0.1)
        Seldom.driver.execute_script(style_blue, elem)
        sleep(0.5)
        Seldom.driver.execute_script(style_null, elem)
