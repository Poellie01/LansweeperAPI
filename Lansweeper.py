import requests
import json
import webbrowser
import terminal_banner
import pprint
from base64 import b64encode
from pyfiglet import Figlet
from termcolor import colored

#pls dont laugh

#credentials for api and standard api url
api_key = "Key=APIKEY"
api_urlBase = "http://http://lansweeperserver:port/api.aspx?"
ticket_urlBase = "http://lansweeperserver:port/helpdesk/ticket.aspx?tid="

#print nice banner
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
lansweeper_banner = Figlet(font='graffiti')
print(lansweeper_banner.renderText('Lansweeper'))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

#choice what you wanna do
keuze = input("Enter your choice [1-9]\n\n1: AddTicket | 2: EditTicket | 3: SearchUsers | 4: SearchTicket |\n\n5: Add a Note | 6: Get notes of ticket | 7: Edit a note | 8: Add Asset to Ticket | 9: View an Ticket ")
keuze = int(keuze)

#standaard functie die in elke if statement word gebruikt. behalve add ticket
def web_filesave():
	fileDe = input("Do you want to save the results to a file? (y/n)")
	if fileDe == "y":
		filename = input("Name of the file (Put the extension behind it, filename.txt, filename.json):  ")
		filename = str(filename)
		with open(filename, 'w') as json_file:
			json.dumps(pprint.pprint(response.json(), json_file))
	openWeb = input("want to open webbrowser? (yes/n)")
	if openWeb == "y" or openWeb == "yes":
		webbrowser.open(ticket_urlBase + ticketid)
	
#Too many if statements but idc 
if keuze == 1:
	action = "AddTicket"
	subj = input("What is the Subject ?: ")
	desc = input("What is the description ?: ")
	user = input("Which user creates this ticket ? Use \ infront of the name:")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&Subject=" + subj + "&Description=" + desc + "&Username=sgg" + user)

elif keuze == 2:
	action = "EditTicket"
	ticketid = input("What is the ticket ID? ")
	newsub = input("What is the new subject?")
	newdesc = input("What is the new description?")
	newuser = input("Which user is editing this ticket? ")
	prio = input("What is the priority? [High, Medium, low]")
	newstate = input("What is the state? [Open, Closed] ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&TicketID=" + ticketid + "&Subject=" + newsub + "&Description=" + newdesc + "&Priority=" + prio + "&State=" + newstate + "&Username=" + newuser)
	web_filesave();

elif keuze == 3:
	action = "SearchUsers"
	searchUs = input("What is the name of the user? (Full name) ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&Name=" + searchUs)
	web_filesave()
	
elif keuze == 4:
	action = "SearchTickets"
	searchState = input("What is the state of the ticket? [open, closed] ")
	searchPrio = input("What is the priority of the ticket? [high, medium, low] ")
	searchAgentID = input("What is the AgentID that created the ticket? ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&State=" + searchState + "&Priority=" + searchPrio + "&AgentID=" + searchAgentID)
	web_filesave()

elif keuze == 5:
	action="AddNote"
	ticketid = input("What is the ticket id?")
	text = input("Message: ")
	user = input("Who wrote that? [Use \ infront of the username]")
	Ttype = input("Public or Private? ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&TicketID=" + ticketid + "&Text=" + text + "&Username=sgg" + user + "&Type=" + Ttype)
	web_filesave();

elif keuze == 6:
	action = "GetNotes"
	ticketid = input("What is the ticketID? ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&TicketID=" + ticketid)
	web_filesave();

elif keuze == 7:
	action = "EditNote"
	noteid = input("What is the note ID? ")
	text = input("New note: ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&NoteID=" + noteid + "&Text=" + text)
	web_filesave();

elif keuze == 8:
	action = "AddAsset"
	ticketid = input("What is the Ticket ID? ")
	assetname = input("What is the asset name? ")
	ip = input("What is the IP address? ")
	response = requests.get(api_urlBase + "Action= " + action + "&" + api_key + "&TicketID=" + ticketid + "&Assetname=" + assetname + "&IPAdress=" + ip)
	web_filesave();

elif keuze == 9:
	action = "GetTicket"
	ticketid = input("What is the Ticket id? ")
	response = requests.get(api_urlBase + "Action=" + action + "&" + api_key + "&TicketID=" + ticketid)
	web_filesave();
	
#print the response in json format	
pprint.pprint(response.json()) 