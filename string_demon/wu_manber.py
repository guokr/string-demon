#!/usr/bin/env python
# -*-coding:utf-8-*-


def DefConstraint(text, index):
    return True


class WuManber(object):
    def __init__(self, ConstraintFunc = DefConstraint):
        self.m_MinLen=0
        self.m_TableSize=0
        self.m_BlockLen=3
        self.m_Pattens=[]
        self.m_ShiftTable=[]
        self.m_HashTable=[]
        self.m_ConstraintFunc=ConstraintFunc

    def Hash(self, string):
        if string is None:
            return -1
        hashValue=int(0)
        for item in string:
            try:
                hashValue=ord(item) + hashValue * (pow(2, 6) + pow(2, 16) - 1)

            except Exception:
                print "[error]WM.Hash,string", string, item
        #hashValue=string.__hash__()
        return hashValue % 0x7FFFFFFF

    def InitPattern(self, ListPattern):
        PattenSize=len(ListPattern)
        self.m_MinLen=len(ListPattern[0])
        for item in ListPattern:
            if len(item)<self.m_MinLen:
                self.m_MinLen=len(item)

        #  print "initPattern: min len of patterns:", self.m_MinLen
        if self.m_BlockLen>self.m_MinLen:
            self.m_BlockLen=self.m_MinLen

        primes=[1003, 10007, 100003, 1000003, 10000019, 100000007]
        threshold=10 * self.m_MinLen

        for item in primes:
            if item>PattenSize and item / PattenSize > threshold:
                self.m_TableSize=item
                break
        if self.m_TableSize is 0:
            self.m_TableSize=primes[-1]

        self.m_Pattens=ListPattern

        for i in range(self.m_TableSize):
            self.m_ShiftTable.append(self.m_MinLen - self.m_BlockLen + 1)
            self.m_HashTable.append([])
        for id in range(PattenSize):
            for index in range(self.m_MinLen, self.m_BlockLen - 1, -1):
                s=ListPattern[id][index - self.m_BlockLen:index]
                h=self.Hash(s) % self.m_TableSize
                if self.m_ShiftTable[h]>self.m_MinLen - index:
                    self.m_ShiftTable[h]=self.m_MinLen - index
                if index==self.m_MinLen:
                    prefixhash=self.Hash(ListPattern[id][:self.m_BlockLen])
                    self.m_HashTable[h].append([prefixhash, id])
        return True

    def Search(self, text):
        result={}
        textLen=len(text)
        wordsIdx = []
        index=self.m_MinLen
        while index <= textLen:
            tmp = text[index - self.m_BlockLen:index]
            if tmp is None:
                print "index-self.m_BlockLen:index", index - self.m_BlockLen, index, text
            h=self.Hash(text[index - self.m_BlockLen:index]) % self.m_TableSize
            if self.m_ShiftTable[h]>0:
                index += self.m_ShiftTable[h]
            else:
                prefixHash=self.Hash(text[index - self.m_MinLen:index - self.m_MinLen + self.m_BlockLen])
                for item in self.m_HashTable[h]:
                    if prefixHash == item[0]:
                        lenP=len(self.m_Pattens[item[1]])
                        cmpindex = index - self.m_MinLen
                        for i in range(lenP):
                            if cmpindex>=textLen or (self.m_Pattens[item[1]][i] is not text[cmpindex]):
                                break
                            else:
                                cmpindex += 1
                        else:
                            if self.m_ConstraintFunc(text, index - self.m_MinLen + len(self.m_Pattens[item[1]])):
                                if self.m_Pattens[item[1]] in result.keys():
                                    result[self.m_Pattens[item[1]]]+=1
                                    wordsIdx.append(cmpindex)
                                else:
                                    result[self.m_Pattens[item[1]]]=1
                                    wordsIdx.append(cmpindex)
                            break

                index += 1
        return result, wordsIdx
