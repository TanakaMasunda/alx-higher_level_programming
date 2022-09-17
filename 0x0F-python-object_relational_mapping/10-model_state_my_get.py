#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_al = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_al)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == sys.argv[4]).first()

    for instance in None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
