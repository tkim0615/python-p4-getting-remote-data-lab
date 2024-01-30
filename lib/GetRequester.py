import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content


    def load_json(self):
        people_list = []
        people = json.loads(self.get_response_body())
        for p in people:
            people_list.append(p)
        return people_list


get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
people_data = get_requester.load_json()
# print (people_data)
        



# Start by creating a GetRequester class. This class should be able to initialize with a string URL.

# The GetRequester class should have a get_response_body method that sends a GET request
#  to the URL passed in on initialization. This method should return the body of the response.

# The GetRequester class should have a load_json method that should use get_response_body 
# to send a request, then return a Python list or dictionary made up of data converted from the response of that request.