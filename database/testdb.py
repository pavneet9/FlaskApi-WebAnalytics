from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:pavneet9@34.66.75.237/webevents')

engine.connect()
