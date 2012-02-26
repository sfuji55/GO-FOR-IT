#!/usr/bin/python
# -*- coding: utf-8 -*-


# 標準 C で定義されている初歩的な数学関数を扱う
# 数学定数 pi と e をインポート
from math import exp, e, pi, log, sin, sqrt, pow

PI = pi
E = e
N = 8

# Bernoulli数
# list of B_2*i
B_2i = [1, (1.0 / 6.0), (-1.0 / 30.0), (1.0 / 42.0), (-1.0 / 30.0), (5.0 / 66.0),
     (-691.0 / 2730.0), (7.0 / 6.0), (-3617.0 / 510.0)]
"""
B0 = 1
B1 = (-1.0 / 2.0)
B2 = (1.0 / 6.0)
B4 = (-1.0 / 30.0)
B6 = (1.0 / 42.0)
B8 = (-1.0 / 30.0)
B10 = (5.0 / 66.0)
B12 = (-691.0 / 2730.0)
B14 = (7.0 / 6.0)
B16 = (-3617.0 / 510.0)
"""


class Factorial():
    def Bernoulli_log_gamma(self, z):
        # Bernoulli数を用いたガンマ関数の導出
        # z: 入力値

        self.check_value_error(z)
        y = 1
        while z < N:
            y *= z
            z +=1
        w = 1 / (z * z)
        return (((((((( (B_2i[8] / (16  *15)) * w + (B_2i[7]/(14 * 13))) * w
                      + (B_2i[6] / (12 * 11))) * w + (B_2i[5] / (10 * 9)))) * w
                   + (B_2i[4] / (8 * 7))) * w + (B_2i[3] / (6 * 5))) * w
                 +(B_2i[2] / (4 * 3))) * w + (B_2i[1] / (2 * 1))) / z + 0.5 * log(2 * PI) - log(y) - z + (z - 0.5) * log(z)


    def Nemes_log_gamma(self, z):
        # Nemesによる近似式（関数電卓などの計算機用に用いる）
        # z: 入力値

        self.check_value_error(z)
        ans = 0.5 * (log(2 * PI) - log(z)) + z * (log(z + 1 / (12 * z - 1 / (10 * z))) - 1)
        return ans

    def Euler_log_gamma(self, z):
        # オイラーの和公式による導出
        # z: 入力値
        self.check_value_error(z)
        ans = log(sqrt(2 * PI)) - z + (z - 0.5) * log(z) + 1/(12 * z) - 1/(360 * pow(z, 3)) + 1/(1260 * pow(z, 5)) + 1/(1680 * pow(z, 7)) + 1/(1188 * pow(z, 9))
        return ans


    def gamma(self, x, select = 0):
        # ガンマ関数を計算
        # x: 入力値
        # select: ガンマ関数の導出方法の選択
        #        0:Bernoulli(default), 1:Nemes, 2:Euler

        if x < 0:
            # マイナスの値の階乗計算
            if select == 1:
                b = exp(self.Nemes_log_gamma(1 - x))
            elif select == 2:
                b = exp(self.Euler_log_gamma(1 - x))
            else:
                b = exp(self.Bernoulli_log_gamma(1 - x))
            return PI / (sin(PI * x) * b)
        else:
            if select == 1:
                return exp(self.Nemes_log_gamma(x))
            elif select == 2:
                return exp(self.Euler_log_gamma(x))
            else:
                return exp(self.Bernoulli_log_gamma(x))


    def factorial(self, k, select = 0):
        # ガンマ関数を用いた階乗計算
        # k: 入力値
        # select: ガンマ関数の導出方法の選択
        #        0:Bernoulli(default), 1:Nemes, 2:Euler

        return self.gamma(k + 1, select)


    def int_factorial(self, k):
        # 入力が正の整数である場合の階乗計算
        # k: 入力値

        self.is_minus_error(k)
        ans = 1
        for i in range(int(k)):
            ans *= (i + 1)
        return ans


    def kaijo(self, k, select = 0, switch = 0):
        # 階乗計算のメソッド
        # k: 入力値
        # select: ガンマ関数の導出方法の選択
        #        0:Bernoulli(default), 1:Nemes, 2:Euler
        # switch:
        #        0:入力が正の整数である場合に、自動的に正の整数用の計算を行う
        #        1:入力の値に関わらず、selectで選択したガンマ関数の導出法で計算

        if switch == 0:
            if self.is_p_int(k) == True:
                return self.int_factorial(k)
            else:
                return self.factorial(k, select)
        else:
            return self.factorial(k, select)


    @staticmethod
    def is_minus_error(x):
        # 数値のチェックを行う
        # 0 未満の値に対してエラー
        if x < 0:
            raise ValueError, "minus_value is not available!"

    @staticmethod
    def check_value_error(x):
        # 入力値のチェックを行う
        # ガンマ関数の導出式は、(入力値) > 0 の制約がある

        if x <= 0.0:
            raise ValueError, "[" + str(x) + "] is not available!"

    @staticmethod
    def is_p_int(x):
        # 値が正の整数であればTrueを返す
        y = int(x)
        if x == y and x >= 0:
            return True
        else:
            return False

