#!/usr/bin/env python

class Table:

    def __init__(self, name) :
        self.rows = []
        self.name = name
        self.title = None

    def add_row(self,lt) :
        self.rows.append(lt)

    def set_title(self,lt) :
        self.title = lt

    def to_html(self) :
        is_blue = False
        html = "<h3>" + self.name + "</h3>"
        html += "\n<table border=\"1\">"
        html += "\n<tr>"
        for t in self.title :
            html += "\n<th>" + t + "</th>" 
        html += "\n</tr>"
        for row in self.rows :
            if is_blue :
                html += "\n<tr bgcolor=#c0ffff>"
                is_blue = False
            else :
                html += "\n<tr bgcolor=white>"
                is_blue = True
            for it in row :
                html += "\n<th>" + str(it) + "</th>"
            html += "</tr>"
        html += "</table>"
        return html
