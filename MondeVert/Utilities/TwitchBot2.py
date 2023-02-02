from selenium import webdriver
from time import sleep

# The profile directory which Opera VPN was enabled manually using the GUI



from selenium import webdriver
import threading
import time

def test_logic():
    driver = webdriver.Chrome()
    url = 'https://www.twitch.tv/mondevert'
    driver.get(url)
    # Implement your test logic
    time.sleep(2)
    driver.quit()
    # opera_profile = '/home/user-directory/.config/opera'
    # #options = webdriver.ChromeOptions()
    # options = webdriver.Opera(executable_path='/path/to/functional_tests/operadriver')
    # options.add_argument('user-data-dir=' + opera_profile)
    # driver = webdriver.Opera(options=options)
    # driver.get('https://www.twitch.tv/mondevert')
    # sleep(180)
    # driver.quit()


N = 2  # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(180)
    print (t.name + ' started!')
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

print ('Test completed!')