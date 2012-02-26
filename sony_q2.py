#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys,getopt
from My_Factorial import Factorial

def usage():
    print "usage: python sony_q2.py [-t: test_modo]"
    sys.exit(0)


def main():
    # Get parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t", "h")
    except:
        usage()
        sys.exit(0)

    # Test_mode flag
    t_flag = 0

    for o, a in opts:
        if o == "-t": t_flag = 1
        if o == "-h": usage()

    # 通常動作
    # GO FOR IT の解答
    if t_flag == 0:
        print "Sample_Data:"
        print "5! =", Factorial().kaijo(5)
        print "2.5! =", Factorial().kaijo(2.5)
        print "(-1.9)!=", Factorial().kaijo(-1.9)

        print "\ni) (0<=a<=10)"
        for i in range(11):
            print str(i) + "! =", Factorial().kaijo(i)

        print "\nii) (0<=a<=10)"
        i = 0.0
        while i <= 10.0:
            print str(i) + "! =", Factorial().kaijo(i)
            i += 0.1

        print "\niii) (-1.9<=a<=-1.1)"
        i = -1.9
        while i <= -1.0:
            print "(" + str(i) + ")! =", Factorial().kaijo(i)
            i += 0.1

    # Test_mode
    # ガンマ関数の導出法の選択と正の整数専用の階乗計算を使用するかの選択が可能
    # 任意の値に対して、階乗の計算を行う
    else:
        print ":::Test_mode:::"
        while True:
            print "Select Gamma_function(0:Bernoulli(default), 1:Nemes, 2:Euler): "
            s = raw_input()
            if s == "" :
                select = 0
            elif s not in ["0", "1", "2"]:
                continue
            select = int(s)
            break

        while True:
            print "Do you use the int_factorial function? y/n"
            ans = raw_input()
            if ans == "y":
                switch = 0
            elif ans == "n":
                switch = 1
            else:
                continue
            break

        while True:
            print "\n( x )! , Please input x (end: Exit the program):"
            x = raw_input()
            if x == "end":
                break
            #elif x.isdigit() == False:
                #continue
            try:
                k = float(x)
            except ValueError:
                continue
            try:
                f = Factorial().kaijo(k, select, switch)
            except ValueError, (m):
                print "Error! " + str(m)
                continue
            print "(" + str(k) + ")! =", f



if __name__ == '__main__':
    main()