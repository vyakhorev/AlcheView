# -*- coding: utf-8 -*-
from db_exec import BASE
from db_handlers import engine

from db_model import *

BASE.metadata.create_all(engine)

from db_handlers import the_session_handler


if __name__ == "__main__":
    # Create fake records
    import datetime
    td = datetime.datetime.today()
    tom = td + datetime.timedelta(days=1)
    imwk = td + datetime.timedelta(days=7)
    yst = td + datetime.timedelta(days=-1)
    rec1 = c_EventRecord(headline="Annual meeting", text="blah-blah-blah",date_added=td,due_date=imwk)
    rec2 = c_EventRecord(headline="Monthly meeting", text="bul-bul-bul",date_added=yst,due_date=tom)
    rec3 = c_NewsRecord(headline="Meeting overview", text="that was nice",date_added=yst)
    the_session_handler.add_object_to_session(rec1)
    the_session_handler.add_object_to_session(rec2)
    the_session_handler.add_object_to_session(rec3)
    the_session_handler.commit_and_close_session()