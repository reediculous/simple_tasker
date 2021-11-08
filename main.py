import os


def get_task(id):
    file = open(f"tasks/task{id}/Assignment.txt")
    text = file.read()
    return text


def gen_tests(id):
    file = open(f"tasks/task{id}/Tests.txt")
    raw_text = file.read()
    tests = raw_text.split("---")
    return tests


def check(solution, id):
    code = open(solution).read()
    tests = gen_tests(id)
    print(tests)
    for test in tests:
        lines = test.strip("\n").split("\n")
        inp_file = open("input.txt", "w")
        inp_file.write(lines[0])
        inp_file.close()
        correct = lines[1]
        exec(code)
        outp_file = open("output.txt")
        answer = outp_file.read()
        outp_file.close()
        if answer == correct:
            print("OK")
        else:
            print("WA")
        os.remove("input.txt")
        os.remove("output.txt")


sol = input()
check(sol, 1)

