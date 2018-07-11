# -*- coding: utf-8 -*-
# by DrZ3r0
import base64
import re
import sys


def url_decode(url_enc):
    lenght = len(url_enc)
    print ("LEN ==> "+str(lenght)+"\n")
    if lenght % 2 == 0:
        len2 = int(lenght / 2)
        print ("LEN2 ==> "+str(len2)+"\n")
        first = url_enc[0:len2]
        last = url_enc[len2:lenght]
        url_enc = last + first
        reverse = url_enc[::-1]
        return base64.b64decode(reverse)

    last_car = url_enc[lenght - 1]
    url_enc[lenght - 1] = ' '
    url_enc = url_enc.strip()
    len1 = len(url_enc)
    len2 = len1 / 2
    first = url_enc[0:len2]
    last = url_enc[len2:len1]
    url_enc = last + first
    reverse = url_enc[::-1]
    reverse = reverse + last_car
    return base64.b64decode(reverse)

print ("START\n")

var2 = url_decode("0lWbf5WVf1yXpJXYyJXZG9yc5N3SmljVxZDUh9CZlJWbl9ybj5CZh9GbuVGcv9yL6MHc0RHa==ANQ1kL5ITJ3EDMygjMl8FR1UCcwYzMtJUNl8FR1USQUlULiV3UCVTJfVGbhRncv1Wbp91b")
print (var2)
