###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 14th excrcise
from random import choice

lottery_numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']

def lottery():
				winning_lottery = ""
				for _ in range(4):
								winning_lottery += choice(lottery_numbers)
				return winning_lottery

def lottery_win():
				
				ticket = lottery()
				print(f"Any one with this number printed on there lottery ticket will win the prize:")
				print(f"\nLottery No.:{ticket}")

#raw data to test code
lottery_win()
rough_ticket = []
my_ticket = "EEEE"
while True:
				ticket = lottery()
				if ticket == my_ticket:
								print(f"Your Ticket Found:\nTicket NO.:{ticket}")
								print(len(rough_ticket))
								break
				else:
								print(f"Lottery No.:{ticket}")
								rough_ticket.append(ticket)
								
				


								
								