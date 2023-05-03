from typing import Any

import os
import generator

pass_cnt = 0


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
    return ok


if __name__ == '__main__':
    n = 100  # 设置测试点总数
    generator = 'code.jar'  # 用于数据生成的jar包
    tester = 'mine.jar'  # 用于对拍的jar包
    file_add = "data"
    echo_on = False
    print("======DATA GENERATING======")
    os.system(f'python generator.py {n} {generator}')
    print("======COMPLETE======")
    folder = os.path.exists('out')
    if not folder:
        os.makedirs('out')
    folder = os.path.exists('diff')
    if not folder:
        os.makedirs('diff')
    for home, dirs, files in os.walk(file_add):
        for i in range(1, len(files) + 1):
            os.system(f'java -jar {tester}<data/random{i}.txt >out/out{i}.txt')
            print(f'testId:{i}')
            if echo_on:
                os.system(f'fc ans/ans{i}.txt out/out{i}.txt >diff/diff{i}.txt')
            else:
                ok = cmp_file(f'ans/ans{i}.txt', f'out/out{i}.txt')
                if ok:
                    pass_cnt = pass_cnt + 1
    if pass_cnt == n:
        print("You have passed all the tests.")
    else:
        print(f"You have {n - pass_cnt} errors.")
    print("======TEST FINISH======")
