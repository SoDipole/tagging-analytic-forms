import os, re

def tag_fut(text): #будущее время глаголов несов. вида - тэг fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_2(text): #будущее время глаголов несов. вида (инфинитив на 1 месте) - тэг fut_an
    text2 = re.sub('(lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
<w><ana lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_3(text): #будущее время глаголов несов. вида (инфинитив через 1 слово) - тэг fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w>.+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_fut_4(text): #будущее время глаголов несов. вида (два инфинитива с союзом) - тэг fut_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?fut[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
(?:(?:<w><ana lex="и" gr="CONJ"></ana>[^\s]+?</w>)|(?:<w><ana lex="или" gr="CONJ"></ana>[^\s]+?</w>))\s?\n\
<w><ana lex=".+?" gr="V,ipf[0-9A-Za-z=,\-]*?inf[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,fut_an\\2,fut_an\\3', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_compare(text): #сравнительная степень прил/прич/нареч - тэг comp_an
    text2 = re.sub('(?<!<w><ana lex="то" gr="S-PRO,n,sg=ins"></ana>тем</w>\n\
<w><ana lex="не" gr="PART"></ana>не</w>\n\
)(<w><ana lex="(?:(?:более)|(?:менее))" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="(?:(?:A=)|(?:[0-9A-Za-z=,\-]*?partcp)|(?:ADV))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,comp_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_superl(text): #превосходная степень прил/прич/нареч - тэг supr_an
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

def tag_subjunctive(text): #сослагательное наклонение - тэг subj_an
    text2 = re.sub('(lex=".+?" gr="(?:(?:PRAEDIC)|(?:V[0-9A-Za-z=,\-]*?(?:(?:praet)|(?:inf))))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>\s?\n\
<w><ana lex="бы?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_subjunctive_2(text): #сослагательное наклонение - тэг subj_an
    text2 = re.sub('(?<!хотя)(?<!как)(?<!будто)(?<!словно)(?<!точно)(?<!вроде)(" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>.*?\n\
<w><ana lex="бы?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:praet)|(?:inf))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_subjunctive_3(text): #сослагательное наклонение (чтобы) - тэг subj_an
    text2 = re.sub('(<w><ana lex="чтобы" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
(?:<w>.+?</w>\s?\n\
)?<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:praet)|(?:inf))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,subj_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)

def tag_passive(text): #страдательный залог - тэг pass_an
    text2 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".*?(?:(?:бегнуть)|(?:стигнуть)|(?:стынуть))" gr="V[0-9A-Za-z=,\-]*?)\
("></ana><ana lex="[а-яё]+?" gr="V[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,pass_an\\2,pass_an\\3', text)
    text3 = re.sub('(lex="быть" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="[0-9A-Za-z=,\-]*?pass[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,pass_an\\2', text2)
    if text3:
        return(text3)
    else:
        return(text)

def tag_coop(text): #совместное действие - тэг coop_an
    text2 = re.sub('(lex="давай(?:те)?" gr="[0-9A-Za-z=,\-]*?"></ana>[^\s]+?</w>\s?\n\
<w><ana lex=".+?" gr="V[0-9A-Za-z=,\-]*?(?:(?:imper)|(?:inf))[0-9A-Za-z=,\-]*?)("></ana>[^\s]+?</w>)', '\\1,coop_an\\2', text)
    if text2:
        return(text2)
    else:
        return(text)
    
#path = './test'
path = './final_test/auto_tagging'
#path = './corpora_1M'
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
                print(i)
                text1 = fr.read()
                fr.close()
                text2 = tag_coop(tag_passive(tag_subjunctive_3(tag_subjunctive_2(tag_subjunctive(tag_superl(tag_compare(tag_fut_3(tag_fut_2(tag_fut(tag_fut_4(text1)))))))))))
                fw = open(new_path + i, 'w', encoding = 'windows-1251')
                fw.write(text2)
                fw.close()
