# -*- coding: utf-8 -*-
import web
from web import form
import BeautifulSoup
import urllib2
import os
import jieba
import threading
import sys
import SearchFiles
import lucene
from lucene import \
    QueryParser, IndexSearcher, SimpleAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version, BooleanQuery, BooleanClause, StandardAnalyzer,\
    WhitespaceAnalyzer
vm_env=initVM()

#分词
def segment(s):
    seg_list=jieba.cut(s)
    return " ".join(seg_list)

#去掉逻辑关系
def parse(command):
    commandlist=[]
    syn=['AND','OR','NOT','']
    for i in command.split(' '):
        if i not in syn:
            commandlist.append(i)
    return commandlist
  
#自定义函数在一段文字中返回所有关键字
def getAll(content,s):
    ans=[]
    try:
      i=content.find(s)
      while i<>-1:
        ans.append(i)
        i=content.find(s,i+1)
    except:
        pass
    return ans

#定义函数把一段话中出现了搜索关键词的部分标记为高光，在template里实现高光
def turnRED(s,command):
    ans=[]
    commandlist=parse(command)
    for c in commandlist:
        ii=getAll(s,c)
        for i in ii:
            ans+=[[i,len(c)]]
    ans.sort(lambda x,y:x[0]-y[0])
    anslist=[]
    j=0;
    for i in ans:
        anslist+=[[s[j:i[0]],0]]
        anslist+=[[s[i[0]:i[0]+i[1]],1]]
        j=i[0]+i[1]
    anslist+=[[s[j:],0]]
    return anslist

urls = (
    '/', 'index',
    '/i','image'
)

render = web.template.render('templates')

login = form.Form(
    form.Textbox('keyword',description=""),
    form.Button("search", type="submit",description="ss "),
)

class index:
    def GET(self):
        f = login()
        return render.index(f)

class image:
    def GET(self):
        f = login()
        command = web.input().keyword
        pages=SearchFiles.search(command)
        command2 = segment(command)
        for i in pages:
            deal = i["lyric"]
            i["lyric"] = turnRED(deal,command2)
        return render.image(f,command,pages)

if __name__ == "__main__":
    lucene.initVM()
    app = web.application(urls, globals())
    app.run()
