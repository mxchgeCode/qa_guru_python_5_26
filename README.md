## Проект автоматизации тестирования мобильного приложения "Wikipedia"
<img width="1162" alt="image" src="https://user-images.githubusercontent.com/109241600/207922538-dab0b3f0-a6e6-4474-8e1d-7b4f6d1f0daa.png">

## Содержание
+ [Технологии и инструменты](#Технологии)
+ [Тест-кейсы](#Тесты)
+ [Запуск автотестов из Jenkins](#Jenkins) 
+ [Оповещение о результатах через Telegram-бот](#Telegram) 
+ [Отчеты о прохождении тестов Allure report](#Allure) 
+ [Интеграция с Allure TestOPS](#TestOPS) 
+ [Интеграция с Jira](#Jira) 

## <a name="Технологии">Технологии и инструменты, использованные в проекте</a>
<p align="center">
<img width="6%" title="PyCharm" src="images/logo/pycharm.svg">
<img width="6%" title="Python" src="images/logo/python.svg">
<img width="6%" title="Pytest" src="images/logo/pytest.svg">
<img width="6%" title="Selenium" src="images/logo/selenium.png">
<img width="6%" title="Selene" src="images/logo/selene.png">
<img width="6%" title="GitHub" src="images/logo/GitHub.svg">
<img width="6%" title="Jenkins" src="images/logo/Jenkins.svg">  
<img width="6%" title="AllureReport" src="images/logo/Allure_Report.svg">  
<img width="6%" title="AllureTestOPS" src="images/logo/Allure_TO.svg"> 
<img width="6%" title="Telegram" src="images/logo/Telegram.svg">  
<img width="6%" title="Jira" src="images/logo/jira.svg"> 
<img width="6%" title="Browserstack" src="images/logo/Browserstack.svg"> 
<img width="5%" title="Appium" src="images/logo/Appium.svg"> 
</p>

## <a name="Тесты">Тест-кейсы</a>
  - Поиск информации
  - Возврат на главную страницу из результатов поиска
  - Переход на страницу с настройками
  - Возврат на главную страницу со страницы настроек
  
  ## <a name="Jenkins">Запуск автотестов из Jenkins</a>
Для удаленного запуска автотестов в <a href="https://jenkins.autotests.cloud/job/002-annazukowska-python-wikipedia-mobile/" target="_blank">Jenkins</a> создана задача (job), настроена и связана с репозиторием в GitHub.
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/109241600/207936123-2dd2443b-6529-46d4-9136-aba01d4b175f.png">

## <a name="Telegram">Уведомление о результатах тестирования через Telegram-бот</a>
После завершения тестов приходит такое оповещение в Telegram с помощью заранее созданного Telegram-бота, привязанного к задаче в Jenkins.

<img width="349" alt="image" src="https://user-images.githubusercontent.com/109241600/207936849-0bb509ae-d923-4799-b8cc-98c4687306b8.png">




