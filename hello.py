from flask import Flask
from dateutil import parser
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
 content = requests.get('https://9g9xhayrh5.execute-api.us-west-2.amazonaws.com/test/data')
 response = content.json() # reads the data as JSON, into a dict-like object
 response.keys()
 emailList = [user['email'] for user in response['data']]
 uniqueEmails = set(emailList)
 answers = {'Emails': uniqueEmails}

 domain = []

 for email in uniqueEmails:
  if email is not None:
   domain.append('@' + email.split('@')[1])

   # print domain

 

 uniqueDomain = set(domain)
 uniqueDict = dict.fromkeys(uniqueDomain, 0)
 
 count = 0

 overOne = {}

 for uniq in uniqueDomain:
 	for email in domain:
 		# print 'unique: ', uniq, ' email: ', email
 		if uniq == email:
 			count = count + 1
 			uniqueDict[uniq] = uniqueDict[uniq] + 1
 			if uniqueDict[uniq] > 1:
 				overOne.update({uniq: uniqueDict[uniq]})
 		

 answers.update({'# of Emails per Domain': overOne})

 aprilList = []
 # print answers

 loggedList = [user['login_date'] for user in response['data']]
 # for login in loggedList:
 # 	if login is not None:
 # 	 groups = login.split('-')
 # 	 aprilList.append(groups[1])
 # print loggedList
 for date in loggedList:
 	if date is not None:
 	 d = parser.parse(date)
 	 aprilList.append(d.month)

 # print aprilList
 
 aprilCount = 0

 for month in aprilList:
 	if month == 4:
 		aprilCount = aprilCount + 1

 answers.update({'April Users': aprilCount})

 # print answers
 answers['Emails'] = list(answers['Emails'])
 answers = json.dumps(answers)
 print answers
 r = requests.post('https://9g9xhayrh5.execute-api.us-west-2.amazonaws.com/test/data', json = answers)
 print r.text

 # print answers
 
 




 return 'check console'

if __name__ == '__main__':
    app.run(debug=True)