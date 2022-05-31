"""
    ORM Connection to database
"""
import json
from sqlalchemy import create_engine, event, DDL
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models.models import *
from models.base import Base
event.listen(
    Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS weather_data")
)

class SqlService:
    """
        A class implements the ORM Connection to database.

    """
    def __init__(self, db_params_path = "db_url.json") -> None:
        """
            Init object SqlService with params

            :param db_params_path: Path to json with sql params
               to connection with db
        """
        self.db_params_path = db_params_path
        self.engine = self.__get_engine_from_params()

    def get_session(self):
        """
            Getting session for connection.

        """
        return sessionmaker(bind=self.engine)()

    def __get_engine_from_params(self) -> Engine:
        """
            Getting engine from json.

        """
        with open(self.db_params_path, 'r', encoding='utf-8') as file:
            json_sql:dict = json.load(file)
        keys = ['type','user','password','host','port', 'dbname']
        if not all(key in keys for key in json_sql.keys()):
            raise Exception('Bad config file')

        return self.__get_engine( json_sql['type'],
                                json_sql['user'],
                                json_sql['password'],
                                json_sql['host'],
                                json_sql['port'],
                                json_sql['dbname'])
    def __get_engine(self, typedb, user, password, host, port, dbname) -> Engine:
        """
            Getting or Create Database Engine.

        """
        url = f"{typedb}://{user}:{password}@{host}:{port}/{dbname}"
        if not database_exists(url):
            create_database(url)
        engine = create_engine(url, pool_size=50, echo=False)
        return engine
    def add_objects(self, orm_objects):
        """
            Method for adding ORM object in database.

        """
        sess =  self.get_session()
        sess.add_all(orm_objects)
        sess.commit()
        



if __name__ == "__main__":
    sql_service = SqlService()
    session = sql_service.get_session()
    Base.metadata.create_all(sql_service.engine)
    #result = session.query(City).all()
    #print(result)
    #session.close()
