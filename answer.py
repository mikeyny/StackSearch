import json ,requests,sys
from bs4 import BeautifulSoup
#stackexchange url
url ="https://api.stackexchange.com/2.2/"
#variables
intitle = input("Please input your search query \n")
tags = input("\n Please input tags associated with your query b \n")
#api endpoint
search_url ="{}search?".format(url)
search_params ={"pagesize": 5,"order":"desc","sort":"votes","tags":tags, "intitle": intitle,"site":"stackoverflow"}
#retrieving answers
search_response = requests.get(search_url, params=search_params)
data = search_response.json()
questions = data["items"]
print("The following are the top 5 which meet your query \n")

i =0
for question in questions:
	
	print("Option" ,i+1 ,question["title"],"       score:",question["score"] ,"       answered ?:",question["is_answered"] ,"\n")
	i = i + 1

option = int(input("\n please choose an option you prefer"))
if option > search_params["pagesize"]:
	print("invalid option")
	sys.exit()

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
	answer_data = answer_response.json()
	answer = answer_data["items"]
	html_doc = answer[0]["body"]
	soup = BeautifulSoup(html_doc, 'html.parser')

	print(soup.get_text())	




