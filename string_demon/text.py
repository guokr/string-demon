#!/usr/bin/env python
# encoding: utf-8

import regex as re

# Chinese repeation
def repeat_content(text):
    que = list(text)
    if float(len(set(que)))/len(que) < 0.35:
        return True
    return False

# Chinese & English break
def break_check(text):
    text = text.decode('utf-8')
    en_regex = re.compile(ur'[\u4e00-\u9fa5]')

    m = en_regex.search(text, 0)
    print m.group()
    res = re.findall(en_regex, text)
    print res

    fined_text = ''.join(e for e in text if e.isalnum())
    print fined_text

    findPart(u"[\u0000-\u007F]+", usample, "acsii")
    findPart(u"[\u4e00-\u9fa5]+", usample, "unicode chinese")
    findPart(u"[\uac00-\ud7ff]+", usample, "unicode korean")
    findPart(u"[\u30a0-\u30ff]+", usample, "unicode japanese katakana")
    findPart(u"[\u3040-\u309f]+", usample, "unicode japanese hiragana")
    findPart(u"[\u3000-\u303f\ufb00-\ufffd]+", usample, "unicode cjk Punctuation")




    if float(len(fined_text))/len(text) > 0.95:
        return True
    return False

def findPart(regex, text, name):
    res=re.findall(regex, text)
    if res:
        print "There are %d %s parts:\n"% (len(res), name)
        for r in res:
            print "\t",r
        print

#sample is utf8 by default.
sample='''en: Regular expression is a powerful tool for manipulating text.正则表达式是一种很有用的处理文本的工具。有时候不管设呢事情。，好的。正規表現は非常に役に立つツールテキストを操作することです。あアいイうウえエおオ정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다。？！、，；：“ ”‘ ’——……·－·《》〈〉！￥％＆＊＃'''
#find the non-ascii chars:

usample=unicode(sample,'utf8')

#get each language parts:
def spam_check(string_content):
    print repeat_content(string_content)
    print break_check(string_content)


def blacklist_check(string_content):
    pass
