
import logging
# from common.base_page import BasePage
import allure


def running_info(func):

    logging.basicConfig(level=logging.INFO)

    def wrapper(*args,**kwargs):
        instance = args[0]
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args,**kwargs)
            return element
        except Exception as e:
            instance.driver.save_screenshot('err.png')
            with open("err.png","rb") as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error(" run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            raise e
    return wrapper