#!/usr/bin/python3

"""Start link class to table in the database
"""
from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_and_states = session.query(City, State)
    .filter(City.state_id == State.id).order_by(City.id).all()

    for city, state in cities_and_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
