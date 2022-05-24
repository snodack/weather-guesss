"""
    This Module implements API connection to Wetheapi.com
"""
import json
from datetime import datetime
from click import FileError
import requests

class HtmlClient:
    """
        A class implements the API connection mechanism.
    """
    def __init__(self, file_api = "api.json"):
        """
            Init object HtmlClient with params

            :param file_api: Path to json with API key
                like {"key": "HiimYourKeyToWeatherapi.com"}
        """

        try:
            with open(file_api, 'r', encoding='utf-8') as file:
                json_api:dict = json.load(file)
                key = json_api.get("key", None)
                if key is None:
                    raise FileError
                self.api_key = key
        except FileNotFoundError:
            print(f"Can't find file: {file_api}")
        except FileError:
            print(f"Can't find value \"key\" in file: {file_api}")
    def get_historical_data(self, location: str, date: datetime) -> dict:
        """
            Getting data for day From API Free Weather.

            :param location: Getting weather for this US Zipcode, UK Postcode, Canada Postalcode,
                IP address, Latitude/Longitude (decimal degree) or city name
            :param date: Date, which you want to get.
            :return: dict with weather data
        """

        resp = requests.request("GET",
                        "http://api.weatherapi.com/v1/history.json",
                        params={"key":self.api_key,
                        "q": location,
                        "dt": date.strftime("%Y-%m-%d")})
        if resp.status_code != 200:
            raise Exception(f"Can't get Historical Date {resp.status_code}")
        print(type(resp.json()))

if __name__ == "__main__":
    htmlclient = HtmlClient()
    htmlclient.get_historical_data("UFA", datetime.now())
