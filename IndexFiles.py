#!/usr/bin/env python

import sys, os, lucene, threading, time, re
from datetime import datetime
from lucene import WhitespaceAnalyzer
import jieba

class Ticker(object):

    def __init__(self):
        self.tick = True

    def run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)

class IndexFiles_0(object):
    def __init__(self, root, storeDir, analyzer):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)
        store = lucene.SimpleFSDirectory(lucene.File(storeDir))
        writer = lucene.IndexWriter(store, analyzer, True,
                                    lucene.IndexWriter.MaxFieldLength.LIMITED)
        writer.setMaxFieldLength(1048576)
        self.indexDocs(root, writer)
        ticker = Ticker()
        print 'optimizing index',
        threading.Thread(target=ticker.run).start()
        writer.optimize()
        writer.close()
        ticker.tick = False
        print 'done'
    def getTxtAttribute(self, contents, attr):
        m = re.search(attr + ': (.*?)\n',contents)
        if m:
            return m.group(1)
        else:
            return ''
    def indexDocs(self, root, writer):
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                try:
                    number=filename.split('.')[0]
                    path = os.path.join(root, filename)
                    print path
                    file = open(path)
                    d=file.readlines()
                    name=d[1].split(' ')[-1]
                    singer=d[0].split(' ')[-1]
                    imgurl=d[2].split(' ')[1]
                    downloadurl=d[5].split(' ')[1]
                    album=d[3].split(' ')[-1]
                    albumurl=d[4].split(' ')[1]
                    content = d[6:]
                    content0=' '.join(content)
                    lyric=''.join(jieba.cut(content0))
                    file.close()
                    doc = lucene.Document()
                    doc.add(lucene.Field("number", number,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("lyric_for_search", lyric,
                                         lucene.Field.Store.NO,
                                         lucene.Field.Index.ANALYZED))
                    doc.add(lucene.Field("lyric", content0,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("downloadurl", downloadurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("singer", singer,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("imgurl", imgurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("name", name,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("album", album,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("albumurl", albumurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    writer.addDocument(doc)
                except Exception, e:
                    print "Failed in indexDocs:", e

class IndexFiles_1(object):
    def __init__(self, root, storeDir, analyzer):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)
        store = lucene.SimpleFSDirectory(lucene.File(storeDir))
        writer = lucene.IndexWriter(store, analyzer, True,
                                    lucene.IndexWriter.MaxFieldLength.LIMITED)
        writer.setMaxFieldLength(1048576)
        self.indexDocs(root, writer)
        ticker = Ticker()
        print 'optimizing index',
        threading.Thread(target=ticker.run).start()
        writer.optimize()
        writer.close()
        ticker.tick = False
        print 'done'
    def getTxtAttribute(self, contents, attr):
        m = re.search(attr + ': (.*?)\n',contents)
        if m:
            return m.group(1)
        else:
            return ''
    def indexDocs(self, root, writer):
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                try:
                    number=filename.split('.')[0]
                    path = os.path.join(root, filename)
                    print path
                    file = open(path)
                    d=file.readlines()
                    name=d[1].split(' ')[-1]
                    singer=d[0].split(' ')[-1]
                    imgurl=d[2].split(' ')[1]
                    downloadurl=d[5].split(' ')[1]
                    album=d[3].split(' ')[-1]
                    albumurl=d[4].split(' ')[1]
                    content = d[6:]
                    content0=' '.join(content)
                    lyric=' '.join(jieba.cut(content0))
                    file.close()
                    doc = lucene.Document()
                    doc.add(lucene.Field("number", number,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("lyric_for_search", lyric,
                                         lucene.Field.Store.NO,
                                         lucene.Field.Index.ANALYZED))
                    doc.add(lucene.Field("lyric", content0,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("downloadurl", downloadurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("singer", singer,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("imgurl", imgurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("name", name,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("album", album,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("albumurl", albumurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    writer.addDocument(doc)
                except Exception, e:
                    print "Failed in indexDocs:", e
        

class IndexFiles_2(object):
    def __init__(self, root, storeDir, analyzer):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)
        store = lucene.SimpleFSDirectory(lucene.File(storeDir))
        writer = lucene.IndexWriter(store, analyzer, True,
                                    lucene.IndexWriter.MaxFieldLength.LIMITED)
        writer.setMaxFieldLength(1048576)
        self.indexDocs(root, writer)
        ticker = Ticker()
        print 'optimizing index',
        threading.Thread(target=ticker.run).start()
        writer.optimize()
        writer.close()
        ticker.tick = False
        print 'done'
    def getTxtAttribute(self, contents, attr):
        m = re.search(attr + ': (.*?)\n',contents)
        if m:
            return m.group(1)
        else:
            return ''
    def indexDocs(self, root, writer):
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                try:
                    number=filename.split('.')[0]
                    path = os.path.join(root, filename)
                    print path
                    file = open(path)
                    d=file.readlines()
                    name=d[1].split(' ')[-1]
                    singer=d[0].split(' ')[-1]
                    imgurl=d[2].split(' ')[1]
                    downloadurl=d[5].split(' ')[1]
                    album=d[3].split(' ')[-1]
                    albumurl=d[4].split(' ')[1]
                    content = d[6:]
                    content0=' '.join(content)
                    lyric=' '.join(jieba.cut_for_search(content0))
                    file.close()
                    
                    doc = lucene.Document()

                    doc.add(lucene.Field("number", number,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("lyric_for_search", lyric,
                                         lucene.Field.Store.NO,
                                         lucene.Field.Index.ANALYZED))
                    doc.add(lucene.Field("lyric", content0,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("downloadurl", downloadurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("singer", singer,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("imgurl", imgurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("name", name,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("album", album,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    doc.add(lucene.Field("albumurl", albumurl,
                                         lucene.Field.Store.YES,
                                         lucene.Field.Index.NOT_ANALYZED))
                    writer.addDocument(doc)
                except Exception, e:
                    print "Failed in indexDocs:", e

if __name__ == '__main__':
    lucene.initVM()
    print 'lucene', lucene.VERSION
    start = datetime.now()
    try :
        IndexFiles_0('lyric', "index_0", lucene.StandardAnalyzer(lucene.Version.LUCENE_CURRENT))
        IndexFiles_1('lyric', "index_1", lucene.WhitespaceAnalyzer(lucene.Version.LUCENE_CURRENT))
        IndexFiles_2('lyric', "index_2", lucene.WhitespaceAnalyzer(lucene.Version.LUCENE_CURRENT))
        end = datetime.now()
        print end - start
    except Exception, e:
        print "Failed: ", e
