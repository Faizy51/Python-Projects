import bs4 as bs
import urllib.request
import re
import csv


usnlist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','51','53','54','56','57','58','59','60','61','62']
i = 0
names = []
marks = []

while i<len(usnlist):
    htmlfile = urllib.request.urlopen('http://results.vtu.ac.in/results17/result_page.php?usn=1bg13cs0'+usnlist[i])
    htmlte = htmlfile.read()
    htmltext = str(htmlte)

    regex = '<td style="padding-left:15px"><b>:</b>(.+?)</td>'
    regex2 = '<td style="padding-left:10px"><b>:(.+?)</b></td>'
    
    pattern = re.compile(regex)
    pattern2 = re.compile(regex2)

    name = re.findall(pattern,htmltext)
    mark = re.findall(pattern2,htmltext)

##    names.append(name[0])
##    marks.append(mark[0])
    print (name[0] , mark[0])
    i+=1

##n = open('new2.csv',"r+", newline = '')
##csv_n = csv.writer(n)
##ip = csv.reader(n)
##for item in names:
##    csv_n.writerow(item)
##for row in ip:
##    row[1] = marks[i]
##    csv_n.writerow()
##    i+=1
