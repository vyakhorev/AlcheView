# -*- coding: utf-8 -*-

class abst_key(object):
    def __repr__(self):
        return self.string_key()

    def __my_key(self):
        return (self.__tablename__, self.rec_id)

    def string_key(self):
        s_r = ""
        for s in self.__my_key():
            s_r += str(s)
        return s_r

    def __eq__(x, y):
        return x.__my_key() == y.__my_key()

    def __hash__(self):
        return hash(self.__my_key())