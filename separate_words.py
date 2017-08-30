#*_*coding:utf-8*_*
#!/usr/bin/python36

from sys import argv
import panduanzimu
program_name,file_name = argv
#file_name = 'Friends.S01E01.The.One.Where.Monica.Gets.A.New.Roommate.DVDRip.AC3.3.2ch.JOG.srt'
worddic = panduanzimu.check_word_frequency(file_name)#'%s'%
#print worddic
out_file_name = "%s 词汇统计.txt"%file_name
#target = open(out_file_name, 'w')
#target.writelines(worddic)
#target.close()


