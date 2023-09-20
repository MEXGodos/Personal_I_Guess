import requests
lines = []

while True:
    response = requests.get('http://172.25.0.20?guess=20')
    #fetch the page with the cookie set and return the response
    currentPageText = response.text
    # Save the current apge text to a variable
    if "wrong!" not in currentPageText:
        print(response.text)
    #Check to see if the text above is not there. If it's not, show us what actually was returned!
