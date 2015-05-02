# -*- coding: utf-8 -*-

from db_exec import BASE
from db_shared import *

class c_EventRecord(BASE, abst_key):
    __tablename__ = "event_records"
    rec_id = Column(Integer, primary_key=True)
    headline = Column(Unicode(255))
    text = Column(Unicode(255))
    date_added = Column(DateTime)
    due_date = Column(DateTime)

    def __repr__(self):
        return self.headline + " @ " + self.due_date.strftime("%x")

class c_NewsRecord(BASE, abst_key):
    __tablename__ = "news_records"
    rec_id = Column(Integer, primary_key=True)
    headline = Column(Unicode(255))
    text = Column(Unicode(255))
    date_added = Column(DateTime)

    def __repr__(self):
        return self.headline