#!/usr/bin/env python
# -*- coding: cp936 -*-
from lucene import \
    QueryParser, IndexSearcher, WhitespaceAnalyzer, StandardAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version, BooleanQuery, BooleanClause
import lucene
import jieba

#解析传入的用户输入命令，解析为四种搜索方式所需的Query
#flag：
#0：单字或                      1：jieba.cut()
#2: jieba.cut_for_search()     3: 单字与
def parseCommand(command, flag):
    command = "".join(command.split())
    command0 = " OR ".join(command.split())
    command1 = " AND ".join(jieba.cut(command))
    command2 = " AND ".join(jieba.cut_for_search(command))
    command3 = " AND ".join(command.split())
    if flag == 0:
        return command0
    elif flag == 1:
        return command1
    elif flag == 2:
        return command2
    elif flag == 3:
        return command3

#返回两个字典的并
def union(a, b):
    union = dict(a,**b)
    return union

#执行一次搜索函数，输入中的flag确定了搜索方法，返回本次搜索的结果集
def run(searcher, analyzer, command, flag):
    results={}
    query = QueryParser(Version.LUCENE_CURRENT, 'lyric_for_search',
                        analyzer).parse(parseCommand(command,flag))
    scoreDocs = searcher.search(query, 50).scoreDocs
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        number = doc.get("number")
        results[number]={"name":doc.get("name"),"singer":doc.get("singer"),"lyric":doc.get("lyric"),"imgurl":doc.get("imgurl").encode("utf8"),"downloadurl":doc.get("downloadurl").encode("utf8"),"album":doc.get("album"),"albumurl":doc.get("albumurl")}
    return results

#作为模块，最终可供调用的函数，执行四次搜索并综合了所有搜索结果，给出排序
def search(command):
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    if command != '':
        #先执行4次搜索
        STORE_DIR = "index_0"
        directory = SimpleFSDirectory(File(STORE_DIR))
        searcher = IndexSearcher(directory, True)
        analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
        results0 = run(searcher, analyzer, command, 0)
        searcher.close()
        STORE_DIR = "index_1"
        directory = SimpleFSDirectory(File(STORE_DIR))
        searcher = IndexSearcher(directory, True)
        analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
        results1 = run(searcher, analyzer, command, 1)
        searcher.close()
        STORE_DIR = "index_2"
        directory = SimpleFSDirectory(File(STORE_DIR))
        searcher = IndexSearcher(directory, True)
        analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
        results2 = run(searcher, analyzer, command, 2)
        searcher.close()
        STORE_DIR = "index_0"
        directory = SimpleFSDirectory(File(STORE_DIR))
        searcher = IndexSearcher(directory, True)
        analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
        results3 = run(searcher, analyzer, command, 3)
        searcher.close()
        #取其并集
        results=union(union(results0, results1), union(results2, results3))
        results_stats={}
        results_ordered=[]
        #以输入为依据，对结果集计算权，进行排序
        wordstring =' '.join(jieba.cut_for_search(command))
        for i in results.keys():
            results_stats[i]=0
            for word in wordstring:
                if word in results[i]["lyric"]:
                    results_stats[i]+=1
        results_stats_ordered = sorted(results_stats.items(),key=lambda e:e[1],reverse=True)
        for i in results_stats_ordered:
            if len(results_ordered)<10:
                results_ordered.append(results[i[0]])
        return results_ordered
    else:
        return []

#测试用的程序
if __name__ == '__main__':
    lucene.initVM()
    while True:
        command = raw_input("Query:")
        command = unicode(command, 'GBK')
        print search(command)

         
