# dayonewriter
Python wrapper which internally uses [dayone-cli](http://help.dayoneapp.com/day-one-2-0/command-line-interface-cli). Compatible with [Day One 2+](http://dayoneapp.com/)+.

Make sure that it is installed [dayone-cli](http://help.dayoneapp.com/day-one-2-0/command-line-interface-cli) is installed.

Day One 3 features like audio are not supported.

## Installation

```pip install dayonewriter```

## Usage

### Creating an Entry with text, photo and tag

```
from dayonewriter import Entry, dayonewriter, markdown, helper
from datetime import datetime

entry = Entry()
# Providing datetime is compulsary
entry.date = datetime.now() 

#optionals
entry.text = 'Hello' 
entry.tags = ['Tag 1','Tag2']
entry.photos = ['Photo1','Photo2'] # needs to be maximum 10. If more then checkout helper.list_subset
entry.journal = 'Journal Name'

entry_id = dayonewriter(entry) #sends to dayone using cli
```

### ```Entry``` class
each new entry and has these attributes by default:
```
class Entry:
    text: str = ''
    tags: list = []
    date: datetime = None
    photos: list = []
    journal: str = None
    starred: bool = False
    
    # below attributes are not tested 
    coordinate: list = []
    timezone: list = None
```

#### Note:
- ```date``` attribute in ```None``` by default and needs a [datetime](https://docs.python.org/3/library/datetime.html) object.
- you can use [{photo}] in entry text to position photo.

### helper

Helper contains only 1 method **list_subset** to create groups of 10 from list. 

Helpful when photos are more than 10.

```
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13] # works with any data type
print('Without subset ', numbers)
print('With subset' ,helper.list_subset(numbers))
```

### markdown

contains methods which make writing markdown text easier:
- bold
- bullet
- bullet_list
- number_list
- italic
- dayone_link
- photo
- header
- checklist
- online_image
- online_link
- quote

#### Links:
- [Day One App](http://dayoneapp.com/)
- [Day One 2 CLI](http://help.dayoneapp.com/day-one-2-0/command-line-interface-cli)
