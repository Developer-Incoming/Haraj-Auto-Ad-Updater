# Internal Libraries
import sys
from requests import utils, post, get
import json
import time

# External Libraries
import config # local
import colorama

# Variables
# utils.default_user_agent = lambda: "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.3"
# headers = utils.default_headers()

auth = config.auth
postId = config.postId
english = config.english
# headers["authorization"] = auth

## colors for aesthetics
class colors:
    end = "\033[0m"
    black = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    white = "\033[97m"

# Function
def updateAd(ad_id: int):
    json_data = {
        "query": "mutation updatePost($token: String!, $id: Int!) {\n    \n  updatePost(token: $token, id: $id)\n  { \n\t\t\t\t  status\n\t\t\t\t  notValidReason\n\t\t\t\t   }\n  \n  }",
        "variables": {
            "token": auth.removeprefix("Bearer "),
            "id": ad_id,
        },
    }

    response = post(
        f"https://graphql.haraj.com.sa/?queryName=updatePost{'&lang=en' if english else ''}",
        # cookies=cookies,
        # headers=headers,
        json=json_data,
    )

    print(f'{colors.green if response.status_code == 200 else colors.red }{response} {colors.black}- {colors.white}{json.dumps(json.loads(response.content), indent=4).encode(sys.getfilesystemencoding()).decode("unicode-escape")}')
    

# Main
## will make it run every day or two using the windows process schedule
colorama.init() # i lost and needed to use this :( , but hey it works!
updateAd(ad_id=postId)
input(f"{colors.blue}\nPress enter to exit the Haraj Ad Auto Updater :){colors.end}")
