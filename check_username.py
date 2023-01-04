import requests
import json

# Replace YOUR_CONSUMER_KEY and YOUR_CONSUMER_SECRET with your Twitter API
# consumer key and secret, respectively
consumer_key = "3KiS2w8prnFWS0BJLc8wnbCii"
consumer_secret = "dIgFmXN2bRqnoaMuEJXtylACAvA1YSkCrbsZEaU3Q3AWEt6Pcr"

# Use the requests library to send a request to the Twitter API to retrieve an
# access token
response = requests.post(
    "https://api.twitter.com/oauth2/token",
    auth=(consumer_key, consumer_secret),
    data={"grant_type": "client_credentials"}
)

# Extract the access token from the response
access_token = response.json()["1366625424302743552-BxbYR5npKJKsDKcKBkGUD26Vi64a8V"]

# Use the access token to authenticate requests to the Twitter API
auth_header = f"Bearer AAAAAAAAAAAAAAAAAAAAAA32kwEAAAAAx1IINmWEdgkFwgnaQ%2B6cJOMPHKU%3DbooHynMG6i3XXK8ngGlvC8o3EfU0WdGYQw4aTRBfKohk6voFC9"

# Use the requests library to send a request to the Twitter API to check if a
# username is available
def check_username_availability(username):
  url = f"https://api.twitter.com/2/users/username_available.json?username={username}"
  headers = {"Authorization": auth_header}
  response = requests.get(url, headers=headers)
  data = response.json()
  return data["available"]

# Check if the username "johndoe" is available
username = "johndoe"
available = check_username_availability(username)
if available:
  print(f"The username {username} is available!")
else:
  print(f"The username {username} is not available.")
