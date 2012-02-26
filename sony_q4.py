#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import seed, randint
from My_Melody import Melody, Note, Rest, Piece_of_Melody



def main():

    # 楽譜データ
    melody_a = '-3:4:,-2:4:,-1:4:,0:4:b,-1:4:,-2:4:,-3:4:,:4:,\
-1:4:,0:4:b,1:4:,2:4:,1:4:,0:4:b,-1:4:,:4:'

    melody_b = '3:4:,2:4:,1:4:,0:4:b,1:4:,2:4:,3:4:,:4:,1:4:,\
0:4:b,-1:4:,-2:4:,-1:4:,0:4:b,1:4:,:4:'

    melody_c = '3:4:,2:4:,1:4:,0:4:,1:4:,2:4:,3:4:,:4:,1:8:,\
0:4.:,-1:4:,-2:4:,:8:,-1:4.:,0:8:,1:8:,:4:'

    melody_d = '\
-6:8:,-6:8:,-6:8:,-4:8:,-2:8:,-2:8:,-2:8:,:8:,\
-5:8:,-5:8:,-5:8:,-3:8:,-2:8:,-2:8:,-2:8:,:8:,:8:,\
-2:8:,-2:8:,-1:8:b,-1:8:,-1:8:,-1:8:,-1:8:b,-2:4:,0:4:,1:4:,:4:'

    melody_e = '\
-6:8.:,-7:16:,-6:8:,-5:8:,-4:8:,-4:8:,-4:4:,-3:8.:,\
-4:16:,-5:8:,-6:8:,-5:4:,:4:,-3:8:,-5:4:,-5:8:,-4:8:,\
-4:8:,-3:8:,-3:8:,-4:8:,-4:8:,-5:8:,-5:8:,-6:4:,:4:'

    melody_f = '\
-6:2:,-5:4:,-6:8:,-5:8:,-4:4:,-2:4:,-4:4:,:4:,-5:4:,\
-5:4:,-6:4:,-5:4:,-4:2.:,:4:'

    melody_g = '\
-2:8.:,-1:16:,-2:8.:,-1:16:,-2:4:,-4:4:,-4:8.:,-3:16:,\
-4:8.:,-3:16:,-4:4:,-6:4:,-4:8:,:8:,-6:8.:,-5:16:,-4:8:,:8:,\
-6:8.:,-5:16:,-4:8.:,-4:16:,-2:8.:,-2:16:,-5:8.:,-4:16:,-5:4:'



    # 問題の解答
    print "i) A == C, A != B"
    print "A : ", Melody.fromstring(melody_a).get_feature()
    b = Melody.fromstring(melody_b).get_feature()
    print "B : ", b
    print "C : ", Melody.fromstring(melody_c).get_feature()

    print "\nii) B == ?"
    d = Melody.fromstring(melody_d).get_feature()
    e = Melody.fromstring(melody_e).get_feature()
    f = Melody.fromstring(melody_f).get_feature()
    print "D : ", d
    print "E : ", e
    print "F : ", f
    for i, k in zip([d, e, f], ["D", "E", "F"]):
        if b == i:
            print "Answer is B == " + k
            break

    print "\niii) Create melody"
    g = Melody.fromstring(melody_g).get_feature()
    print "G : ", g
    print

    seed(12345)
    x = Melody().predict(g , 4.0, Note(-3), Note(-3))

    print "<Original melody >"
    print "feature :", x.get_feature()
    print "length :", x.get_span()
    print "score :", x


if __name__ == '__main__':
    main()
