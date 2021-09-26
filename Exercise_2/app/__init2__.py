
# importing the requests library 
import requests 
import json
  
# defining the api-endpoint  
API_ENDPOINT = "http://localhost:5000/classify"
  
# API key here 
# API_KEY = "XXXXXXXXXXXXXXXXX"
  
  
# data to be sent to api 
data = { "title": "1 paar shchuhe " }
finalJson = json.dumps(data)
headers= {"Content-Type": "application/json"}

  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = finalJson,headers=headers) 


# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)  