
import sys
'''
print(s.platform)
print(s.maxsize)
'''
#for i in s.path:
#    print(i)
'''

#載入geometry

import geometry.point #載入模組，並且載入裡面的封包
result = geometry.point.distance(1,1,5,5) #載入模組裡面的封包，然後再存取裡面的def函式
print(result)

result = geometry.slope(1, 1, 3, 3)
print(result)

#調整搜尋模組的路徑
for i in s.path:
    print(i)

#找不到module，因為把geometry移到modele file裡面，我們的path還沒更改。
#如何新增Path?
'''
sys.path.append("C:\\Users\\ted\\Desktop\\程式練習\\Python\\module") #可以相對路徑也可以絕對路徑 

#絕對路徑記得要多加一個「\」

for i in sys.path:
    print(i)

import geometry
result=geometry.distance(1,1,5,5)
print(result)