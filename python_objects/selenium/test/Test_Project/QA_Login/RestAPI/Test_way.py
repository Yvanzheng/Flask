# -*- coding:utf-8 -*-
from selenium import webdriver

dr = webdriver.Chrome()


def test_login(username, password):
	dr.get('http://beebank.qa.com/testhome/')
	dr.find_element_by_name('username').send_keys(username)
	dr.find_element_by_name('password').send_keys(password)
	dr.find_element_by_class_name('but').click()
	dr.quit()


def test_login_success(self):
	self.test_login('admin', 'admin')
	dr.get_screenshot_as_file('../../Test_Result/login_success.jpg')
	dr.quit()


def test_login_pwd_error(self):
	self.test_login('admin', '111')
	dr.get_screenshot_as_file('../../Test_Result/login_pwd_error.jpg')
	dr.quit()


def test_login_pwd_null(self):
	self.test_login('admin', '')
	dr.get_screenshot_as_file('../../Test_Result/login_pwd_null.jpg')
	dr.quit()


def test_login_user_error(self):
	self.test_login('123', 'admin')
	dr.get_screenshot_as_file('../../Test_Result/login_user_error.jpg')
	dr.quit()


def test_login_user_null(self):
	self.test_login('', 'admin')
	dr.get_screenshot_as_file('../../Test_Result/login_user_null.jpg')
	dr.quit()


def tearDown():
	print('自动测试完毕！')
	dr.quit()
