#!/usr/bin/env python
# coding: utf-8

import requests
import pprint
import json



class MakeApiCall:

    def __init__(self, api):
        self.main_list = []
        self.reviews = ""
        self.get_data(api)

    def get_data(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            print("Successfully fetched the data")
            self.reviews = json.loads(response.content)
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

    def sort_data(self):
        self.reviews = self.reviews['data']['reviews']
        for rev in self.reviews:

            data_id = self.reviews["Id"]
            
            try:
                likes = rev["LikesText"]
            except KeyError:
                likes = ""
            try:
                dislikes = rev["DisLikesText"]
            except KeyError:
                dislikes = ""
            try:
                created = rev["Created"]
            except KeyError:
                created = ""

            self.main_list.append([likes, dislikes, created])

    def show_all(self):
        print("=== Sorted data ===") 
        for i in self.main_list:
            print(i)

if __name__ == "__main__":
    api_call = MakeApiCall("https://www.ambitionbox.com/api/v2/reviews/data/114?page=1&sort=recent")
    api_call.sort_data()
    api_call.show_all()



