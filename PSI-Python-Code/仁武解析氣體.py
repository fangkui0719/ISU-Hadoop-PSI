# -*- coding: cp950 -*-
TestItem = ['NMHC','NOx','O3']

#�j�M����
"""
�ؼзj�M
�q���Z�ʴ��������NMHC,NOx,O3�T�Ӵ���
���p���^��0�O�{�����~��]�j��
���Ϥ��O�H�W�T�˴���A�^��1�h���L���U�Ӫ��B�J
"""
def search(Item):
    for T in TestItem:
        if T == Item:
            return 0
    return 1
#�j�M�ؼп�XCsv�ɮ�
"""
�]����X�ɮץu���T���A�ҥH�ĥνu�ʷj�M
"""
def searchOutputCsv(Item):
    count = 0
    while Item != TestItem[count]:
        count = count + 1
    return count
#�q91~104�~�����Z�ʴ������L�o�XNMHC,NOx,O3�T������
"""
�̥~��ϥΦ~���A�q91~104�~�}�l
"""
for year in range(91,105):
    fin = open(str(year)+'�~���Z��.csv','r')
    f = []
    titlecount = 0
    for Item in  TestItem:
        f.append(open(str(year)+'�~���Z@'+Item+'.csv','w'))
        #f[titlecount].write('Date'+','+'Value'+'\n');
        titlecount = titlecount + 1

    #�H�Wfor�j��]�w�ɮ׿�X
    
    rowData = fin.readline().rstrip('\n').split(',')    #�L�o���Y
    
    for rowData in fin:
        rowData = rowData.rstrip('\n').split(',')
        #Ū���@��ç@���
        if search(rowData[2]):
            continue
        #�ĥνu�ʷj�M �Y���O�ؼд��ꪽ�����L
        if rowData[2] == 'O3':
            value = rowData[3:27]
            times = 24
        else:
            value = rowData[8:13]
            times = 5
        #���o����A����ɶ�6~10�I
        clearCount = 0
        for clearValue in value:
            if clearValue == '' or not clearValue[-1].isdigit():
                value[clearCount] = 0
            
            clearCount = clearCount + 1
        
        value[:] = [float(x) for x in value]
        value.sort()
        f[searchOutputCsv(rowData[2])].write(rowData[0]+','+str(value[-1])+'\n');
        #��X�榡 (���/��)
    fin.close()
    for closeCsv in range(0,3):
        f[closeCsv].close()
    #�����ɮ�
