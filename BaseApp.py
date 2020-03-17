from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

class HomePage:
	
	#локатор ссылки "ВНИКАТЬ В ДЕТАЛИ ПРОЕКТОВ"
	graphsDetailsLinkLocator = (By.XPATH, '//div[contains(@class, "graphs-details")]/a')
	
	#локатор ссылки "НАХОДИТЬ НЕСОВЕРШЕНСТВА"
	graphsErrorsLinkLocator = (By.XPATH, '//div[contains(@class, "graphs-errors")]/a')
	
	#локатор ссылки "СОПРОВОЖДАТЬ ПРОЕКТЫ"
	graphsSupportLinkLocator = (By.XPATH, '//div[contains(@class, "graphs-support")]/a')
	
	#локатор ссылки "РАБОТАТЬ С ФАЙЛАМИ ПРОЕКТОВ"
	graphsFilesLinkLocator = (By.XPATH, '//div[contains(@class, "graphs-files")]/a')
	
	#общий локатор раздела "Распределение обязанностей"
	graphsTabLocator = (By.XPATH, '//section[contains(@class, "graphs")]/div[contains(@class, "graphs-")]')
	
	#локатор ссылки "Софт для быстрого создания скриншотов"
	monosnapLinkLocator = (By.XPATH, '//div//div[contains(@class,"info-errors")]//a')
	
	
	#локаторы footer-a
	#
	#локатор ссылки на почту HR
	hrLinkLocator = (By.XPATH, '//nav/div/a[contains(@href, "hr@csssr.com")]')
	
	#локатор ссылки на ВК группу
	vkLinkLoactor = (By.XPATH, '//nav/div/a[contains(@href, "vk.com/csssr")]')
	
	#локатор ссылки на Twitter
	twitterLinkLocator = (By.XPATH, '//nav/div/a[contains(@href, "twitter.com/csssr_dev")]')
	
	#контент
	#
	#локатор контента
	contentLocator = (By.XPATH, '//div[contains(@class, "wrap")]')
	
	def __init__(self, browser):
		self.browser = browser
		self.base_url = "http://blog.csssr.ru/qa-engineer/"
		
	#принимает локатор в формате (By.*,*)
	#отдает найденный элемент
	def findElement(self, locator, time=10):
		return WebDriverWait(self.browser,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
													  
	#принимает локатор в формате (By.*,*)
	#отдает список найденных элементов
	def findElements(self, locator,time=10):
		return WebDriverWait(self.browser,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
	
	#принимает найденный по локатору элемент
	#отдает цвет в формате HEX
	def getColor(self,element):
		color = element.value_of_css_property("color")
		return Color.from_string(color).hex

	#принимает найденный по локатору элемент
	#вызывает :hover у элемента
	def hover(self, element):
		hover = ActionChains(self.browser).move_to_element(element)
		hover.perform()
	
	#передает х(int) и у(int) 
	#изменяет размер окна браузера
	def changeWindowSize(self, x, y):
		return self.browser.set_window_size(x, y)
	
	#принимает найденный по локатору элемент
	#возвращает True или False
	def isElementClickable(self, element):
		return element.is_displayed()
	
	#принимает найденный по локатору элемент
	#кликает по элементу
	def click(self, element):
		hover = ActionChains(self.browser).move_to_element(element)
		hover.perform()
		element.click()
		
	#ничего не принимает
	#открывает браузер с базовым Url
	def openUrl(self):
		return self.browser.get(self.base_url)
		
	