#Tagging analytic forms in the Russian National Corpus

import os, re

def tag_fut(text): #future compound forms of imperfective verbs - adding tag fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_2(text): #future compound forms of imperfective verbs - tag fut_an
    text2 = re.sub('(lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
<w><ana lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_3(text): #future compound forms of imperfective verbs - tag fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w>.+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_4(text): #future compound forms of imperfective verbs - tag fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
(?:(?:<w><ana lex="и" gr="CONJ"></ana>[^\s]+?</w>)|(?:<w><ana lex="или" gr="CONJ"></ana>[^\s]+?</w>))\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2,fut_an\\3', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_compar(text): #comparative compound forms - tag comp_an
    text2 = re.sub('(?<!<w><ana lex="то" gr="S-PRO,n,sg=ins"></ana>тем</w>\n\
<w><ana lex="не" gr="PART"></ana>не</w>\n\
)(<w><ana lex="(?:(?:более)|(?:менее))" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="(?:(?:A=)|(?:[0-9A-Za-z=,\-]*?partcp)|(?:ADV))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,comp_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_superl(text): #superlative compound forms - tag supr_an
    text2 = re.sub('(lex="(?:(?:наиболее)|(?:наименее)|(?:самый))" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="(?:(?:A=)|(?:[0-9A-Za-z=,\-]*?partcp))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,supr_an\\2', text)
    text3 = re.sub('(lex="(?:(?:наиболее)|(?:наименее))" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="ADV[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,supr_an\\2', text2)
    text4 = re.sub('(<w><ana lex=".+?" gr="(?:(?:A=)|(?:[0-9A-Za-z=,\-]*?partcp)|(?:ADV))[0-9A-Za-z=,\-]*?comp[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
<w><ana lex="все" gr="[0-9A-Za-z=,\-]*?"></ana>всех</w>)', '\\1,supr_an\\2', text3)
    if text4:
        return(text4)
    else:
        return(text)

def tag_subjunctive(text): #subjunctive mood compound forms - tag subj_an
    text2 = re.sub('(lex=".+?" gr="(?:(?:PRAEDIC)|(?:V[0-9A-Za-z=,\-]*?(?:(?:inf)|(?:praet))))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
<w><ana lex="бы?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_subjunctive_2(text): #subjunctive mood compound forms - tag subj_an
    text2 = re.sub('(?<!хотя)(?<!как)(?<!будто)(?<!словно)(?<!точно)(?<!вроде)(" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>.*?\n\
<w><ana lex="бы?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:inf)|(?:praet))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_subjunctive_3(text): #subjunctive mood compound forms - tag subj_an
    text2 = re.sub('(<w><ana lex="чтобы" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
(?:<w>.+?</w>\s?\n\
)?<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:inf)|(?:praet))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_passive(text): #passive voice compound forms - tag pass_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".*?(?:(?:бегнуть)|(?:стигнуть)|(?:стынуть))" gr="V[0-9A-Za-z=,\-]*?)\
("></ana><ana lex="[а-яё]+?" gr="V[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,pass_an\\2,pass_an\\3', text)
    text3 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="[0-9A-Za-z=,\-]*?pass[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,pass_an\\2', text2)
    if text3:
        return(text3)
    else:
        return(text)

def tag_coop(text): #imperative compound forms of cooperative action - tag coop_an
    text2 = re.sub('(lex="давай(?:те)?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:imper)|(?:inf))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,coop_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

path = input('Type a path to a folder containing texts for tagging: ')
if os.path.exists(path):
    new_path = path + '_result/'
    try:
        os.makedirs(new_path)
    except:
        pass
    for root, dirs, files in os.walk(path):
        for i in files:
            r = re.search('\.([0-9a-zA-Z]+)$', i)
            if r:
                form = r.group(1)
                if form == 'xhtml':
                    fr = open(root + '/' + i, 'r', encoding = 'windows-1251')
                    text1 = fr.read()
                    fr.close()
                    text2 = tag_coop(tag_passive(tag_subjunctive_3(tag_subjunctive_2(tag_subjunctive(tag_superl(tag_compar(tag_fut_3(tag_fut_2(tag_fut(tag_fut_4(text1)))))))))))
                    fw = open(new_path + i, 'w', encoding = 'windows-1251')
                    fw.write(text2)
                    fw.close()
else:
    print('Path does not exist')
