# encoding: utf-8
"""
Parser for tab file
"""
from app.sales.models import Sale
from django.utils.encoding import force_unicode

class TabFileParser(object):
    columns = 6
    ignore_first_line = True
    object_class = Sale

    def __init__(self, tab_file):
        self.tab_file = tab_file

    def seek(self):
        '''
        Seek file to position 0.
        Ignore first line if this is set.
        '''
        self.tab_file.seek(0)
        if self.ignore_first_line:
            self.tab_file.readline()

    def sales(self):
        assert self.check_file(), u'File is invalid'
        for line in self.tab_file.readlines():
            split = line.split('\t')
            yield self.make_object(split)

    def make_object(self, split):
        '''
        Return an object filled with data passed on split
        :split: tuple with data (eg: row)
        '''
        return self.object_class(
            client_name = force_unicode(split[0]),
            item_description = force_unicode(split[1]),
            item_price = split[2],
            purchase_count = int(split[3]),
            saller_address = force_unicode(split[4]),
            saller_name = force_unicode(split[5]),
            )

    def check_file(self):
        '''
        Check if all lines on file have %columns% columns
        '''
        if hasattr(self, '_valid_file'):
            return self._valid_file

        for line in self.tab_file.readlines():
            split = line.split('\t')
            if len(split) < self.columns:
                self._valid_file = False
                self.seek()
                return False
        self._valid_file = True
        self.seek()
        return True


