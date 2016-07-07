'''
Created on 07-Jul-2016

@author: maya
'''
import wikipedia
import io
import codecs
import urllib
import html2text

from re import sub

def createCorpusForOpinionHolders (filename, output):
    with io.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            print('Fetching wikipedia page for: ', line)
            try:
                page = wikipedia.page(line)
            except Exception:
                print ('Could not find an article for: ', line)
                continue
            line = sub('_', ' ', line)
            outputFile = output+'/'+sub(' ', '_', line)
            w = io.open(outputFile, 'w', encoding='utf-8')
            w.write(page.content)
            w.close()
            f.close()

def createCorpusForTopics (filename, output):
    with io.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            topic,url = line.split(',')
            topic = topic.strip();
            url = url.strip();
            print ("Topic: ", topic,", URL: ", url)
            topic = sub(' ','_', topic)
            content = urllib.URLopener()
            content.retrieve(url, output+'/temp')
            with codecs.open(output+'/temp', 'r', encoding='utf-8', errors='ignore') as tempFile:
                text = html2text.html2text(tempFile.read())
                with io.open(output+'/'+topic, 'w', encoding='utf-8') as w:
                    w.write(text)

if __name__ == '__main__':
    
    pass