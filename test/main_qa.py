import glob
from subprocess import call

for file in glob.glob("test/UT*.py"):
    call(["python", file])
