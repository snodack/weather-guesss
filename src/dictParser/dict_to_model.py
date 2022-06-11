"""
    Class to implement dict parsing to ORM models

"""
from datetime import datetime
from sqlAlchemy.models.models import City, Weather
class DictToModel:
    """
        Class to implement dict parsing to ORM models
    """
    def __init__(self):
        """
            Constructor.
        """
        pass
    def parse_hour_to_model(self, dict_hour, location_id:int) -> Weather:
        """
            Method for parsing weather dict to ORM Object(Weather).
            :param dict_hour: Json weatherapi;
            :param location_id id of the city;
            :return ORM Model of Weather.

        """
        weather_in_hour = Weather(  temp_c=dict_hour["temp_c"],
                                        city_id=location_id,
                                        time = datetime.strptime(dict_hour["time"], "%Y-%m-%d %H:%M"),
                                        is_day=dict_hour["is_day"],
                                        wind_kph=dict_hour["wind_kph"],
                                        wind_degree=dict_hour["wind_degree"],
                                        precip_in=dict_hour["precip_in"],
                                        pressure_in=dict_hour["pressure_in"],
                                        humidity=dict_hour["humidity"],
                                        cloud=dict_hour["cloud"],
                                        will_it_rain=dict_hour["will_it_rain"],
                                        chance_of_rain=dict_hour["chance_of_rain"],
                                        will_it_snow=dict_hour["will_it_snow"],
                                        chance_of_snow=dict_hour["chance_of_snow"])
        return weather_in_hour
    def parse_city_to_model(self, dict_city: dict) -> City:
        """
            Method for parsing dict to ORM Object.
            :param Dictionary Json {"name": London, "state": "Blablabla"}
            :return: ORM Model of City.
        """
        return City(name=dict_city["city"],
                    state = dict_city["state"])
    def parse_list_of_city(self, list_of_dict: list) ->list:
        """
            Method for parsing list of dict to list of ORM Object.
            :param List of Dict Json {"name": London, "state": "Blablabla"}
            :return: list of ORM Model of City.
        """
        return list(map(self.parse_city_to_model, list_of_dict))
        