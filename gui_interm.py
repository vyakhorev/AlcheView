# -*- coding: utf-8 -*-

from db_model import c_EventRecord, c_NewsRecord
from db_handlers import the_session_handler

class c_ItemIntermidiate(object):
    def __init__(self, sa_obj):
        self.sa_obj = sa_obj

    def build_HTML(self):
        raise NotImplementedError

class c_ListIntermidiate(object):
    def __init__(self, sa_cls_list):
        self.sa_cls_list = sa_cls_list
        # Each element
        self.d_links = dict()

    def parse_url(self, url_body):
        return self.d_links[url_body].obj

    def create_edit_link(self, obj, link_name):
        new_link = c_link(command="edit",obj=obj, label=link_name)
        self.d_links[new_link.get_key()] = new_link
        return new_link.get_html()

    def build_HTML(self):
        s = ""
        obj_list = []
        for cls in self.sa_cls_list:
            obj_list += the_session_handler.get_all_objects_list(cls)
        for obj in obj_list:
            s += self.build_item_HTML(obj)
            s += "<br><br>"
            #self.d_links[link] = (obj)
        return s

class c_link():
    # Всё что нужно от этого объекта - сделать уникальную ссылку и потом
    # по ней найти объект.
    def __init__(self, command, obj, label):
        self.command = command
        self.obj = obj
        self.label = label

    def get_key(self):
        return self.command + ":" + self.obj.string_key()

    def get_html(self):
        return '<a href="%s">%s</a>'%(self.get_key(),self.label)

    def __eq__(x, y):
        return x.get_key() == y.get_key()

    def __hash__(self):
        return hash(self.get_key())

class c_RecordList_intm(c_ListIntermidiate):
    def build_item_HTML(self, obj):
        s = ""
        # Вставляем ссылку для печати
        s += obj.date_added.strftime("%Y %B %d (%A)")
        s += "   <b>" + obj.headline + "<b><br>"
        s += self.create_edit_link(obj,"edit this record")+"<br>"
        s += obj.text
        return s

