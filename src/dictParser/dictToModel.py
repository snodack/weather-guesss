"""
    Class to implement dict parsing to ORM models

"""
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
    def parse_to_model(self, dict_hour) -> Weather:
        """
            Method for parsing dict to ORM Object.
            :param array_by_dict_hour: Dictionary json weatherapi
            :return: list, of ORM Models.
        """
 
        weathet_in_hour = Weather(  temp_c=dict_hour["temp_c"],
                                        city_id=1,
                                        is_day=dict_hour["is_day"],
                                        wind_kph=dict_hour["wind_kph"],
                                        wind_degree=dict_hour["wind_degree"],
                                        precip_in=dict_hour["precip_in"],
                                        pressure_in=dict_hour["pressure_in"],
                                        humidity=dict_hour["humidity"],
                                        cloud=dict_hour["cloud"],
                                        will_it_rain=dict_hour["will_it_rain"],
                                        chance_of_rain=dict_hour["chance_of_rain"],
                                        will_it_show=dict_hour["will_it_snow"],
                                        chance_of_snow=dict_hour["chance_of_snow"])
        return weathet_in_hour

        