# -*- coding: cp950 -*-
TestItem = ['NOx','NMHC','O3']
#目標合併檔案
"""
    最後輸出格式
    (日期，NOx/NMHC，O3)
"""
for year in range(102,105):
    fin = []
    for Item in  TestItem:
        fin.append(open(str(year)+'年仁武@'+Item+'.csv','r'))
    fout = open(str(year)+'年仁武PSI.csv','w')
    fout.write('date'+','+'NOx/Nmhc'+','+'O3'+'\n')
    #開啟輸入檔案(3個)設置輸出檔案(1個)
    for nox in fin[0]:
        nox = nox.rstrip('\n').split(',')
        nmhc = fin[1].readline().rstrip('\n').split(',')
        o3 = fin[2].readline().rstrip('\n').split(',')

        #(每個輸入檔案的一行)
        if nox[1][-1].isdigit() and nmhc[1][-1].isdigit() and o3[1][-1].isdigit() and nmhc[1][-1] != '0':
            fout.write(str(nox[0])+','+str(float(nox[1])/float(nmhc[1]))+','+str(o3[1])+'\n')
        #過濾無效值 假使三個檔案中其中有一個為無效值則不做輸出動作
    fin[0].close()
    fin[1].close()
    fin[2].close()
    fout.close()
    #關閉檔案
