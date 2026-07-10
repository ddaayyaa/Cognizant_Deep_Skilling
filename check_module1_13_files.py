from pathlib import Path
import shutil
import subprocess
import sys
from collections import defaultdict

base = Path(r'c:\Users\ydaya\Desktop\Cognizant Deep Skilling')
modules = [
    'Module_01_Java_Fundamentals',
    'Module_02_Object_Oriented_Programming',
    'Module_03_Exception_Handling',
    'Module_04_Collections_Framework',
    'Module_05_Multithreading',
    'Module_06_File_Handling',
    'Module_07_JDBC',
    'Module_08_SQL_MySQL',
    'Module_09_HTML_CSS_JavaScript',
    'Module_10_ReactJS',
    'Module_11_Spring_Core',
    'Module_12_Spring_Boot',
    'Module_13_Git_GitHub_Maven',
]

all_files = []
for module in modules:
    root = base / module
    if not root.exists():
        continue
    for path in root.rglob('*'):
        if path.is_file():
            all_files.append(path)

counts = defaultdict(int)
for p in all_files:
    counts[p.suffix] += 1
print('Total files:', len(all_files))
for ext, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
    print(f'{ext or "<noext>"}: {count}')

java_files = [p for p in all_files if p.suffix == '.java']
print('Java files:', len(java_files))

# Attempt to compile Java files that are standalone
javac = shutil.which('javac') if 'shutil' in globals() else None
if javac is None:
    import shutil
    javac = shutil.which('javac')
print('javac:', javac)

if javac:
    errors = []
    for path in java_files:
        # compile independently to temp directory with no package issues
        rel = path.relative_to(base)
        target = base / 'tmp_compile'
        target.mkdir(exist_ok=True)
        cmd = [javac, '-d', str(target), str(path)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            errors.append((path, proc.stderr.strip()))
    print('Compile errors:', len(errors))
    for path, err in errors[:20]:
        print('ERROR:', path)
        print(err)
else:
    print('No javac available.')
