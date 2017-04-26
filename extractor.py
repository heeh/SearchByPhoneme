# -*- coding: utf-8 -*-
#Author: Hee Hwang(heehcs@gmail.com)
'''
 입력   : 파일 f
 출력   : 파일 g
 설명   : 1. wrongwords.txt에 포함된 음절과 단어를 추출합니다.
          2. extractor.py에 명시된 음소를 포함하는 라인을 추출합니다.
'''

#Constants

ONSET_START_LETTER = 4352
NUCLEUS_START_LETTER = 4449
CODA_START_LETTER = 4520

JAMO_START_LETTER = 44032
JAMO_END_LETTER = 55203
JAMO_CYCLE = 588

import codecs

# 함수모음
def isHangul(ch): #주어진 문자가 한글인지 아닌지 리턴해주는 함수
    JAMO_START_LETTER = 44032
    JAMO_END_LETTER = 55203
    return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER

def getOnset(ch): # 문자코드에서 초성을 추출하는 함수
    return unichr(((ord(ch) - JAMO_START_LETTER) / 28) / 21 + ONSET_START_LETTER)

def getNucleus(ch): #문자코드에서 중성을 추출하는 함수
    return unichr(((ord(ch) - JAMO_START_LETTER) / 28) % 21 + NUCLEUS_START_LETTER)

def getCoda(ch): # 문자코드에서 종성을 추출하는 함수
    return unichr((ord(ch) - JAMO_START_LETTER) % 28 + CODA_START_LETTER -1)

# 파일로부터 잘못될 가능성이 높은 음절 혹은 단어를 가져옵니다.
wrongwords = codecs.open("wrongwords.txt", "r", "utf-8")
wronglines = wrongwords.readlines()


f = codecs.open("foo.txt", "r", "utf-8") # 입력파일


g = codecs.open("foo.txt.fix",'w',"utf-8") # 출력파일

#f = codecs.open("../hunspell/150112_general.3.txt.uniq.hunspell", "r", "utf-8")
#g = codecs.open("../extr/150112_general.3.txt.uniq.hunspell.extr",'w',"utf-8")

print "Name of the file: ", f.name
lines = f.readlines()

# 음소검색

# 종성으로 'ㅅ'을 지니는 모든 단어 추출. 초성 혹은 중성도 가능.
aa1 = unichr(ord(getCoda(u"햇")))

# 1개이상의 음소를 사용하는 예시
bb1 = unichr(ord(getOnset(u"찌")))
bb2 = unichr(ord(getNucleus(u"찌")))
bb3 = unichr(ord(getCoda(u"찌")))

for line in lines:
    # wrongwords.txt에 포함된 "음절 혹은 단어" 검색
    for wrongline in wronglines:
        if wrongline in line:
            g.write(line)
            break;
    
    # 음소검색: i는 인덱스로 사용가능. c는 다음 음절
    for i, c in enumerate(line):
        #    for ch in line:
        if isHangul(c):
            curOnset = getOnset(c)
            curNucleus = getNucleus(c)
            curCoda = getCoda(c)
            #ㅅ
            if curCoda == aa1:
                g.write(line)
                break
            #찌
            elif curOnset == bb1 and curNucleus == bb2:
                g.write(line)
                break
