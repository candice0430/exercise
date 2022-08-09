# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count_words(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        data = f.readlines()
    print(data)
    words = []
    for line in data:
        # print(line)
        d = re.findall('[a-zA-Z]+',line)
        print(d)
        for d1 in d:
            words.append(d1)
    print("words:",words)
    return len(words)


if __name__ == '__main__':
    c = count_words('./pic/words.txt')
    print("单词个数：",c)
    