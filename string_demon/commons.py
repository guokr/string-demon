#!/usr/bin/env python
# -*- coding:utf-8 -*-


def suffix_array(text):
    suffix = []
    for i in xrange(len(text)):
        suffix.append(text[i:])
    suffix.sort()
    return suffix


def longest_common_prefix(suffix, text):
    lcp = []
    previous = ""
    for i in xrange(len(text)):
        count = 0
        current = suffix[i]
        max_count = min(len(current), len(previous))
        count = 0
        for j in xrange(max_count):
            if current[j] != previous[j]:
                break
            count += 1

        lcp.append(count)
        previous = current
    return lcp


def leftmost(A, W):
    length = len(W)
    if W <= A[0][0:length]:
        return 0
    elif W > A[-1]:
        return len(A) - 1
    else:
        L = 0
        R = len(A) - 1
        while R - L > 1:
            M = (L + R) // 2
            if W <= A[M][0:length]:
                R = M
            else:
                L = M
        return R


def rightmost(A, W):
    length = len(W)
    if W >= A[-1][0:length]:
        return len(A) - 1
    elif W < A[0]:
        return 0
    else:
        L = 0
        R = len(A) - 1
        while R - L > 1:
            M = (L + R) // 2
            if W >= A[M][0:length]:
                L = M
            else:
                R = M
        return L


def max_value_and_index(L):
    max_value = L[0]
    max_index = 0
    i = 0
    for x in L:
        if x > max_value:
            max_value = x
            max_index = i
        i += 1
    return (max_value, max_index)


def suffix_count_of_word(suffix, W):
    if (not W):
        return 0
    return (rightmost(suffix, W) - leftmost(suffix, W)) + 1


def suffix_counts(suffix, lcp):
    count = [0] * len(suffix)
    for i in xrange(len(suffix)):
        count[i] = suffix_count_of_word(suffix, suffix[i][0:lcp[i]])
    return count


def left_maximal(text, suffix, W1):
    c1 = suffix_count_of_word(suffix, W1)
    W2 = text[:-len(W1)]
    c2 = suffix_count_of_word(suffix, W2)
    print " c2 = (%d, '%s') and c1 = (%d, '%s')  " % (c2, W2, c1, W1)
    return c2 < c1


def q(s):
    return "'%s'" % s


def wcount(text):
    "returns the number of words"
    import re
    text = re.sub('[^\w&^\d]', ' ', text)
    return len(text.split())


def print_maximal_phrases(suffix, lcp, count, text):
    prev = ""
    print '%s\t%s\t%s' % ("count", "numberwords", "phrase")
    for i in xrange(len(suffix)):
        w = suffix[i][:lcp[i]]
        if w.strip() == prev.strip():
            continue
        if w[:1].isalnum() or w[-1:].isalnum():
            continue

        s = suffix[i]
        left_suffix = text[-(len(s) + 1):]
        j = leftmost(suffix, left_suffix)
        left_suffix = left_suffix[:lcp[j]]
        if count[j] != 0 and lcp[j] <= lcp[i]:
            print '%d\t%d\t%s' % (count[i], wcount(w), q(w))
            prev = w
