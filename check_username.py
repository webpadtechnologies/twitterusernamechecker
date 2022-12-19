import requests
import json

# Replace YOUR_CONSUMER_KEY and YOUR_CONSUMER_SECRET with your Twitter API
# consumer key and secret, respectively
consumer_key = "BRai9sz3p6bTcqgKowW2YYaFn"
consumer_secret = "F5MDKIWgjgBhN4UEqnMEG01mfo95J8sNKyTUaDtVy5NlfbkUHo"

# Use the requests library to send a request to the Twitter API to retrieve an
# access token
response = requests.post(
    "https://api.twitter.com/oauth2/token",
    auth=(consumer_key, consumer_secret),
    data={"grant_type": "client_credentials"}
)

# Extract the access token from the response
access_token = response.json()["AAAAAAAAAAAAAAAAAAAAACxMkgEAAAAAovUYIgSrZ%2BwuEdF%2Fe%2BJnXywYnuM%3DitPR7vr5DvnjPlEKToqyBrQ2V5tAyeiHElxqrQzGaJQX5vFpp3"]

# Use the access token to authenticate requests to the Twitter API
auth_header = f"Bearer {AAAAAAAAAAAAAAAAAAAAACxMkgEAAAAAovUYIgSrZ%2BwuEdF%2Fe%2BJnXywYnuM%3DitPR7vr5DvnjPlEKToqyBrQ2V5tAyeiHElxqrQzGaJQX5vFpp3}"

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
