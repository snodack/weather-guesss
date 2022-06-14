"""
    Main module with executing main logic
"""
from ast import arg
from queue import Queue
from threading import Thread, Event
import datetime
from sqlAlchemy.slq_alchemy_service import SqlService
from dictParser.dict_to_model import DictToModel
from weatherHtmlClient.html_client import HtmlClient

if __name__ == "__main__":
    que = Queue(maxsize=3)
    stop_event = Event()
    dictParser = DictToModel()
    sql_service = SqlService()
    city = sql_service.get_city(id=1)
    html_client = HtmlClient(dictParser, que)
    #sql_service.add_city(dictParser.parse_list_of_city(sql_service.get_city_from_json_path("ru.json")))
    html_client_thread = Thread(target=html_client.get_last_week_data, 
                                args=(city, stop_event))
    sql_service_thread = Thread(target=sql_service.add_objects, args=(que,stop_event))
    html_client_thread.start()
    sql_service_thread.start()
    sql_service_thread.join()
