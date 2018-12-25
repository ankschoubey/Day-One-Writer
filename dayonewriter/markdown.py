def bold(word: str):
    word = word.strip()
    return '**' + word + '**'

def bullet(sentence:str):
    return '- '+ sentence

def bullet_list(sentences: list):
    sentences = [str(i) for i in sentences]
    return '\n- '.join(sentences)

def number_list(sentences: list):
    sentences = [ f'{count+1}. {str(i)}' for count,i in enumerate(sentences)]
    return '\n- '.join(sentences)

def italic(text: str):
    text = text.strip()
    return '*' + text + '*'

def dayone_link(text:str, entry_id:str):
    if len(entry_id)!=32:
        raise Exception(f'{entry_id} is not a valid entry id. It should be of length 32')
    return f'[{text}](dayone2://view?entryId={entry_id})'

def photo(message:str=''):
    return f'[{{photo}}]\n {message}'

def header(text: str, value:int = 1):
    return f'{"#"*value} {text}'

def checklist(text: str, checked: bool=False):
    return f'- [{"x" if checked == True else " "}] {text}'

def online_image(image_link: str, alternate_text: str=''):
    return f'![{alternate_text}]({image_link})'

def online_link(text:str, hyperlink:str):
    return '['+str(text)+']('+str(hyperlink)+')'

def quote(quote:str):
    return f'> {quote}'