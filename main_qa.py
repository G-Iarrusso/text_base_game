import glob
from subprocess import call

for file in glob.glob("UT*.py"):
    call(["python", file])
