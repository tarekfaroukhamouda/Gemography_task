from flask import Flask
from flask import Response
app = Flask(__name__)

@app.route('/')
def language_counter():

    import requests 
    import httplib2
    import urllib
    import json
    all_language=[]
    all_users={}
    languages={}
    all_data=[]
    list_of_users=[]
    response2 = requests.get("https://api.github.com/search/repositories?q=created:>2020-03-01&sort=stars&order=desc")
    for item in response2.json()['items']:

              

            if item['language'] not in languages and item['language'] not in all_users:
                languages[item['language']]=1
                all_users[item['language']]=str(item['name'])
                
             
            else:
                languages[item['language']]+=1
                all_users[item['language']]+=","+item['name']

    all_data.append(languages)
    all_data.append(all_users)
                                        
    return Response(json.dumps(all_data))
    
