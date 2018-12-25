import sys
import logging
import os
import time
from datetime import datetime
import uuid

class Entry:
    text: str = ''
    tags: list = []
    date: datetime = None
    photos: list = []
    journal: str = None
    starred: bool = False
    coordinate: list = []
    timezone: list = None


class DayOne:
    """
    use DayOne() object's .push(entry) method send something to dayone
    """

    def __init__(self,default_journal: str = None):
        self.default_journal = default_journal

    @staticmethod
    def _single_escape(text):
        for i in ['|','`','(',')']:
            text = text.split(i)
            joiner = '\\'+i
            text = joiner.join(text)
        return text

    @staticmethod
    def escape(text):

        if type(text) == list:
            temp = []
            for i in text:
                temp.append(DayOne._single_escape(i))
            return temp
        return DayOne._single_escape(text)

    def get_journal(self, journal):
        if not journal and not self.default_journal:
            return ''
        if journal:
            return '-j ' + journal
        return '-j ' + self.default_journal

    @staticmethod
    def format_tags(tags):

        if len(tags) == 0:
            return ''
        for i in range(len(tags)):
            tags[i] = str(tags[i])
            tags[i] = '\ '.join(tags[i].split(' '))
        tags = DayOne.escape(tags)
        return '--tags '+ ' '.join(tags)

    @staticmethod
    def format_date(date):
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

    @staticmethod
    def format_system_address(address):
        address = address.split(' ')
        address = '\ '.join(address)
        return address
    
    @staticmethod
    def format_photos(photos):
        if len(photos) == 0:
            return ''

        if len(photos) >= 10:
            raise Exception('Number of Photos is higher than 10 which is not accepted by dayone-cli', photos)

        for i in range(len(photos)):
            photos[i] = DayOne.format_system_address(photos[i])

        return '-p '+' '.join(photos)

    @staticmethod
    def create_markdown_link(title, uuid):
        return f'[{title}](dayone2://view?entryId={uuid})'

    def push(self,entry: Entry):
        date = DayOne.format_date(entry.date)
        tags = DayOne.format_tags(entry.tags)
        photos = DayOne.format_photos(entry.photos)

        journal = self.get_journal(entry.journal)
        file_name = DayOne.create_unique_file()
        with open(file_name,'w') as file:
            file.write(entry.text)

        command = 'cat '+file_name+' | dayone2 new '+' '.join([journal,tags,date,photos])
        output = os.popen(command).read()
        DayOne.delete_file(file_name)
        return command, output.split(' ')[-1].strip()

a = DayOne()
note = Entry()
note.date = datetime.now()
command, output = a.push(note)
uuid = output.split(' ')[-1].strip()
print(command, uuid, sep='\n')
print(a.create_markdown_link("hello",uuid))