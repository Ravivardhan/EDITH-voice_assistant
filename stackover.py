import shlex
import requests
from subprocess import Popen, PIPE



def make_request(error):
    print("Searching for "+error)
    resp  = requests.get("https://api.stackexchange.com/"+"2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    return resp.json()

def get_urls(json_dict):
    url_list = []
    count = 0
    for i in json_dict['items']:
        if i["is_answered"]:
            url_list.append(i["link"])
        count+=1
        if count == len(i) or count == 3:
            break
    import webbrowser
    for i in url_list:
        webbrowser.open(i)




def stack_overflow(error):

    error_message = error
    print(error_message)
    if error_message:
        filter_out = error_message.split(":")
        print(filter_out)
        print(filter_out[0])
        json1 = make_request(filter_out[0])

        json = make_request(error_message)
        get_urls(json1)

        get_urls(json)
    else:
        print("No errors")