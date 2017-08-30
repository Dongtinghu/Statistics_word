#_*_coding:utf-8_*_
#!/usr/bin/python36
#判断字母，并提取出所有单词，转换成小写，并输出单词列表
#from sys import argv
#discribt , zimufile = argv
#导入字幕文件
def check_word_frequency(file_adress):
    f = open (file_adress)#('Friends.S01E01.The.One.Where.Monica.Gets.A.New.Roommate.DVDRip.AC3.3.2ch.JOG.srt')
    #导入文件
    data =f.read()
    f.close()
    astr = data
    wordlist = []
    wordadress = 0
    string1 = ''
    for a in astr:
        wordadress += 1
        if (a >= 'a' and a <= 'z') or (a >= 'A' and a<= 'Z'):
            string1 += a
        else:
            if not(string1 ==''):
                wordlist.append(string1.lower())
            string1 =''
    #列表排序
    wordlist = sorted(wordlist)
    #print(wordlist)
    worddic = {}
    #单词字典的键
    key_worddic =0
    len_wordlist = len(wordlist)
    word_frequency = 0
    for i in range(0 , len_wordlist):
        #判断是否是最后一个
        if  i == (len_wordlist - 1):
            key_worddic += 1
            continue
        a = wordlist[i]
        b = wordlist[i + 1]
        if a == b:#worddic[i] == wordlist[i + 1]:
            word_frequency +=1
        else:
            #频率归1，单词种类加1
            word_frequency += 1
            key_worddic +=1
        #给键赋值，单词及频率
            worddic[key_worddic] =(wordlist[i],word_frequency)
        #出现新单词，频率归零
        if a != b:#worddic[i] == wordlist[i + 1]:
            word_frequency = 0
    #worddic=sorted(worddic.items())
    print(worddic)
    return worddic