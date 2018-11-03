#Asg2-Junaid Khalid
#Program1-BlackJack Game
#Add dealer wins all ties condition to it. Add exception handling to your codes. Add comments.

import random

def initialChecker(dealerCard01, dealerCard02, playerCard02, playerCard01):

	print("You get an %d and a %d." %(playerCard01, playerCard02)) #Shows the cards of the player

	dealerSum= dealerCard01 + dealerCard02
	playerSum= playerCard01 + playerCard02

	print("Your total is %d. \nThe dealer has a %d showing, and a hidden card. \nHis total is hidden, too." %(playerSum, dealerCard01))

	flag= checker(dealerSum, playerSum) #checks if the dealer or the player have won with their intial cards.

	if flag==False:
		nextRound(dealerSum, playerSum, dealerCard02) #if neither have won with the intitial cards, it allows the player to hit for as many times as he wants.

def checker(playerSum, dealerSum):

	flag=False

	if dealerSum==21 and playerSum!= 21:
		print("The Dealer wins!")
		flag= True

	elif playerSum==21 and dealerSum!=21:
		print("You win!")
		flag= True

	elif playerSum>21 and dealerSum<21:
		print("You have busted. Dealer wins!")
		flag= True

	elif dealerSum>21 and playerSum<21:
		print("The dealer has busted. You win!")
		flag = True

	return flag

def nextRound(dealerSum, playerSum, dealerCard02):

	for i in range(10): 

		response01= input("Would you like to hit or stay? ")

		if response01=="hit":

			playerNew= random.randint(2,11)
			playerSum+=playerNew

			print("You draw a %d.\nYour total is %d." %(playerNew, playerSum))
			flag= checker(playerSum, dealerSum) #each time the player hits, this function is called to make sure that the player hasn't busted and lost already.

			if flag==True:
				break

		elif response01=="stay":

			print ("Okay. Dealer's turn.\nHis hidden card was a %d. \nHis total was %d "%(dealerCard02, dealerSum)) #shows the player the hidden card of the dealer when he decides to stay.
			
			for a in range(10):

				if dealerSum<=16: #dealer continues to hit till his sum of cards is less than 17.

					dealerNew= random.randint(2,11)
					dealerSum+=dealerNew

					print("Dealer chooses to hit. \nHe draws a %d. \nHis total is %d."%(dealerNew, dealerSum))
					flag= checker(playerSum, dealerSum) #checks each time the dealer hits, if he has busted and lost.

					if flag==True:
						break

				elif dealerSum>16:

					print("Dealer stays. ")
					
					if dealerSum==playerSum:
					
						print("Dealer wins.")

				else:

					print("Dealer stays.")
					break

		if flag==True:
			break

def main():

	dealerCard01= random.randint(2,11)
	dealerCard02= random.randint(2,11)
	playerCard01= random.randint(2,11)
	playerCard02= random.randint(2,11)

	initialChecker(dealerCard01, dealerCard02, playerCard02, playerCard01)

main()

#Program 2

def atmMachine (pins,accountNumbers,userNames,accountBalance):
	
	for x in range(1,100000000000000000):
	
		count=0
	
		try:
			
			pinCode = int(input("Enter your 4 digit pin: "))
			
		except Exception as e:
	
			print("Invalid pin entered.")
			print(e)
	
		else:
	
			for pin in pins:
	
				if pin==pinCode:
	
					print("Welcome :",userNames[count])
					print("Your account number is :", accountNumbers[count])
					print("Your current account balance is: ", accountBalance[count])
					accBalance= int(accountBalance[count])
					transType = input("Please select a transaction type: d for deposit/ w for withdrawal: ")
		
					if transType == "d":

						try:
		
							depAmount = int(input("Enter the amount you want to deposit: "))
							
						except Exception as e:
						
							print("Invalid input of deposit amount. Please try again")
							print(e)

						else:
						
							accBalance+=depAmount
							accountBalance[count]= accBalance
							print("Your new balance is: ",accBalance, ".Have a nice day!")

					else:
						
						try:
					
							withdrawalAmount = int(input("Enter the amount you want to withdraw: "))
					
						except Exception as e:
					
							print("Invalid input of withdrawal amount. Please try again.")
							print(e)

						else:
								
							accBalance-=withdrawalAmount

							if accBalance<0: 
								
								print("You do not have sufficient funds in your account. ")
								accBalance+=withdrawalAmount
								continue

							accountBalance[count]= accBalance
							print("Your new balance is:",accBalance,".Have a nice day!")

				count+=1

