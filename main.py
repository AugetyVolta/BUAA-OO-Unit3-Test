import os
import generator


def cmp_file(file1, file2):
    l1 = []
    l2 = []
    with open(file1, 'r') as f:
        l1 = f.read().splitlines()
    with open(file2, 'r') as f:
        l2 = f.read().splitlines()
    if len(l1) != len(l2):
        print("len not eq")
        return
    ok = True
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            print(f'not equals at line {i + 1}')
            ok = False
    if ok:
        print('good')


if __name__ == '__main__':
    print("======DATA GENERATING======")
    os.system('python generator.py')
    print("======COMPLETE======")
    file_add = "data"
    echo_on = False
    for home, dirs, files in os.walk(file_add):
        for i in range(1, len(files) + 1):
            os.system(f'java -jar code.jar<data/random{i}.txt >out/out{i}.txt')
            if echo_on:
                os.system(f'fc ans/ans{i}.txt out/out{i}.txt >diff/diff{i}.txt')
            else:
                print(f'testId:{i}')
                cmp_file(f'ans/ans{i}.txt', f'out/out{i}.txt')
    print("======TEST FINISH======")
