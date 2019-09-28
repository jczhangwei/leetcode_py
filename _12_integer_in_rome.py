import math


class Sollution:

    def intToRoman(self, num):
        m = {
            1000:"M",
            900: "CM",
            500:"D",
            400:"CD",
            100:"C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9:"IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        r = ""
        while(num > 0) :
            for k, v in m.items():
                if num >= k:
                    r = r + v
                    num = num - k
                    break
        return r        
