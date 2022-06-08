"""
    Module to getting all City for County/State.
    Modele is using www.universal-tutorial.com, so you need api_token.
"""
import json
from typing import List
import requests
from enum import Enum

class Area_Type:
    """
        Enum class for area type.
        For Type Country -> Find States -> Find City
        For Type State -> Find City
    """
    COUNTRY = 1
    STATE = 2

class CityJsonGetter:
    """
        Main class for getting all City.
    """
    def __init__(self, api_token_json_path:str, city_output_json_path: str) -> None:
        self.auth_token = ""
        self.output_path =  city_output_json_path
        self._get_api_token_from_file(api_token_json_path=api_token_json_path)
        self._get_auth_token_from_api()
    def _get_api_token_from_file(self, api_token_json_path) -> None:
        try:
            with open(api_token_json_path, 'r', encoding='utf-8') as file:
                json_api:dict = json.load(file)
                api_token = json_api.get("api-token", None)
                user_email = json_api.get("user-email", None)
                if api_token is None or user_email is None:
                    raise KeyError()
                self.api_token =  api_token
                self.user_email =  user_email
        except FileNotFoundError:
            print(f"Can't find file: {api_token_json_path}")
        except KeyError:
            print(f"Can't find value \"api_token\" or \"user-email\" \
                    in file: {api_token_json_path}")
    def _get_auth_token_from_api(self):
        """
            Getting auth_token(need to generate every 24 hours)

        """
        resp = requests.request("GET",
                                "https://www.universal-tutorial.com/api/getaccesstoken",
                                headers={"Accept":"application/json",
                                "api-token": self.api_token,
                                "user-email": self.user_email})
        if resp.status_code != 200:
            raise Exception(f"Email:{self.user_email} \
                is not registered in www.universal-tutorial.com")
        resp_json = resp.json()
        self.auth_token = resp_json["auth_token"]
    def _get_all_state(self, country) -> List:
        resp = requests.request("GET",
                                f"https://www.universal-tutorial.com/api/states/{country}",
                        headers={"Accept":"application/json",
                                "Authorization": f"Bearer {self.auth_token}"})
        if resp.status_code != 200:
            raise requests.RequestException(resp)
        return resp.json()
    def _get_all_city_in_state(self,state) -> List:
        resp = requests.request("GET",
                                f"https://www.universal-tutorial.com/api/cities/{state}",
                                headers={"Accept":"application/json",
                                "Authorization": f"Bearer {self.auth_token}"})
        if resp.status_code != 200:
            raise requests.RequestException(resp)
        return resp.json()
    def get_city_json(self, area_string:str, area_type: Area_Type) -> None:
        """
            Get city for area_string. if area_type == country then
            getting all states in; after getting all city for all states
            if area_type == state then getting all city for state
            and write in path.

        """
        if area_type == Area_Type.COUNTRY:
            states = list(map(lambda x: x["state_name"],self._get_all_state(area_string)))
            all_city = []
            for state in states:
                city = list(map(lambda x: x["city_name"],self._get_all_city_in_state(state)))
                all_city.extend(city)
        elif area_type == Area_Type.STATE:
            all_city = list(map(lambda x: x["city_name"],self._get_all_city_in_state(area_string)))
        print(all_city)
        
        
