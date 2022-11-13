from playsound import playsound
import requests, time

url = "https://pisa.ucsc.edu/class_search/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIyMzAiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiMzEzNzciO30%253D"

#runs until program is stopped
i = 0
while(True):
    try:
        content = requests.get(url).text
        #accesses webpage at ucsc
        #checks for 0 avaliable seats
        if "<dt>Available Seats</dt><dd>0</span></dd>" in content:
            print("Class Closed " + str(i))
            i += 1
        else:
            print("Class Open")
            playsound("noti.mp3")

            
    except:
        print("Error occurred")
    
    #time delay to avoid overloading server
    time.sleep(5.3)