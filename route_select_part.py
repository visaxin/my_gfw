import os
import sqlite3
class GfwList(object):
    def __init__(self,domain):
        self.domain= domain
        self.conn = sqlite3.connect('gfwlist.db')
    def _add_():
        c = self.conn.cursor()
        c.execute("insert in to gfw values ('%s')"%self.domain)
        self.conn.commit()
    def _check_from_db():
        c = self.conn.cursor()
        res = c.execute("select * from gfw")
        if self.domain in res:
            return True
        else:
            return False
    def _route_select():
        if _check_from_db():
            return True
        else:
            response = os.system("ping -n 1 " + self.domain)
            if response == 0:
                return False
            else:
                _add_()
                return False

route_select('www.google.com')
