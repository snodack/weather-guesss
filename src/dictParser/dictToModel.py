"""
    Class to implement dict parsing to ORM models

"""
from src.sqlAlchemy.models.models import City, Weather
class DictToModel:
    """
        Class to implement dict parsing to ORM models
    """
    def __init__(self):
        """
            Constructor.
        """
        pass
    def parse_to_model(self, array_by_dict_hour) -> list:
        """
            Method for parsing dict to ORM Object.
            :param array_by_dict_hour: Dictionary json weatherapi
            :return: list, of ORM Models.
        """
        all_hours_dict = array_by_dict_hour["forecast"]["forecastday"]["hour"]
        weather_orm_models = []
        for hour in all_hours_dict:
            weathet_in_hour = Weather(  temp_c=hour["temp_c"],
                                        city_id=1,
                                        is_day=hour["is_day"],
                                        wind_kph=hour["wind_kph"],
                                        wind_degree=hour["wind_degree"],
                                        precip_in=hour["precip_in"],
                                        pressure_in=hour["pressure_in"],
                                        humidity=hour["humidity"],
                                        cloud=hour["cloud"],
                                        will_it_rain=hour["will_it_rain"],
                                        chance_of_rain=hour["chance_of_rain"],
                                        will_it_show=hour["will_it_show"],
                                        chance_of_snow=hour["chance_of_snow"])
            weather_orm_models.append(weathet_in_hour)
        return weathet_in_hour

        