# Day-One-Python-Wrapper
Python wrapper which internally uses [dayone-cli](http://help.dayoneapp.com/day-one-2-0/command-line-interface-cli). Compatible with [Day One 2](http://dayoneapp.com/) only.

## Usage

Creating an Entry with text, photo and tag

```
from dayone2 import Entry, DayOne
from datetime import datetime

note = Entry()
note.text = 'Hello World'
note.photo = ['path to photo.png', 'photo2.png']
note.tag = ['tags are awesome']
note.date = datetime.now() # needs a datetime object

journal = DayOne()
journal.push(note)
```

## Explaination

2 classes

### ```Entry``` class
for each new entry and has these attributes by default:
```
text = ''
tags = [] #list
date = None
photos = [] #list
journal = None
starred = False

## below attributes are not tested well
coordinate = []
timezone = None
```

#### Note:
- ```date``` attribute in ```None``` by default and needs a [datetime](https://docs.python.org/3/library/datetime.html) object.
- you can use [{photo}] in entry text to position photo.

### ```DayOne``` class

Actual Wrapper to Day One Cli

```push``` method:
- Takes ```Entry``` object as argument in push and writes it to Day One App.

Constructor for ```DayOne``` class also has an optional argument to specify ```default_journal``` name

***
#### Links:
- [Day One App](http://dayoneapp.com/)
- [Day One 2 CLI](http://help.dayoneapp.com/day-one-2-0/command-line-interface-cli)
