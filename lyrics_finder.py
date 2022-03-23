from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from time import sleep

print("HELLO THERE!\n Welcome to Lyrics Finder. Enter the name of the song your want to search the lyrics for.")
song_name = input("Song Name => ")

#CHROME DRIVER PATH. Use this variable to update the Chrome driver path
webdriver_path = Service("<<<Chrome Driver path goes here>>>")

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service = webdriver_path, options = option)

print("\nSearching",end="")
for i in range(10):
    sleep(0.5)
    print(".", end="")

driver.get("https://www.google.com")
search_bar = driver.find_element_by_class_name('gLFyf')
search_bar.send_keys(song_name + " lyrics" + Keys.ENTER)


try:
    lyrics = driver.find_element_by_class_name('sATSHe')
    print("\nHow do you want the lyrics to be presented\n 1. CLI\n 2. Text File")
    choice = int(input("Enter your choice => "))

    if choice == 1:
        print("\nHere is your lyrics........\n")
        print(lyrics.text)

    elif choice == 2:
        with open('lyrics.txt', 'w') as f:
            f.write(lyrics.text)
        print("Check out the 'lyrics.txt' for your Lyrics")
except NoSuchElementException:
    print("\nSong not found!!")
    pass

print("\n\nTHANK YOU FOR USING LYRIC FINDER APP!\n made with <3 by Vivek :)")