def main():
	
	pins = [1122, 1234, 1000, 2000, 3000]
	accountNumbers = [123456789, 987654321, 125896347, 123456781, 321456987]
	userNames = ["Junaid Khalid","Muhammad Khalid","Husnain Khalid","Talha Khalid","Waleed Khalid"]
	accountBalance = [50000000,1000000,350000,250000,2540000]
	atmMachine (pins,accountNumbers,userNames,accountBalance)

main()

#program3

print(''' Below is a list of symptoms that this system can handle: 
1.Headache
2.Aggression
3.Night sweats
4.Nocturnal coughs
5.Itchy scalp
6.Back pain
7.Blurred vision
8.Nausea
9.Dizziness
10.Blisters & Skin rashes
11.Red Eyes
12.Joint pain''')

def medication(disease):

	if disease=="altitude sickness":
		print("Suggested Medicine: Acetazolamide")

	if disease=="hypertension":
		print("Suggested Medicine: Propranolol")

	if disease=="HIV":
		print("Suggested Medicine: Antiretroviral drug")

	if disease=="headache":
		print("Suggested Medicine: Disprin")		

	if disease=="alzheimer":
		print("Suggested Medicine: Haloperidol")

	if disease=="arthritis":
		print("Suggested Medicine: Meclofenamic acid")

	if disease=="myocardial infarction":
		print("Suggested Medicine: Streptokinase")

	if disease=="asthma":
		print("Suggested Medicine: Zileuton")

	if disease=="alopecia":
		print("Suggested Medicine: Minoxidil")

	if disease=="bladdercancer":
		print("Suggested Medicine: Radiation therapy")

	if disease=="braintumor":
		print("Suggested Medicine: Radiation therapy")

	if disease=="dehydration":
		print("Suggested Medicine: Water")

	if disease=="hepatitis":
		print("Suggested Medicine: Telbivudine")

	if disease=="cardiovascular":
		print("Suggested Medicine: ACE inhibitor")

	if disease=="heartfailure":
		print("Suggested Medicine: Cyclothiazide")

	if disease=="dermatitis":
		print("Suggested Medicine: Ketoconazole")

	if disease=="influenza":
		print("Suggested Medicine: Amantadine")

	if disease=="leukemia":
		print("Suggested Medicine: Irinotecan")

def simpleMed(sym):

	if sym=="1":
		print("Suggested medicine: Disprin.")

	elif sym=="2":
		print("Suggested medicine: Clozapine.")

	elif sym=="3":
		print("Suggested medicine: Black Cohosh")

	elif sym=="4":
		print("Suggested medicine: Ethextrol")

	elif sym=="5":
		print("Suggested medicine: Tea Tree Oil")

	elif sym=="6":
		print("Suggested medicine: Tylenol")

	elif sym=="7":
		print("Suggested medicine: Visine")

	elif sym=="8":
		print("Suggested medicine: Phenergan")

	elif sym=="9":
		print("Suggested medicine: Meclizine")

	elif sym=="10":
		print("Suggested medicine: Acetaminophen")

	elif sym=="11":
		print("Suggested medicine: Visine Eyes drops")

	elif sym=="12":
		print("Suggested medicine: Ibuprofen")

