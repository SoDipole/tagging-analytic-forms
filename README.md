# tagging-analytic-forms
Tagging analytic forms in the Russian National Corpus

Description
----------
analytic_tagging.py is a script for tagging russian analytic forms in texts from Russian National Corpus (http://www.ruscorpora.ru/index.html). 
The script is written in Python (version 3.5.1.). Used libraries: os, re.

Insruction
----------
To use this script:
- Have a compatible version of Python installed
- Download the analytic_tagging.py file
- Run the file
- In a command window type in a path to a folder that contains texts for tagging (Example: corpus/texts)
- If folder exists new folder (Example: texts_result) will be created containing texts with tags added

Texts format
-----------
Script works with xhtml files in windows-1251 encoding. Texts are disambiguated texts from Russian National Corpus with meta tagging and morphological tagging.
Text fragment:
```
...
<p><se>
<w><ana lex="мой" gr="A-PRO=m,sg,nom"></ana>Мой</w>
<w><ana lex="брат" gr="S,m,anim=sg,nom"></ana>брат</w>
<w><ana lex="не" gr="PART"></ana>не</w>
<w><ana lex="быть" gr="V,ipf,intr,act=sg,fut,3p,indic"></ana>б`удет</w>
<w><ana lex="играть" gr="V,ipf,tran=inf,act"></ana>игр`ать</w>
<w><ana lex="в" gr="PR"></ana>в</w>
<w><ana lex="фойе" gr="S,n,inan,0=sg,loc"></ana>фой`е</w>!
</se>
...
```

Output
-----------
Script creates new texts in which tags are added.
List of tags:
- fut_an (future compound forms of imperfective verbs)
- comp_an (comparative compound forms)
- supr_an (superlative compound forms)
- subj_an (subjunctive mood compound forms)
- pass_an (passive voice compound forms)
- coop_an (imperative compound forms of cooperative action)

Text fragment with fut_an tag added:
```
...
<p><se>
<w><ana lex="мой" gr="A-PRO=m,sg,nom"></ana>Мой</w>
<w><ana lex="брат" gr="S,m,anim=sg,nom"></ana>брат</w>
<w><ana lex="не" gr="PART"></ana>не</w>
<w><ana lex="быть" gr="V,ipf,intr,act=sg,fut,3p,indic"></ana>б`удет</w>
<w><ana lex="играть" gr="V,ipf,tran=inf,act,fut_an"></ana>игр`ать</w>
<w><ana lex="в" gr="PR"></ana>в</w>
<w><ana lex="фойе" gr="S,n,inan,0=sg,loc"></ana>фой`е</w>!
</se>
…
```
