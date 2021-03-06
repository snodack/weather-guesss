"""
    This Module implements API connection to Wetheapi.com
"""
import json
from datetime import datetime, timedelta
from sqlAlchemy.models.models import City, Weather
import requests

class HtmlClient:
    """
        A class implements the API connection mechanism.
    """
    def __init__(self, parser, que, file_api = "api.json") -> None:
        """
            Init object HtmlClient with params

            :param file_api: Path to json with API key
                like {"key": "HiimYourKeyToWeatherapi.com"},
            :param parser: Parser object, with method parse_to_model,
            :param queue: Queue to return value.
        """
        self.parser = parser
        self.que = que
        try:
            with open(file_api, 'r', encoding='utf-8') as file:
                json_api:dict = json.load(file)
                key = json_api.get("key", None)
                if key is None:
                    raise Exception()
                self.api_key = key
        except FileNotFoundError:
            print(f"Can't find file: {file_api}")
        except Exception:
            print(f"Can't find value \"key\" in file: {file_api}")
    def get_historical_data(self, city:City, date: datetime, stop_event=None):
        """
            Getting data for day From API Free Weather.

            :param location: Getting weather for this US Zipcode, UK Postcode, Canada Postalcode,
                IP address, Latitude/Longitude (decimal degree) or city name
            :param date: Date, which you want to get.
        """

        resp = requests.request("GET",
                        "http://api.weatherapi.com/v1/history.json",
                        params={"key":self.api_key,
                        "q": city.long_lat,
                        "dt": date.strftime("%Y-%m-%d")})
        try:
            if resp.status_code != 200:
                raise Exception(f"Can't get Historical Date {resp.status_code}")
            if resp.status_code == 400:
                print(f"can't find the city: {city.long_lat}")
            responce_json = resp.json()
            hours = responce_json["forecast"]["forecastday"][0]["hour"]
            for hour in hours:
                self.que.put(self.parser.parse_hour_to_model(hour, city.id))
        except Exception:
            print("Error with data {data}")
        if not stop_event is None:
            stop_event.set()
    def get_last_week_data(self, list_of_city: list,  stop_event):
        """
            Get weather data about location
            :param list_of_city
            :param stop_event - event that will be set after all querys
        """
        date = datetime.now()
        for city in list_of_city:
            for minus_day in range(0, 8):
                current_date = date - timedelta(days=minus_day)
                self.get_historical_data(city= city, date=current_date)
        stop_event.set()

    

