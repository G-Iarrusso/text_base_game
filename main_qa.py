"""
TODO
add a dict for #:test file
add a list of suites: PR, Daily, regression
pseudo code:
tests/regression = {
    1: "test_TC1_name"
    .
    .
    .
}
Daily = {
    base of code that people need to run
}
PR = {
    base of code to run on a PR
}
can expand to targeted regression i.e. movement, attacking, scavenging

run each test
"""
import glob
from subprocess import call

txtfiles = []
for file in glob.glob("UT*.py"):
    txtfiles.append(file)
    call(["python", file])
print(txtfiles)