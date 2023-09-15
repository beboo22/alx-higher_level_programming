#!/usr/bin/python3

"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name="Louisiana")
    session.add(newstate)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
