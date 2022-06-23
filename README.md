# Amazon Customer Review

This body of work is a review of amazon's employees response to the co pany's  policies and working conditions.


# Main script

import requests
import json


class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        # self.get_data(api)

        parameters = {
            "pros": " ",
            "cons": " ",
            "date": " "
        }
        self.get_user_data(api,parameters)


if __name__ == "__main__":
    api_call = MakeApiCall("https://www.ambitionbox.com/api/v2/reviews/data/114?page=1&sort=recent")
