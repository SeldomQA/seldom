# coding=utf-8
import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MyTest(unittest.TestCase):

    global case_count
    case_count = 0

    global image_count
    image_count = 0

    # Calculate the number of test cases
    def case_id_number(self):
        global case_count
        case_count += 1
        if case_count <= 9:
            count = "00" + str(case_count)
        elif case_count <= 99:
            count = "0" + str(case_count)
        else:
            count = str(case_count)
        return count

    # Generate a screenshot file name
    def image_id_number(self):
        global image_count
        image_count += 1
        if image_count <= 9:
            count = "00" + str(image_count)
        elif image_count <= 99:
            count = "0" + str(image_count)
        else:
            count = str(image_count)
        return count

    def insert_img(self, driver, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        f = open(base_dir+"\\reporting\\report.txt", 'r')
        file_path = f.read()
        driver.get_windows_img(file_path + "report\\image\\" + file_name)

    def setUp(self):
        print "case " + str(self.case_id_number())

    def tearDown(self):
        img_id = self.image_id_number()
        file_name = img_id + ".jpg"
        self.insert_img(self.driver, file_name)
        print "image/" + file_name
        self.driver.quit()


if __name__ == '__main__':
    pass
