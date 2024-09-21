from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver_path = '[ruta_path]'
similiar_account = 'chefsteps'
INSTAGRAM = 'https://instagram.com/'
USERNAME = '[usuario]'
PASSWORD = '[contraseña_instagram]'

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)


    def login(self):

        self.driver.get(f'{INSTAGRAM}{similiar_account}')

        time.sleep(2)
        cookies = self.driver.find_element(By.CSS_SELECTOR, '.aOOlW.HoLwm ')
        cookies.click()
        time.sleep(2)

        try:
            entrar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
            entrar.click()

        except:
            time.sleep(4)
            username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            username.send_keys(USERNAME)

            password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)

            guardar_datos = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
            guardar_datos.click()

        #notificacion = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        #notificacion.click()




    def find_followers(self):
        time.sleep(8)
        seguidores = self.driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        seguidores.click()

        time.sleep(2)
        lista_seguidoras = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        numero_seguidores = self.driver.find_element(By.XPATH,
                                                     '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').text
        print(numero_seguidores)
        for n in range(40):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", lista_seguidoras)
            time.sleep(1)

    def follow(self):
        follow = self.driver.find_elements(By.CSS_SELECTOR, 'button.sqdOP.L3NKy.y3zKF')
        print(len(follow))
        for any in follow:
            any.click()
            time.sleep(2)

    def unfollow(self):
        follow = self.driver.find_elements(By.CSS_SELECTOR, 'button.sqdOP.L3NKy._8A5w5')
        print(len(follow))
        for any in follow:
            any.click()
            time.sleep(1.5)
            self.driver.find_element(By.CSS_SELECTOR,'button.aOOlW.-Cab_').click()
            time.sleep(1.5)










insta_bot = InstaFollower()
insta_bot.login()

insta_bot.find_followers()

insta_bot.follow()

insta_bot.unfollow()
