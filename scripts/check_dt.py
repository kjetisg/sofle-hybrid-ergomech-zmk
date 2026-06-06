from pathlib import Path
p=Path('C:/Users/kjeti/Source/repos/sofle-ergom-zmk/config/sofle_ergomech.keymap')
s=p.read_text(encoding='utf-8')
lines=s.splitlines()
issues=[]
for i,l in enumerate(lines):
    if 'bindings = <' in l and 'sensor-bindings' not in l:
        # find next non-empty non-comment line
        j=i+1
        while j<len(lines) and lines[j].strip()=='' :
            j+=1
        if j<len(lines) and lines[j].lstrip().startswith('//'):
            issues.append((i+1, 'comment immediately after bindings = <', lines[j].lstrip()))
        # find closing '>;'
        k=i+1
        found=False
        while k<len(lines):
            if '>;' in lines[k]:
                found=True
                break
            k+=1
        if not found:
            issues.append((i+1, 'no closing >; found for bindings starting here', ''))

# global angle bracket balance
open_angle = s.count('<')
close_angle = s.count('>')

print('bindings-issues:')
for it in issues:
    print(' ',it)
print('angle-brackets: open',open_angle,'close',close_angle, 'diff', open_angle-close_angle)

# find lines with &bt BT_SEL pattern and show context
for i,l in enumerate(lines):
    if '&bt BT_SEL' in l:
        print('\nBT line', i+1, l)
        idx=l.find('&bt BT_SEL')
        print('context:', l[max(0,idx-20):idx+40])
