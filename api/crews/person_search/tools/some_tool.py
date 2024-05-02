import json
import os
import requests

from langchain.tools import tool


def search(some_param: dict) -> dict:
    """Useful to find information about a person on social media"""
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = os.getenv('PROXY_CURL_TOKEN')

    if not api_key:
        return {'error': 'Missing API key', 'status_code': 400}

    headers = {'Authorization': 'Bearer ' + api_key}
    params = {
        # 'extra': 'include',
        # 'github_profile_id': 'include',
        # 'facebook_profile_id': 'include',
        # 'twitter_profile_id': 'include',
        # 'personal_contact_number': 'include',
        # 'personal_email': 'include',
        # 'inferred_salary': 'include',
        # 'skills': 'include',
        'use_cache': 'if-present',
        'fallback_to_cache': 'on-error',
    }

    params.update(some_param)

    print("***** Searching social media... *****")
    print(f"Params: {params}")
    print(f"api_endpoint: {api_endpoint}")
    print(f"api_key: {api_key}")

    response = requests.get(api_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data', 'status_code': response.status_code}


class SocialMediaProfileTool:

    @staticmethod
    @tool("Retrieves linkedIn user information using the Proxycurl API")
    def search_linkedin(url: str) -> dict:
        """Useful to find user data from linkedIn"""

        if os.getenv('PROXY_CURL_PRE_FETCHED_DATA'):
            json_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'io', 'templates', 'linkedin_example.json')
            with open(json_path, 'r') as file:
                return json.load(file)

        linkedin = {
            'linkedin_profile_url': url
        }

        return search(linkedin)

    @staticmethod
    @tool("Retrieves twitter user information using the Proxycurl API")
    def search_twitter(url: str) -> dict:
        """Useful to find user data from twitter"""

        if os.getenv('PROXY_CURL_PRE_FETCHED_DATA'):
            json_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'io', 'templates', 'twitter_example.json')
            with open(json_path, 'r') as file:
                return json.load(file)

        twitter = {
            'twitter_profile_url': url
        }

        return search(twitter)

    @staticmethod
    @tool("Retrieves facebook user information using the Proxycurl API")
    def search_facebook(url: str) -> dict:
        """Useful to find user data from facebook"""

        if os.getenv('PROXY_CURL_PRE_FETCHED_DATA'):
            json_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'io', 'templates', 'facebook_example.json')
            with open(json_path, 'r') as file:
                return json.load(file)

        facebook = {
            'facebook_profile_url': url
        }

        return search(facebook)
