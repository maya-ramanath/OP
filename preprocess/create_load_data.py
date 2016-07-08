'''
Created on 08-Jul-2016

@author: maya
'''
from _io import open
from re import sub
import codecs

## Creates the directory structure so that the text files can be used by the 'load_files' method 
#  and subsequently by the CountVectorizer method.
# Takes in: file name of file containing list of opinion triples, corpus of opinion holders and topics
# Outputs: creates directory structure with given parent directory and based on relations


def create_load_data_directory (triplesFileName, rootDir, outputDir):
    with open(triplesFileName, 'r') as tf:
        for line in tf:
            opHolder,opinion,topic = line.split(',')
            opHolder = sub(' ', '_', opHolder.strip())
            opinion = opinion.strip()
            topic = sub(' ', '_', topic.strip())
            
            try:
                ohfname = rootDir+'/opinion_holders/'+opHolder
                tfname = rootDir+'/topics/'+topic
                outfname = outputDir+'/'+opinion+'/'+opHolder+'__'+topic
                with codecs.open(ohfname, 'r',errors='ignore') as ohFile, codecs.open(tfname,'r', errors='ignore') as tFile:
                    content = ''
                    for line1 in ohFile:
                        content = content+line1
                    for line2 in tFile:
                        content = content+line2
                    with codecs.open(outfname, 'w', errors='ignore') as outFile:
                        print ('Writing...'+ opHolder+ ', '+ topic)
                        outFile.write(content)
                        outFile.close()
            except Exception:
                print ("Something wrong with either "+ opHolder+ ' or '+ 
                       topic + '...skipping...')
    pass

if __name__ == '__main__':
    create_load_data_directory('/Users/maya/git/OP/Data/opinion_triples.csv', 
                               '/Users/maya/git/OP/Data/Corpus', 
                               '/Users/maya/git/OP/Data/Load')
    pass