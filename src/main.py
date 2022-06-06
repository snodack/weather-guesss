"""
    Main module with executing main logic
"""
from ast import arg
from queue import Queue
from threading import Thread, Event
import datetime
from sqlAlchemy.slq_alchemy_service import SqlService
from dictParser.dictToModel import DictToModel
from weatherHtmlClient.html_client import HtmlClient

if __name__ == "__main__":
    que = Queue(maxsize=3)
    stop_event = Event()
    dictParser = DictToModel()
    sql_service = SqlService()
    html_client = HtmlClient(dictParser, que)
    html_client_thread = Thread(target=html_client.get_historical_data, args=("UFA", datetime.datetime.now(), stop_event))
    sql_service_thread = Thread(target=sql_service.add_objects, args=(que,stop_event))
    html_client_thread.start()
    sql_service_thread.start()
    html_client_thread.join()
    sql_service_thread.join()
    #sql_service_thread =sql_service.
