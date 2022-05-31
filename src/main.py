"""
    Main module with executing main logic
"""
from ast import arg
from Queue import Queue
from threading import Thread
import datetime
from sqlAlchemy.slq_alchemy_service import SqlService
from weatherHtmlClient.html_client import HtmlClient

if __name__ == "__main__":
    que = Queue(maxsize=0)
    sql_service = SqlService()
    html_client = HtmlClient()
    html_client_thread = Thread(target=html_client.get_historical_data, args=("UFA", datetime.datetime.now()))
    sql_service.add_objects(que)
    #sql_service_thread =sql_service.
