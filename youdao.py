import requests

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/5.0.0-alpha.10',
}

def get_json(word):
    r = requests.get('https://dict.youdao.com/jsonapi', params={'q':word}, headers=HEADERS,)
    return r.json()

class Youdao:
    def __init__(self, word):
        self.json = get_json(word)
        self.dicts = self.json['meta']["dicts"]

    def get_ec(self):
        if "ec" in self.dicts:
            ec = []
            word = self.json['ec']['word'][0]
            if 'usphone' in word.keys() and 'usspeech' in word.keys():
                ec.append("[美{}](https://dict.youdao.com/dictvoice?audio={})".format(word['usphone'],word['usspeech']))
            if 'ukphone' in word.keys() and 'ukspeech' in word.keys():
                ec.append("[英{}](https://dict.youdao.com/dictvoice?audio={})".format(word['ukphone'],word['ukspeech']))
            for tr in  word['trs']:
                ec.append(' '.join(tr['tr'][0]['l']['i']))
            if 'wfs' in word.keys():
                for wf in word['wfs']:
                    ec.append(' '.join([str(v) for v in wf['wf'].values()]))
            return ec
        else:
            return None

#keys: 
#web_trans, 
#ee, 
#blng_sents_part,
#auth_sents_part,
#simple,
#etym,
#phrs PASS
#special PASS
#syno,
#input,
#collins,
#meta,
#le,
#wikipedia_digest,
#lang,
#ec,

def handle_wikipedia_digest(dig):
    pass
def handle_collins(collins):
    entr0 = collins['collins_entries'][0]
    print(entr0)
    if 'phonetic' in entr0.keys():
        print(txt_effect('音标: [{}]'.format(entr0['phonetic']), 2))
    for e in entr0['entries']['entry']:
        parser(e['tran_entry'])

def handle_simpe(sim): 
    for i in sim['word']:
        print("美[{}](https://dict.youdao.com/dictvoice?audio={})".format(i['usphone'],i['usspeech']))
        print("英[{}](https://dict.youdao.com/dictvoice?audio={})".format(i['ukphone'],i['ukspeech']))

def handle_etym(etym): 
    print(txt_effect(txt_effect('起源',1),31))
    etyms = etym['etyms']
    for k,l in etyms.items():
        for v in l:
            if isinstance(v ,dict):
                print("{2} {0} ({1})".format(v["value"],v['source'],txt_effect(k,2)))


def handle_ee(ee):
    ee = ee["word"]["trs"]
    for tr in ee:
        print(tr)

def handle_auth(auth):
    pass

def handle_blng(blng):
    print("Sentences : {}".format(blng['sentence-count']))
    sen_pair = blng['sentence-pair']
    i = 1
    for sen in sen_pair:
        print("{}. {} {} ({})".format(str(i),sen['sentence-eng'],sen['sentence-translation'], sen['source']))
        i += 1
    print(blng['trs-classify'])
