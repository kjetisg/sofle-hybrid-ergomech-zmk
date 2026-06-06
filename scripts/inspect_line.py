from pathlib import Path
path = Path(r'C:/Users/kjeti/Source/repos/sofle-ergom-zmk/config/sofle_ergomech.keymap')
lines = path.read_text(encoding='utf-8').splitlines()
line_num = 413
line = lines[line_num - 1]
print(f'{line_num}: {repr(line)}')
print('len=', len(line))
for i, ch in enumerate(line, start=1):
    if 18 <= i <= 30:
        print(f'{i}: {repr(ch)} ord={ord(ch)}')
print('slice 18-30:', repr(line[17:30]))
