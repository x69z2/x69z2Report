import requests
import tempfile
import os
main = ''
def login(hh,hhh,hhhh,a,b,c,d,e,f,g,h):
    req = requests.get(str(hh+hhh+hhhh+a+b+c+d+e+f+g+str(h))).text
    return req