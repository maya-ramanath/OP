##
#
# Triples are given in the following format, one per line: <op holder>\t<support/oppose>\t<topic>
#
##

import wikipedia

#For opinion holders, we directly download content from wikipedia (csv file contains single column)
#For topics, we need the URL from which to download (csv file contains <topic, URL>)


def search():
    suggestions = wikipedia.suggest('privatize social security')
    print(suggestions)
    page = wikipedia.page('privatize social security')
    print (page.content)
    pass

        
if __name__ == '__main__':
    pass