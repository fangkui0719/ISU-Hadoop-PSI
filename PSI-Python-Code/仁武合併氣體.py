# -*- coding: cp950 -*-
TestItem = ['NOx','NMHC','O3']
#�ؼЦX���ɮ�
"""
    �̫��X�榡
    (����ANOx/NMHC�AO3)
"""
for year in range(102,105):
    fin = []
    for Item in  TestItem:
        fin.append(open(str(year)+'�~���Z@'+Item+'.csv','r'))
    fout = open(str(year)+'�~���ZPSI.csv','w')
    fout.write('date'+','+'NOx/Nmhc'+','+'O3'+'\n')
    #�}�ҿ�J�ɮ�(3��)�]�m��X�ɮ�(1��)
    for nox in fin[0]:
        nox = nox.rstrip('\n').split(',')
        nmhc = fin[1].readline().rstrip('\n').split(',')
        o3 = fin[2].readline().rstrip('\n').split(',')

        #(�C�ӿ�J�ɮת��@��)
        if nox[1][-1].isdigit() and nmhc[1][-1].isdigit() and o3[1][-1].isdigit() and nmhc[1][-1] != '0':
            fout.write(str(nox[0])+','+str(float(nox[1])/float(nmhc[1]))+','+str(o3[1])+'\n')
        #�L�o�L�ĭ� ���ϤT���ɮפ��䤤���@�Ӭ��L�ĭȫh������X�ʧ@
    fin[0].close()
    fin[1].close()
    fin[2].close()
    fout.close()
    #�����ɮ�
