import json ,requests,sys , configparser ,textwrap
from bs4 import BeautifulSoup
from prettytable import PrettyTable
# variable
#command line arguments
intitle = sys.argv[1]
tags = sys.argv[2]
#config defaults
config = configparser.SafeConfigParser()
config.read("config.txt")
site = config.get("settings", "site")
pagesize = config.get("settings", "number_of_results")
sort_by = config.get("settings", "sort_by")

#stackexchange url
url ="https://api.stackexchange.com/2.2/"

#api endpoint
search_url ="{}search?".format(url)
search_params ={"pagesize": pagesize,"order":"desc","sort":sort_by,"tags":tags, "intitle": intitle,"site":site}
#retrieving questions that match the query
data  = requests.get(search_url, params=search_params).json()
questions = data["items"]
print('\033[1m')
if not questions:
	print("No questions match your query ,please rephrase your query")
	quit()
print("The following are the top {} which meet your query \n".format(pagesize))
#print top results
t = PrettyTable(["Option","Title", "Score","Answered"])
for index,question in enumerate(questions):
	t.add_row([index+1 ,question["title"],question["score"] ,question["is_answered"] ])

print( t)


option = int(input("\nPlease choose an option you prefer \t"))
if option > int(search_params["pagesize"]):
	print("invalid option")
	quit()
#retrieving the answer
try:
	answer_url = "{0}/answers/{1}".format(url,questions[option-1]["accepted_answer_id"])
	answer_params = {"order":"desc","sort":"votes", "site":"stackoverflow","filter":"withbody"}
	answer_response = requests.get(answer_url, params=answer_params)
	print("The following is the accepted answer to your question \n\n")

except Exception :
	print("Your question doesn't have an accepted answer yet \n\n This is the top aswer so far \n\n")
	qstn_id = questions[option-1]["question_id"]
	surl ="{}questions/{}/answers?".format(url,qstn_id)
	sparams ={"pagesize": 5,"order":"desc","sort":"votes","site":"stackoverflow","filter":"withbody"}
	answer_response = requests.get(surl, params=sparams)

finally:
	#print the answer
	answer_data = answer_response.json()
	answer = answer_data["items"][0]["body"]
	soup = BeautifulSoup(answer, 'html.parser')

	print('\033[94m' + textwrap.indent(soup.get_text(), '       ')+'\033[0m')
print('\033[0m')