def disease(sym):

	disease= "No disease could be evaluated."
	for i in range(len(sym)):

		sym01= sym[i]

		if sym01=="1":

			ques01= input("Have you been to a place of high altitude recently? Answer with yes or no :")
			
			if ques01=="yes":

				print("You have altitude sickness.")
				disease= "altitude sickness"
				break

			elif ques01=="no":
				diseaseFound= False

				for a in range(len(sym)):

					if sym[a]=="9":

						print("You are suffering from hypertension.")
						disease= "hypertension"
						diseaseFound=True
						break

				if diseaseFound==True:
					break

				else:
					
					ques02= input("Have you been suffering from flu-like symptoms like coughs, fever, sore throat,etc ? yes/no :")

					if ques02=="yes":

						print("You might have HIV.")
						disease="HIV"
						break

					elif ques02=="no":

						print("You're suffering from a simple headache.")
						disease= "headache"
						break

		elif sym01=="2":

			ques01= input("Do you also laugh or cry involuntarily and without any reason? yes/no: ")

			if ques01== "yes":

				print("You might have Alzheimer's disease.")
				disease= "alzheimer"
				break

			elif ques01=="no":

				print("No disease found based on your '''aggression''' symptom.")

		elif sym01=="3":

			ques01= input("Do you sweat ONLY at night? yes/no :")

			if ques01== "yes":

				ques02= input("Do you also have trouble breathing? yes/no : ")
				
				if ques02=="yes":

					print("You could be suffering from arthritis. ")
					disease= "arthritis"
					break

				else:

					print("Couldn't find a disease matching your symptoms.")

			elif ques01=="no":	

				for i in range(len(sym)):

					if sym[i]=="8":

						print("You could have myocardia infarction.")
						disease= "myocardial infarction"
						break

		elif sym01=="4":

			ques01= input("Do you have trouble breathing or suffer from temporary cardia arrests? yes/no : ")

			if ques01=="yes":

				print("You have asthma.")
				disease= "asthma"
				break

			else:

				print("Couldn't find any disease matching the symptoms in the system.")

		elif sym01=="5":

			print("You could be suffering from Alopecia.")
			disease= "alopecia"
			break

		elif sym01=="6":

			ques01=input("Do you have difficulty urinating as well? yes/no : ")

			if ques01=="yes":

				print("You could have bladder cancer. ")
				disease="bladdercancer"
				break

			else:

				print("Coulnd't find a disease matching your symptoms. You must simply be exhausted.")

		elif sym01=="7":

			for a in range(len(sym)):

				if sym[a]=="8":
					
					print("You could have brain tumor.")
					disease="braintumor"
					break

				else:

					print("No diseases matching your symptoms found. You must simply be feeling weak.")

		elif sym01=="8":

			for a in range(len(sym)):

				diseaseFound=False

				if sym[a]=="9":

					print("You are dehydrated.")
					disease="dehydration"
					diseaseFound=True
					break

				elif sym[a]=="12":

					print("You could be suffering from hepatitis.")
					disease="hepatitis"
					diseaseFound=True
					break

			if diseaseFound==False:
				print("No disease matching these symptoms was found.")

		elif sym01=="9":

			ques01= input("Do you also have trouble breathing? yes/no : ")

			if ques01=="yes":

				ques02= input("Do you also have irregular or a very strong heart beatat some times? yes/no : ")

				if ques02=="yes":

					print("You could be suffering from Cardiovascular disease.")
					disease="cardiovascular"
					break

				elif ques02=="no":

					print("You could be suffering from a heart failure.")
					disease="heartfailure"
					break

			else:
				
				print("No diseases matching your symptoms found. You must simply be feeling weak.")

		elif sym01=="10":

			print("You have dermatitis.")
			disease="dermatitis"
			break

		elif sym01=="11":

			ques01= input("Do you also have either watery eyes or fever? yes/no: ")

			if ques01=="yes":

				print("You have Influenza.")
				disease="influenza"
				break

			else:

				print("No disease matching your symptoms found. ")

		elif sym01=="12":

			diseaseFound=False

			for a in range(len(sym)):

				if sym[a]=="13":

					print("You could be suffering from leukemia.")
					disease="leukemia"
					diseaseFound=True
					break

			if diseaseFound==False:

				print("No disease matching your symptoms was found.")

	medication(disease)

def main():

	resp01= input("Do you wish to enter more than one symptoms? yes/no : ")

	if resp01=="yes":

		sym= input("Enter the numbers for the symptoms you have: ").split()
		disease(sym)

	else:

		sym=input("Enter the number for the symptom you have: ")
		simpleMed(sym)

main()
