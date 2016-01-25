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
    text = unicode(text,'utf8')
    #  en_regex = re.compile(ur'[\u4e00-\u9fa5]')

    #  m = en_regex.search(text, 0)
    #  print m.group()
    #  res = re.findall(en_regex, text)
    #  print res

    #  fined_text = ''.join(e for e in text if e.isalnum())
    #  print fined_text

    print findPart(u"[\u0001-\u007F]+", text, "en") # "acsii"
    print findPart(u"[\u4e00-\u9fa5]+", text, "cn") # "unicode chinese"
    #  print findPart(u"[\uac00-\ud7ff]+", text) # "unicode korean"
    #  print findPart(u"[\u30a0-\u30ff]+", text) # "unicode japanese katakana"
    #  findPart(u"[\u3040-\u309f]+", usample) # "unicode japanese hiragana"
    print findPart(u"[\u3000-\u303f\ufb00-\ufffd]+", text, "punc") # "unicode cjk Punctuation"

    if float(len(text))/len(text) > 0.95:
        return True
    return False

def findPart(regex, text, dec_type):
    res=re.findall(regex, text)
    if dec_type == "en":
        text_length_all = 0
        break_times = 0
        for i in res:
            text_length_all += len(i)
            for j in i:
                if j == ' ':
                    break_times += 1
        return text_length_all, break_times

    elif dec_type == "cn":
        text_length_all = 0
        for i in res:
            text_length_all += len(i)
        return text_length_all

    elif dec_type == "punc":
        punc_length_all = 0
        for i in res:
            punc_length_all += len(i)
        return punc_length_all

    #  return len(res)

#sample is utf8 by default.
sample='''en: Regular expression is a powerful tool for manipulating text'''#.正则表达式是一种很有用的处理文本的工具。有时候不管设呢事情。，好的。正規表現は非常に役に立つツールテキストを操作することです。あアいイうウえエおオ정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다。？！、，；：“ ”‘ ’——……·－·《》〈〉！￥％＆＊＃'''
#find the non-ascii chars:

usample=unicode(sample,'utf8')

#get each language parts:
def spam_check(string_content):
    print repeat_content(string_content)
    print break_check(string_content)


def blacklist_check(string_content):
    pass
