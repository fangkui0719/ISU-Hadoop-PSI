# -*- coding: cp950 -*-
TestItem = ['NMHC','NOx','O3']

#搜尋測資
"""
目標搜尋
從仁武監測站中找到NMHC,NOx,O3三個測資
假如找到回傳0令程式不繼續跑迴圈
假使不是以上三樣測資，回傳1則跳過接下來的步驟
"""
def search(Item):
    for T in TestItem:
        if T == Item:
            return 0
    return 1
#搜尋目標輸出Csv檔案
"""
因為輸出檔案只有三項，所以採用線性搜尋
"""
def searchOutputCsv(Item):
    count = 0
    while Item != TestItem[count]:
        count = count + 1
    return count
#從91~104年的仁武監測站中過濾出NMHC,NOx,O3三項測資
"""
最外圈使用年份，從91~104年開始
"""
for year in range(91,105):
    fin = open(str(year)+'年仁武站.csv','r')
    f = []
    titlecount = 0
    for Item in  TestItem:
        f.append(open(str(year)+'年仁武@'+Item+'.csv','w'))
        #f[titlecount].write('Date'+','+'Value'+'\n');
        titlecount = titlecount + 1

    #以上for迴圈設定檔案輸出
    
    rowData = fin.readline().rstrip('\n').split(',')    #過濾標頭
    
    for rowData in fin:
        rowData = rowData.rstrip('\n').split(',')
        #讀取一行並作拆解
        if search(rowData[2]):
            continue
        #採用線性搜尋 若不是目標測資直接跳過
        if rowData[2] == 'O3':
            value = rowData[3:27]
            times = 24
        else:
            value = rowData[8:13]
            times = 5
        #取得日期，早晨時間6~10點
        clearCount = 0
        for clearValue in value:
            if clearValue == '' or not clearValue[-1].isdigit():
                value[clearCount] = 0
            
            clearCount = clearCount + 1
        
        value[:] = [float(x) for x in value]
        value.sort()
        f[searchOutputCsv(rowData[2])].write(rowData[0]+','+str(value[-1])+'\n');
        #輸出格式 (日期/值)
    fin.close()
    for closeCsv in range(0,3):
        f[closeCsv].close()
    #關閉檔案
