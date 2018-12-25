import logging
import os
import sys
import time
import uuid
from datetime import datetime

from .entry import Entry


def _single_escape(text):
    for i in ['|', '`', '(', ')']:
        text = text.split(i)
        joiner = '\\'+i
        text = joiner.join(text)
    return text


def _escape(text):

    if type(text) == list:
        temp = []
        for i in text:
            temp.append(_single_escape(i))
        return temp
    return _single_escape(text)


def _get_journal(journal):
    if not journal:
        return ''
    return '-j ' + journal


def _format_tags(tags):
    if len(tags) == 0:
        return ''
    for i in range(len(tags)):
        tags[i] = str(tags[i])
        tags[i] = '\ '.join(tags[i].split(' '))
    tags = _escape(tags)
    return '--tags ' + ' '.join(tags)


def _format_date(date):
    if type(date) is not datetime:
        raise Exception('date is of type: ' + type(date) +
                        '.Change date attribute of Entry to a datetime object.')

    return '--date \'' + date.strftime('%Y-%m-%d %H:%M:%S')+'\''


def _create_unique_file():
    return uuid.uuid4().hex


def _delete_file(name):
    os.remove(name)


def _format_system_address(address):
    return '\ '.join(address.split(' '))


def _format_photos(photos):
    if len(photos) == 0:
        return ''

    if len(photos) >= 10:
        raise Exception(
            'Number of Photos is higher than 10 which is not accepted by dayone-cli use dayonewriter.helper.list_subset to subset to size of 10 before insertion', photos)

    for i in range(len(photos)):
        photos[i] = _format_system_address(photos[i])

    return '-p '+' '.join(photos)


def _create_markdown_link(title, uuid):
    return f'[{title}](dayone2://view?entryId={uuid})'


def dayonewriter(entry: Entry):
    if entry.date == None:
        raise Exception('entry.date needs a datetime object. If you want it to be current date use datetime.now()')

    date = _format_date(entry.date)
    tags = _format_tags(entry.tags)
    photos = _format_photos(entry.photos)

    journal = _get_journal(entry.journal)
    file_name = _create_unique_file()
    with open(file_name, 'w') as file:
        file.write(entry.text)

    command = 'cat '+file_name+' | dayone2 new ' + \
        ' '.join([journal, tags, date, photos])
    output = os.popen(command).read()
    _delete_file(file_name)
    return output.split(' ')[-1].strip()
