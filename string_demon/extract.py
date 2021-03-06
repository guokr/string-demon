#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import re
import urlparse

# A simple version
email_regex = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', re.IGNORECASE)

# url_regex = re.compile('(https?://\S*)', re.IGNORECASE)
url_regex = re.compile('(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&@#/%=~_|$?!:,.]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)

# Starts with 8 or 9, and 8 digit long
# cn_mobile_phone_regex = re.compile('[1][0-9]{10}')
cn_phone_regex = re.compile('((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)')
cn_400_1_regex= re.compile('\d{4}[-]{0,1}\d{3}[-]{0,1}\d{3}')
cn_400_2_regex= re.compile('\d{3}[-]{0,1}\d{3}[-]{0,1}\d{4}')
# QQ_reg
qq_regex = re.compile(r'[Q]{0,2}\s{0,}[:]{1,}[：]{1,}[0-9]{8,13}', re.IGNORECASE)
wechat_regex = re.compile(r'[a-zA-Z]{1}[-_a-zA-Z0-9]{5,19}', re.IGNORECASE)

# A convenient enum for the type of data that can be extracted


def extract(type, data):
    if (type == "all"):
        list_1, data1 = extract_emails(data)
        list_2, data2 = extract_urls(data1)
        list_3, data3 = extract_phone(data2)
        list_4, data4 = extract_qq(data3)

#        extracted_data_set = set_1 | set_2 | set_3 | set_4 | set_5
        if len(list_1) != 0:
            return True
        if len(list_2) != 0:
            return True
        if len(list_3) != 0:
            return True
        if len(list_4) != 0:
            return True
        else:
            return False

    if (type == "email"):
        return extract_emails(data)

    if (type == "wechat"):
        return extract_wechat(data)

    if (type == "url"):
        return extract_urls(data)

    if (type == "domain"):
        extract_domains(data)

    if (type == "mobile"):
        return extract_cn_mobile(data)

    if (type == "qq"):
        return extract_qq(data)

    if (type == "phone"):
        return extract_phone(data)

def cleanup_for_emails(data):
    data = re.sub('\s*[[(</-]?\s*(?: at |@)\s*[])>/-]?\s*', '@', data)
    data = re.sub('\s*[[(</-]?\s*(?:dot|\.)\s*[])>/-]?\s*', '.', data)
    return data

def extract_wechat(data):
    spam_wechat_list = []
    for qq in wechat_regex.findall(data):
        spam_wechat_list.append(qq)
        data = data.replace(qq, '')
    return [spam_wechat_list, data]


def extract_emails(data):
    spam_emails = []
    data = cleanup_for_emails(data)

    for email in email_regex.findall(data):
        spam_emails.append(email)
        data = data.replace(email, '')

    return spam_emails, data


def extract_phone(data):
    spam_phone_list = []
    for x in cn_phone_regex.findall(data):
        spam_phone_list.append(x)
        data = data.replace(x[0], '')
    for y in cn_400_1_regex.findall(data):
        spam_phone_list.append(y)
        data = data.replace(y[0], '')
    for z in cn_400_2_regex.findall(data):
        spam_phone_list.append(z)
        data = data.replace(z[0], '')
    return [spam_phone_list, data]


def extract_urls(data):
    spam_url_list = []
    for x in url_regex.findall(data):
        spam_url_list.append(x)
        data = data.replace(x, '')
    return [spam_url_list, data]


def extract_domains(data):
    spam_domains_list = []
    urls = extract_urls(data)
    for url in urls:
        try:
            hostname = urlparse.urlparse(url).hostname.split(".")
            hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
            spam_domains_list.append(hostname)
        except:
            pass
    return spam_domains_list


def extract_qq(data):
    spam_qq_list = []
    for qq in qq_regex.findall(data):
        spam_qq_list.append(qq)
        data = data.replace(qq, '')
    return [spam_qq_list, data]


def extract_cn_mobile(data):
    _set = set()
    for phone in cn_mobile_phone_regex.findall(data):
        _set.add(phone)
    return _set
