import mechanize #sudo pip install python-mechanize

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

gitbot = br.open("https://docs.google.com/forms/d/e/1FAIpQLSc-fTsjkPPm-IH6jshrGZXSVI19VNXs2_2S3BbJCYJD9Nz7UQ/formResponse") #requesting the github base url

br.select_form(nr=1) #the sign up form in github is in third position(search and sign in formscome before signup)

br["entry.826740370"] = "Blake Hodges"

sign_up = br.submit()
