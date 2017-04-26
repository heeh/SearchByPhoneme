#Author: Hee Hwang(heehcs@gmail.com)
# -*- coding: utf-8 -*-
#Constants

CHOSUNG_START_LETTER = 4352
JUNGSUNG_START_LETTER = 4449
JONGSUNG_START_LETTER = 4520

JAMO_START_LETTER = 44032
JAMO_END_LETTER = 55203
JAMO_CYCLE = 588

import codecs


def isHangul(ch): #주어진 문자가 한글인지 아닌지 리턴해주는 함수
    JAMO_START_LETTER = 44032
    JAMO_END_LETTER = 55203
    return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER

def getOnset(ch): # 문자코드에서 초성을 추출하는 함수
    return unichr(((ord(ch) - JAMO_START_LETTER) / 28) / 21 + CHOSUNG_START_LETTER)

def getNucleus(ch): #문자코드에서 중성을 추출하는 함수
    return unichr(((ord(ch) - JAMO_START_LETTER) / 28) % 21 + JUNGSUNG_START_LETTER)

def getCoda(ch): # 문자코드에서 종성을 추출하는 함수
    return unichr((ord(ch) - JAMO_START_LETTER) % 28 + 4519)



wrongwords = codecs.open("wrongwords.txt", "r", "utf-8")
wronglines = wrongwords.readlines()

f = codecs.open("../hunspell/150112_general.18.txt.uniq.hunspell", "r", "utf-8")
g = codecs.open("../extr/150112_general.18.txt.uniq.hunspell.extr",'w',"utf-8")
print "Name of the file: ", f.name

lines = f.readlines()

#ㅅ
aa1 = unichr(ord(getCoda(u"햇")))

#찌
bb1 = unichr(ord(getOnset(u"찌")))
bb2 = unichr(ord(getNucleus(u"찌")))
bb3 = unichr(ord(getCoda(u"찌")))

##조
cc1 = unichr(ord(getOnset(u"조")))
cc2 = unichr(ord(getNucleus(u"조")))
cc3 = unichr(ord(getCoda(u"조")))


##업
a1 = unichr(ord(getOnset(u"업")))
a2 = unichr(ord(getNucleus(u"업")))
a3 = unichr(ord(getCoda(u"업")))
##예
b1 = unichr(ord(getOnset(u"예")))
b2 = unichr(ord(getNucleus(u"예")))
b3 = unichr(ord(getCoda(u"예")))

##써
c1 = unichr(ord(getOnset(u"써")))
c2 = unichr(ord(getNucleus(u"써")))
c3 = unichr(ord(getCoda(u"써")))

##께
d1 = unichr(ord(getOnset(u"께")))
d2 = unichr(ord(getNucleus(u"께")))
d3 = unichr(ord(getCoda(u"께")))

##꺼
e1 = unichr(ord(getOnset(u"꺼")))
e2 = unichr(ord(getNucleus(u"꺼")))
e3 = unichr(ord(getCoda(u"꺼")))

##읍
f1 = unichr(ord(getOnset(u"읍")))
f2 = unichr(ord(getNucleus(u"읍")))
f3 = unichr(ord(getCoda(u"읍"))) 
##깍
g1 = unichr(ord(getOnset(u"깍")))
g2 = unichr(ord(getNucleus(u"깍")))
g3 = unichr(ord(getCoda(u"깍")))
##슴
h1 = unichr(ord(getOnset(u"슴")))
h2 = unichr(ord(getNucleus(u"슴")))
h3 = unichr(ord(getCoda(u"슴")))
##굼
i1 = unichr(ord(getOnset(u"굼")))
i2 = unichr(ord(getNucleus(u"굼")))
i3 = unichr(ord(getCoda(u"굼")))
##따
j1 = unichr(ord(getOnset(u"따")))
j2 = unichr(ord(getNucleus(u"따")))
j3 = unichr(ord(getCoda(u"따")))
##봬
k1 = unichr(ord(getOnset(u"봬")))
k2 = unichr(ord(getNucleus(u"봬")))
k3 = unichr(ord(getCoda(u"봬")))
##튼
l1 = unichr(ord(getOnset(u"튼")))
l2 = unichr(ord(getNucleus(u"튼")))
l3 = unichr(ord(getCoda(u"튼")))
##옛
m1 = unichr(ord(getOnset(u"옛")))
m2 = unichr(ord(getNucleus(u"옛")))
m3 = unichr(ord(getCoda(u"옛")))
##률
n1 = unichr(ord(getOnset(u"률")))
n2 = unichr(ord(getNucleus(u"률")))
n3 = unichr(ord(getCoda(u"률")))
##플
o1 = unichr(ord(getOnset(u"플")))
o2 = unichr(ord(getNucleus(u"플")))
o3 = unichr(ord(getCoda(u"플")))
##깎
p1 = unichr(ord(getOnset(u"깎")))
p2 = unichr(ord(getNucleus(u"깎")))
p3 = unichr(ord(getCoda(u"깎")))
##굼
q1 = unichr(ord(getOnset(u"굼")))
q2 = unichr(ord(getNucleus(u"굼")))
q3 = unichr(ord(getCoda(u"굼")))
##돼
r1 = unichr(ord(getOnset(u"돼")))
r2 = unichr(ord(getNucleus(u"돼")))
r3 = unichr(ord(getCoda(u"돼")))

