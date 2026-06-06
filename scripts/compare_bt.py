from pathlib import Path
c=Path('C:/Users/kjeti/Source/repos/sofle-ergom-zmk/config/sofle_ergomech.keymap').read_text(encoding='utf-8').splitlines()
s=Path('C:/Users/kjeti/Source/repos/sofle-ergom-zmk/boards/shields/sofle_ergomech/sofle_ergomech.keymap').read_text(encoding='utf-8').splitlines()
cline_multi=[l for l in c if l.count('&bt')>1]
if cline_multi:
    cline=cline_multi[0]
else:
    cline=''
sline=[l for l in s if l.count('&bt')>1][0]
print('config long BT line repr:')
print(repr(cline))
print('\nshield BT line repr:')
print(repr(sline))
minlen=min(len(cline),len(sline))
for i in range(minlen):
    if cline[i]!=sline[i]:
        print('\nfirst diff at',i+1,'config char',repr(cline[i]),'shield char',repr(sline[i]))
        print('config slice',repr(cline[max(0,i-10):i+10]))
        print('shield slice',repr(sline[max(0,i-10):i+10]))
        break
else:
    if len(cline)!=len(sline):
        print('\nno diffs in minlen but lengths differ: config',len(cline),'shield',len(sline))
    else:
        print('\nlines identical')
print('\nConfig bytes around index 56:', list(map(ord, cline[:80])))
print('Shield bytes around index 56:', list(map(ord, sline[:80])))
