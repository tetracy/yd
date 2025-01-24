import requests
import re
import html 
import sys
import json
import subprocess

class Bingimage:
    def __init__(self, query):
        self.query = query
        self.results = []
    
    def getpic(self):
        r = requests.get("https://cn.bing.com/images/search?q=%s"%(self.query))
        try:
            resp = r.text
            matches = [html.unescape(m)[3:-1]  for m in re.findall('m="{.*}"',  resp) ]
            self.results += [json.loads(i) for i  in matches] 
        except:
            pass

    def more(self):
        # https://cn.bing.com/images/async?q=apple&count=35
        pass


if __name__ == '__main__':
    x = Bingimage(sys.argv[1])
    x.getpic()
    MPVCMD = ['/usr/bin/mpv','--image-display-duration=inf']
    for i in x.results:
        if 'turl' in i.keys():
            MPVCMD.append(i['turl'])
    subprocess.run(MPVCMD)

