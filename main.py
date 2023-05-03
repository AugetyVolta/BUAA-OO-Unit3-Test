import os
file_add = "data"
echo_on = False
for home, dirs, files in os.walk(file_add):
    for i in range(1, len(files) + 1):
        os.system('chcp 65001')
        os.system(f'java -jar hw10_code.jar<data\\random{i}.txt >out\\out{i}.txt')
        if echo_on:
            os.system(f'fc ans\\ans{i}.txt out\\out{i}.txt >diff\\diff{i}.txt')
        else:
            os.system(f'fc ans\\ans{i}.txt out\\out{i}.txt')
