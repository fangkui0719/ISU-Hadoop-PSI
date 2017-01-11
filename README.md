Python版本: 3.4.1
原始資料來源: 空氣品質監測網
檔案格式:csv(以逗號隔開)

資料夾說明:
    原始資料-->PSI-Data-Original
    Python程式code-->PSI-Python-Code
    解析後資料-->PSI-Data-Processed
    
資料分析:
    原始資料仁武區-->測資14~17項-->目標測資(O3,NMHC,NOx)-->分析後整理(一日,一值)-->將O3,NOx,NMHC檔案合併成(日期)/(NOx/Nmhc)/(O3)格式

使用說明:
1.把原始資料歷年的仁武區域與python程式(兩個)放到同一個資料夾中
2.開啟仁武"解析"氣體.py並設定好年份range(91,105)(須先抓Python compiler)，之後會產生14*3個檔案(按年份計)(分別為NOx,NMHC,O3各14個)
3.開啟仁武"合併"氣體.py編譯即可得到(日期)/(NOx/Nmhc)/(O3)這個格式
4.參照WordCount的方式執行PSI.java，統計解析後資料

注意事項:
使用仁武"合併"氣體.py要跳過101年，這原始檔案有缺失造成(少一天NMHC數值)，改成range(91,101)和range(102,105)即可
