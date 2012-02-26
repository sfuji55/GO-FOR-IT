#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt
from random import randint

MAX_SCALE = 22 # 鍵盤の右端
MIN_SCALE = -29 # 鍵盤の左端
NOTES_SPAN = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]

class Note():
    # 音符クラス
    def __init__(self, scale = 0, note_value = 4.0, dot = 1.0, option = 0):
        # 初期化
        self.scale = float(scale)
        self.note_value = float(note_value)
        self.dot = int(dot)
        self.option = float(option)


    def __str__(self):
        # 出力時の形式を設定
        scale = str(int(self.scale))
        note_value = str(int(self.note_value))
        if self.dot == 1.5:
            note_value += "."
        elif self.dot != 1.0:
            raise ValueError, 'unavailable dot_value'

        n = self.option
        if n == 0.0:
            option = ''
        elif n == -1.0:
            option = 'd'
        elif n == -0.5:
            option = 'b'
        elif n == 0.5:
            option = 's'
        elif n == 1.0:
            option = 'x'

        return scale + ':' + note_value + ':' + option

    def copy(self):
        return Note(self.scale, self.note_value, self.dot, self.option)

    def get_a_scale(self):
        return float(self.scale + self.option)

    def get_a_value(self):
        return float(self.note_value / self.dot)

    @staticmethod
    def fromstring(s):
        # 音符1つ分の入力データから、音符クラスを作成する
        toks = s.split(':')

        x = float(toks[0])
        y = float(toks[1])
        z = 1.0
        if y not in NOTES_SPAN:
            raise ValueError, '[' + y + '] is not available'
        if toks[1][-1] == '.':
            z = 1.5

        if toks[2] == '':
            w = 0.0
        elif toks[2] == 'd':
            w = -1.0
        elif toks[2] == 'b':
            w = -0.5
        elif toks[2] == 's':
            w = 0.5
        elif toks[2] == 'x':
            w = 1.0
        else:
            raise ValueError, '[' + toks[2] + '] is not acceptable'

        return Note(x, y, z, w)

class Rest():
    # 休符クラス
    def __init__(self, rest_value = 4.0):
        self.rest_value = rest_value

    def __str__(self):
        rest_value = str(int(self.rest_value))
        return ':' + rest_value + ':'

    def copy(self):
        return Rest(self.rest_value)

    @staticmethod
    def fromstring(s):
        # 休符1つ分の入力データから、休符クラスを作成する
        toks = s.split(':')

        rest_value = float(toks[1])
        if rest_value not in NOTES_SPAN:
            raise ValueError, '[' + rest_value + '] is not available'

        return Rest(rest_value)


class Melody():
    def __init__(self, melody = []):
        self.melody = melody

    def __str__(self):
        s = ''
        for item in self.melody:
            s += str(item)
            s += ','
        return s[:-1]

    def get_feature(self):
        s = 0.0
        melody = self.melody
        for i in range(len(melody)-1):
            t0 = melody[i]
            t1 = melody[i+1]
            if isinstance(t0, Note) & isinstance(t1, Note):
                s += self.get_distance(t0, t1)
            elif isinstance(t1, Rest):
                s += (1/ t1.rest_value)
        return round(s)

    def get_distance(self, note0, note1):
        return sqrt((note1.get_a_scale() - note0.get_a_scale())**2 + (1 / note0.get_a_value())**2)

    def get_span(self):
        s = 0.0
        for i in range(len(self.melody)):
            if isinstance(self.melody[i], Note):
                s += 1 / self.melody[i].note_value
            else:
                s += 1/ self.melody[i].rest_value
        return s

    def predict(self, feature = 14.0, span = 4.0, start = None, end = None):
        s_note = []
        e_note = []
        r = 0.0
        if start != None and isinstance(start, Note):
            s_note.append(start)
            r += 1 / s_note[0].note_value
        if end != None and isinstance(end, Note):
            e_note.append(end)
            r += 1 / e_note[0].note_value

        n = span - r
        p_melody = Piece_of_Melody().create(n)
        for i in range(1000):
            index = randint(0, 100) % len(p_melody.piece)
            var = randint(0, 4)
            x = p_melody.variation(index, var)
            y = Melody(s_note + x.piece + e_note)
            if y.get_feature() == feature and i > 10 and y.get_span() == span:
                return y
            elif y.get_feature() > feature:
                continue
            p_melody = x

        print "Miss!!"
        return Melody(s_note + x.piece + e_note)


    @staticmethod
    def fromstring(s):
        melody = []
        for toks in s.split(','):
            if toks[0] == ':': # Rest
                melody.append(Rest.fromstring(toks))
            else:
                melody.append(Note.fromstring(toks))

        return Melody(melody)



class Piece_of_Melody():
    def __init__(self, piece = []):
        self.piece = piece

    def create(self, span = 1.0,low = -6, high = 6):
        # 直線的なピースを作る
        n = int(span * 4)   # span の中に入る4分音符の数
        r = span - n / 4    # 4分音符を入れた後の余り

        start_note = Note(randint(low, high))
        end_note = Note(randint(low,high))
        x = start_note.scale
        y = end_note.scale
        gap = int(abs(y - x) / (n-1))

        t = []
        for i in range(n-4):
            t.append(Note(x + gap * (i+1)))

        if r != 0.0:
            t.insert(randint(0, len(t)), Rest(round(1 / r)))

        return Piece_of_Melody([start_note] + t + [end_note])


    def variation(self, index = 0, var = 0):
        # ピースの形を変化させる
        piece = self.piece
        if index > len(piece): index = 0

        if var == 0:
            # var 0: shift up all_note
            for i in range(len(piece)):
                if isinstance(piece[i], Note):
                    piece[i].scale += 1.0
        elif var == 1:
            # var 1; shift down all_note
            for i in range(len(piece)):
                if isinstance(piece[i], Note):
                    piece[i].scale -= 1.0
        elif var == 2:
            # var 2: increase scale
            if isinstance(piece[index], Note):
                piece[index].scale += 1.0
        elif var == 3:
            # var 3: decrease scale
            if isinstance(piece[index], Note):
                piece[index].scale -= 1.0
        elif var == 4:
            # var4: split
            piece = self.split(index)
        #elif var == 5:
            # var 5: delete
            #piece = self.delete(index)

        return Piece_of_Melody(piece)


    def split(self, index):
        piece = self.piece
        if isinstance(piece[index], Note):
            piece[index].note_value *= 2
        else:
            piece[index].rest_value *= 2
        piece.insert(index + 1, piece[index].copy())

        return piece

    def delete(self, index):
        piece = self.piece
        if len(piece) > 2:
            if isinstance(piece[index], Note):
                x = piece[index].note_value
                piece.remove(piece[index])
                for i in reversed(range(len(piece))):
                    if isinstance(x, Note) and x == piece[i].note_value:
                        piece[i].note_value *= 2
                        piece[i].note_value /= 4.0
                        return piece
            else:
                x = piece[index].rest_value
                piece.remove(piece[index])
                for i in reversed(range(len(piece))):
                    if isinstance(x, Rest) and x == piece[i].rest_value:
                        piece[i].rest_value *= 2
                        piece[i].rest_value /= 4.0
                        return piece
        return piece


