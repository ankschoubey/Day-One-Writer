import sys
import logging
import os
import time
from datetime import datetime
import uuid
class Entry:
    text = ''
    tags = []
    date = None
    photos = []
    journal = None
    starred = False
    coordinate = []
    timezone = None


class DayOne:
    """
    use DayOne() object's .push(entry) method send something to dayone
    """

    def __init__(self,default_journal = None):
        self.default_journal = journal

    def _single_escape(self,text):
        for i in ['|','`','(',')']:
            text = text.split(i)
            joiner = '\\'+i
            text = joiner.join(text)
        return text
    def escape(self,text):

        if type(text) == list:
            temp = []
            for i in text:
                temp.append(self._single_escape(i))
            return temp
        return self._single_escape(text)
    def get_journal(self, journal):
        if not journal and not self.default_journal:
            return ''
        if journal:
            return '-j ' + journal
        return '-j ' + self.default_journal

    def format_tags(self,tags):

        if len(tags) == 0:
            return ''
        for i in range(len(tags)):
            tags[i] = str(tags[i])
            tags[i] = '\ '.join(tags[i].split(' '))
        tags = self.escape(tags)
        return '--tags '+ ' '.join(tags)

    def format_date(self,date):
        #--date='2015-06-01 15:53:10'
        if type(date) is not datetime:
            raise Exception('date is of type: ' +type(date)+'.Change date attribute of Entry to a datetime object.')

        return '--date \'' + date.strftime('%Y-%m-%d %H:%M:%S')+'\''


    @staticmethod
    def create_unique_file():
        return uuid.uuid4().hex

    @staticmethod
    def delete_file(name):
        os.remove(name)

    def format_system_address(self,address):
        address = address.split(' ')
        address = '\ '.join(address)
        return address
    def format_photos(self,photos):
        if len(photos) == 0:
            return ''

        if len(photos) >= 10:
            raise Exception('Number of Photos is higher than 10 which is not accepted by dayone-cli', photos)

        for i in range(len(photos)):
            photos[i] = self.format_system_address(photos[i])

        return '-p '+' '.join(photos)

    def push(self,entry):
        if type(entry) != Entry:
            raise Exception('This wrapper can only push Entry objects')

        date = self.format_date(entry.date)
        tags = self.format_tags(entry.tags)
        photos = self.format_photos(entry.photos)

        journal = self.get_journal(entry.journal)
        file_name = self.create_unique_file()
        with open(file_name,'w') as file:
            file.write(entry.text)

        command = 'cat '+file_name+' | dayone2 new '+' '.join([journal,tags,date,photos])
        print(command)
        os.system(command)
        self.delete_file(file_name)
        return command

# a = DayOne()
# note = Entry()
# note.date = datetime.now()
# a.push(note)
