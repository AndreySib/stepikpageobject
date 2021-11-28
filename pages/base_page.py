class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	def __init__(self, browser, url, timeout=10):  #добавим команду для неявного ожидания со значением по умолчанию в 10:
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def is_element_present(self, CSS_SELECTOR, NoSuchElementException):#в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
		try:
			self.browser.find_element(By.CSS_SELECTOR, NoSuchElementException)
		except (NoSuchElementException):
			return False
			return True