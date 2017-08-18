#Ping utility to determine the average latency period of a specified server/web-address
#This is for windows only
import os
import re
import sys

def split_units(value): #this function is to slip the time which is in e.g 300(ms) to 300 alone

    units = ""
    number = 0
    while value:
        try:
            number = float(value)
            break
        except ValueError:
            units = value[-1:] + units
            value = value[:-1]
    return number

def pinger():
	ping_input = input("Input web address: ") #this is the text input
	ping_number = int(input("Input the number (2 and above) of times you want the ping to execute: "))
	print("pinging........... {}".format(ping_input))
	file = open('tester.txt', 'w')
	pinger = " " #this empty string is created to refresh the page at intervals
	file.write(pinger) #this is used to refresh the file
	file.close() #this is to close it, it is very important when dealing with file=open
	if sys.platform == 'linux':
		ping = os.system('ping -c {} {} >> tester.txt'.format(ping_number, ping_input))
	elif sys.platform == 'win32':
		ping = os.system('ping /n {} {} >> tester.txt'.format(ping_number, ping_input))
	#above is the ping statement, it consist of the windows ping command, using the os.system
	if ping == 0: # Zero is the default message for a successful ping
		print('\n Ping was successful!!!')
		print('\n\nConnection to {} is resolvable!'.format(ping_input))
	else: # anything apart from Zero means unsuccessful internet connection
		print('\n Pinging Failed!!!')
		print('Error: Check the Web address you typed.\n The problem might be your connection or Invalid Web address!')

	searchfile = open("tester.txt", "r") #this is to open the tester file and search for the Average value
	for line in searchfile:
	    if "Average" in line:
	    	line_to_list = line.split(',') #to convert it to a list, as it contains min, max, and average
	    	last_line = line_to_list[-1] # to get the last value which is the average--(only in windows, linux is different)
	    	print('\nThe Average Response trip time of the web-address is: ', last_line) #to display the average rtt
	    	lasty = last_line.split('=')#since the average rtt is in the format average=30ms, we remove the =,
	    	later = lasty[-1] #the one in the right side or the last value in the list is the 30ms value
	    	split_to_int = split_units(later) #we use the split function to remove the ms from the number
	    	average_int = int(split_to_int) # we convert the number to integer
	    	
	    	if average_int <= 499:
	    		print("If the web-address is not within the LAN, then the Average latency is Fast")
	    	elif average_int >= 500 <=700:
	    		print("If the web-address is not within the LAN, then the Average latency is Good")
	    	elif average_int >= 701 <= 1500:
	    		print("The average latency is not fast enough, \n these might be due to the speed of light,\n or geographic distances")
	    	elif average_int > 1501:
	    		print("The Average latency is slow, check the connection(speed of light) of evaluate the geographic distances")
	searchfile.close()

pinger() #we execute the ping function




