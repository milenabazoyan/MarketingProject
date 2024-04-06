from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from faker import Faker
import random

Base = declarative_base()
fake = Faker()

class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    material = Column(String)
    style = Column(String)
    color = Column(String)
    picture_id = Column(Integer, ForeignKey('picture.picture_id'))
    # Define relationships
    picture = relationship('Picture', back_populates='items')
    sales_outcomes = relationship('Sales_Outcome', back_populates='item')
    trends = relationship('Trend', back_populates='item')
    search_frequencies = relationship('Search_Frequency', back_populates='item')

class Picture(Base):
    __tablename__ = 'picture'
    picture_id = Column(Integer, primary_key=True)
    date_taken = Column(Date)
    # Define relationships
    items = relationship('Item', back_populates='picture')

class Sales_Outcome(Base):
    __tablename__ = 'sales_outcome'
    sales_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.item_id'))
    sales_volume = Column(Float)
    sales_date = Column(Date)
    # Define relationships
    item = relationship('Item', back_populates='sales_outcomes')

class Trend(Base):
    __tablename__ = 'trend'
    trend_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.item_id'))
    trend_score = Column(Float)
    trend_date = Column(Date)
    season = Column(String)
    # Define relationships
    item = relationship('Item', back_populates='trends')

class Search_Frequency(Base):
    __tablename__ = 'search_frequency'
    frequency_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.item_id'))
    date_recorded = Column(Date)
    search_count = Column(Integer)
    # Define relationships
    item = relationship('Item', back_populates='search_frequencies')


# Replace 'sqlite:///your_database.db' with the path to your actual database file
engine = create_engine('sqlite:///FashionAnalysis_temp.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.commit()

# Define how many entries you want for each table
NUM_ENTRIES = 100

# Generate data for all the tables
items_data = [{
    'item_id': i,
    'name': fake.word().capitalize(),
    'description': fake.text(max_nb_chars=50),
    'category': random.choice(['dresses', 'tops', 'pants']),
    'material': random.choice(['cotton', 'polyester', 'wool', 'linen']),
    'style': random.choice(['casual', 'formal', 'sporty']),
    'color': fake.color_name(),
    'picture_id': i
} for i in range(1, NUM_ENTRIES + 1)]

pictures_data = [{
    'picture_id': i,
    'date_taken': fake.date_between(start_date='-5y', end_date='today')
} for i in range(1, NUM_ENTRIES + 1)]

sales_outcomes_data = [{
    'sales_id': i,
    'item_id': random.randint(1, NUM_ENTRIES),
    'sales_volume': random.randint(1, 100),
    'sales_date': fake.date_between(start_date='-1y', end_date='today')
} for i in range(1, NUM_ENTRIES + 1)]

trends_data = [{
    'trend_id': i,
    'item_id': random.randint(1, NUM_ENTRIES),
    'trend_score': round(random.uniform(0, 100), 2),
    'trend_date': fake.date_between(start_date='-1y', end_date='today'),
    'season': random.choice(['Spring', 'Summer', 'Fall', 'Winter'])
} for i in range(1, NUM_ENTRIES + 1)]

search_frequencies_data = [{
    'frequency_id': i,
    'item_id': random.randint(1, NUM_ENTRIES),
    'date_recorded': fake.date_between(start_date='-1y', end_date='today'),
    'search_count': random.randint(0, 500)
} for i in range(1, NUM_ENTRIES + 1)]

# Insert data into the database
Session = sessionmaker(bind=engine)
session = Session()

for item in items_data:
    session.add(Item(**item))
for picture in pictures_data:
    session.add(Picture(**picture))
for sales_outcome in sales_outcomes_data:
    session.add(Sales_Outcome(**sales_outcome))
for trend in trends_data:
    session.add(Trend(**trend))
for search_frequency in search_frequencies_data:
    session.add(Search_Frequency(**search_frequency))

session.commit()
session.close()