##쟎
s1 = unichr(ord(getOnset(u"쟎")))
s2 = unichr(ord(getNucleus(u"쟎")))
s3 = unichr(ord(getCoda(u"쟎")))
##괜
t1 = unichr(ord(getOnset(u"괜")))
t2 = unichr(ord(getNucleus(u"괜")))
t3 = unichr(ord(getCoda(u"괜")))
##긔
u1 = unichr(ord(getOnset(u"긔")))
u2 = unichr(ord(getNucleus(u"긔")))
u3 = unichr(ord(getCoda(u"긔")))

##쳐
v1 = unichr(ord(getOnset(u"쳐")))
v2 = unichr(ord(getNucleus(u"쳐")))
v3 = unichr(ord(getCoda(u"쳐")))

##쬬
w1 = unichr(ord(getOnset(u"쬬")))
w2 = unichr(ord(getNucleus(u"쬬")))
w3 = unichr(ord(getCoda(u"쬬")))

##젼
x1 = unichr(ord(getOnset(u"젼")))
x2 = unichr(ord(getNucleus(u"젼")))
x3 = unichr(ord(getCoda(u"젼")))
##읍
y1 = unichr(ord(getOnset(u"읍")))
y2 = unichr(ord(getNucleus(u"읍")))
y3 = unichr(ord(getCoda(u"읍")))




for line in lines:
    # wrongwords.txt에 포함된 "음절"검색
    for wrongline in wronglines:
        if wrongline in line:
            g.write(line)
            break;
    
    # "음소검색"
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
            #조
            # elif i == 0 and curOnset == cc1 and curNucleus == cc2:
            #     g.write(line)
            #     break

            #업
            elif curOnset == a1 and curNucleus == a2 and curCoda == a3:
                g.write(line)
                break
            #예
            elif curOnset == b1 and curNucleus == b2 and curCoda == b3:
                g.write(line)
                break
            #써
            elif curOnset == c1 and curNucleus == c2 and curCoda == c3:
                g.write(line)
                break            
            #께
            elif curOnset == d1 and curNucleus == d2 and curCoda == d3:
                g.write(line)
                break            
            #꺼
            elif curOnset == e1 and curNucleus == e2 and curCoda == e3:
                g.write(line)
                break            
            #읍
            elif curOnset == f1 and curNucleus == f2 and curCoda == f3:
                g.write(line)
                break            
            #깍
            elif curOnset == g1 and curNucleus == g2 and curCoda == g3:
                g.write(line)
                break            
            #슴
            elif curOnset == h1 and curNucleus == h2 and curCoda == h3:
                g.write(line)
                break            
            #굼
            elif curOnset == i1 and curNucleus == i2 and curCoda == i3:
                g.write(line)
                break            
            #따
            elif curOnset == j1 and curNucleus == j2 and curCoda == j3:
                g.write(line)
                break            
            #봬
            elif curOnset == k1 and curNucleus == k2 and curCoda == k3:
                g.write(line)
                break            
            #튼
            elif curOnset == l1 and curNucleus == l2 and curCoda == l3:
                g.write(line)
                break            
            #옛
            elif curOnset == m1 and curNucleus == m2 and curCoda == m3:
                g.write(line)
                break            
            #률
            elif curOnset == n1 and curNucleus == n2 and curCoda == n3:
                g.write(line)
                break            
            #플
            elif curOnset == o1 and curNucleus == o2 and curCoda == o3:
                g.write(line)
                break            
            #깎
            elif curOnset == p1 and curNucleus == p2 and curCoda == p3:
                g.write(line)
                break            
            #굼
            elif curOnset == q1 and curNucleus == q2 and curCoda == q3:
                g.write(line)
                break            
            #돼
            elif curOnset == r1 and curNucleus == r2 and curCoda == r3:
                g.write(line)
                break            
            #쟎
            elif curOnset == s1 and curNucleus == s2 and curCoda == s3:
                g.write(line)
                break            
            #괜
            elif curOnset == t1 and curNucleus == t2 and curCoda == t3:
                g.write(line)
                break            
            #긔
            elif curOnset == u1 and curNucleus == u2 and curCoda == u3:
                g.write(line)
                break            
            #쳐
            elif curOnset == v1 and curNucleus == v2 and curCoda == v3:
                g.write(line)
                break            
            #쬬
            elif curOnset == w1 and curNucleus == w2 and curCoda == w3:
                g.write(line)
                break            
            #젼
            elif curOnset == x1 and curNucleus == x2 and curCoda == x3:
                g.write(line)
                break            
            #읍
            elif curOnset == y1 and curNucleus == y2 and curCoda == y3:
                g.write(line)
                break            

            



