from subprocess import call
call(["python", "test.py"])
input("youve made it back?")
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
