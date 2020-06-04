#SPECS: 
#1. Create a virtual journal
#2. When opened creates a new file for that day or checks for an exising one
#3. The name of the file is the date (MM/DD/YYYY)
#4. All housed in one folder
#add link from my desktop
#lets you create an entry 


from datetime import date 
from datetime import datetime

def main(): 
    files()


def files(): 
    todayDate = date.today()
    #creates a string version of the date to use to name new file 
    todayString = todayDate.strftime("%m%d%y")

    #create or open entry file for current day
    fileName = todayString + ".txt"

    f = open(fileName, "a+")

    fileWrite(f)

    f.close

def fileWrite(openedFile):
    #gets user entry for the day 
    #asks if wants to add to entry, create a new section or done. 
    #enter value 1, 2 or 3 and catch errors 
    
    set = True
    while(set):
        print("\nWelcome! What would you like to do?\n")
        print("'1' = Add New Entry for Today | '2' = Add to Today's Existing Entry | '3' = Leave ")
        userInput = input("\nEnter an option: ")

        if(userInput == "1"):
            newEntry(openedFile)   

        if(userInput == "2"):
            existingEntry(openedFile)
                
        if(userInput == "3"):
            print("Thanks for using!")
            set = False


def newEntry(aFile): 

    #gets the current time to stamp onto the entry before the user starts writing
    now = datetime.now()
    timeString = now.strftime("%H:%M:%S")

    aFile.write("\n\n" + timeString)
    print("Start Writing Your Entry. Press Enter When Done\n")
    userIn = input()
    aFile.write("\n" + userIn)

    print("\nEntry added!\n")

def existingEntry(openedFile):

    print("Start Writing Your Entry. Press Enter When Done\n")
    userIn = input()
    openedFile.write("\n" + userIn)

    print("\nEntry added!\n")
main()