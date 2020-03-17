from BaseApp import HomePage

REDCOLOR = ('#ff0000',)
GRAPHSLEN = (4,)
MONOSNAPHREF =('http://monosnap.com/',)

#тестируем hover ссылки 1й вкладки "распределение обязанностей"
def testLinkGraphsDetails(browser):
	print("\n\nstart test1")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	elem = homePage.findElement(homePage.graphsDetailsLinkLocator)
	homePage.hover(elem)
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
	
	print("finish test1")

#тестируем hover ссылки 2й вкладки "распределение обязанностей"
def testLinkGraphsErrors(browser):
	print("\n\nstart test2")
	
	homePage = HomePage(browser)
	homePage.openUrl()	
	elem = homePage.findElement(homePage.graphsErrorsLinkLocator)
	homePage.hover(elem)
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test2")	
	
#тестируем hover ссылки 3й вкладки "распределение обязанностей"
def testLinkGraphsSupport(browser):
	print("\n\nstart test3")
	
	homePage = HomePage(browser)
	homePage.openUrl()	
	elem = homePage.findElement(homePage.graphsSupportLinkLocator)
	homePage.hover(elem)
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test3")
	
#тестируем hover ссылки 4й вкладки "распределение обязанностей"
def testLinkGraphsFiles(browser):
	print("\n\nstart test4")
	
	homePage = HomePage(browser)
	homePage.openUrl()	
	elem = homePage.findElement(homePage.graphsFilesLinkLocator)
	homePage.hover(elem)
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test4")
	
#тестируем hover footer-a 1й ссылки на почту HR
def testLinkHr(browser):
	print("\n\nstart test5")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	elem = homePage.findElement(homePage.hrLinkLocator)
	
	#проверяем, выводится ли ссылка на экран
	assert  homePage.isElementClickable(elem) == True, f'Ссылка "{elem.text}" - некликабельна'	
	homePage.hover(elem)
	
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
	
	print("finish test5")

#тестируем hover footer-a 2й ссылки на VK
def testLinkVk(browser):
	print("\n\nstart test6")
		
	homePage = HomePage(browser)
	homePage.openUrl()
	elem = homePage.findElement(homePage.vkLinkLoactor)
	
	#проверяем, выводится ли ссылка на экран
	assert  homePage.isElementClickable(elem) == True, f'Ссылка "{elem.text}" - некликабельна'	
	homePage.hover(elem)
	
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test6")
	
#тестируем hover footer-a 3й ссылки на twitter
def testLinkTwitter(browser):
	print("\n\nstart test7")
		
	homePage = HomePage(browser)
	homePage.openUrl()
	elem = homePage.findElement(homePage.twitterLinkLocator)
	
	#проверяем, выводится ли ссылка на экран
	assert  homePage.isElementClickable(elem) == True, f'Ссылка "{elem.text}" - некликабельна'	
	homePage.hover(elem)
	
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test7")
	
#тестируем ссылку на софт создания скриншотов во вкладке "находить несовершенства"
def testLinkGraphsErrorsTab(browser):
	print("\n\nstart test8")
		
	homePage = HomePage(browser)
	homePage.openUrl()
	
	#переходим на вкладку "находить несовершенства"
	linkTab = homePage.findElement(homePage.graphsErrorsLinkLocator)
	homePage.click(linkTab)
		
	elem = homePage.findElement(homePage.monosnapLinkLocator)
		
	#проверяем, выводится ли ссылка на экран
	assert  homePage.isElementClickable(elem) == True, f'Ссылка "{elem.text}" - некликабельна'
		
	#проверяем, открывается ли ссылка в новой вкладке
	target = elem.get_attribute("target")
	assert target == "_blank", f'Ссылка "{elem.text}" не открывается на новой странице'
	
	#проверяем, ведет ли ссылка на http://monosnap.com/ 
	href = elem.get_attribute("href")
	assert href == MONOSNAPHREF[0], f'Ссылка "{elem.text}" не ведет на http://monosnap.com/'
	
	#тестируем hover ссылки на софт создания скриншотов
	homePage.hover(elem)
	
	assert homePage.getColor(elem) == REDCOLOR[0], f'Цвет hover-a ссылки "{elem.text}" должен быть красный'
		
	print("finish test8")
	
#тестируем ширину поля контента
def testContentWidth(browser):
	print("\n\nstart test9")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	
	content = homePage.findElement(homePage.contentLocator)
					
	#меняем ширину окна браузера (более 1024px)
	homePage.changeWindowSize(1040, 600)
	width = content.value_of_css_property("width")
	assert '1000px' == width, f"Ширина контента при ширине браузера более 1024px должна быть 1000px"
		
	print("finish test9")
	
#тестируем количество состояний (не исчезают ли столбцы с %) блока "распределение обязанностей"
#при клике на ссылку "Вникать в детали проектов"
def testGraphsQuantityDetails(browser):
	print("\n\nstart test10")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	graphsDetails = homePage.findElement(homePage.graphsDetailsLinkLocator)			
	#целиком весь блок "распределение обязанностей"
	graphs = homePage.findElements(homePage.graphsTabLocator)
	homePage.click(graphsDetails)
	assert GRAPHSLEN[0] == len(graphs), f'Ссылка "{graphsDetails.text}" - Блок «Распределение обязанностей» должен иметь 4 состояния'
		
	print("finish test10")
	
	
#тестируем количество состояний (не исчезают ли столбцы с %) блока "распределение обязанностей"
#при клике на ссылку "Находить несовершенства"
def testGraphsQuantityErrors(browser):
	print("\n\nstart test11")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	graphsErrors = homePage.findElement(homePage.graphsErrorsLinkLocator)	
	graphs = homePage.findElements(homePage.graphsTabLocator)	
	homePage.click(graphsErrors)
	assert GRAPHSLEN[0] == len(graphs), f'Ссылка "{graphsErrors.text}" - Блок «Распределение обязанностей» должен иметь 4 состояния'
		
	print("finish test11")

#тестируем количество состояний (не исчезают ли столбцы с %) блока "распределение обязанностей"
#при клике на ссылку "Сопровождать проекты"
def testGraphsQuantitySupport(browser):
	print("\n\nstart test12")
		
	homePage = HomePage(browser)
	homePage.openUrl()
	graphsSupport = homePage.findElement(homePage.graphsSupportLinkLocator)
	graphs = homePage.findElements(homePage.graphsTabLocator)
	homePage.click(graphsSupport)
	assert GRAPHSLEN[0] == len(graphs), f'Ссылка "{graphsSupport.text}" - Блок «Распределение обязанностей» должен иметь 4 состояния'
		
	print("finish test12")

#тестируем количество состояний (не исчезают ли столбцы с %) блока "распределение обязанностей"
#при клике на ссылку "Работать с файлами проектов"
def testGraphsQuantityFiles(browser):
	print("\n\nstart test13")
	
	homePage = HomePage(browser)
	homePage.openUrl()
	graphsFiles = homePage.findElement(homePage.graphsFilesLinkLocator)	
	graphs = homePage.findElements(homePage.graphsTabLocator)
	homePage.click(graphsFiles)
	assert GRAPHSLEN[0] == len(graphs), f'Ссылка "{graphsFiles.text}" - Блок «Распределение обязанностей» должен иметь 4 состояния'
		
	print("finish test13")