# 1
import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4, 5] # x 축 데이터 (예: 시간)
y = [10, 15, 13, 18, 20] # y 축 데이터 (예: 온도)

## 선 그래프 생성
plt.plot(x, y, marker='o', linestyle='-', color='b', label='temperature')
#marker: 데이터 점에 마커 표시
#linestyle: 선 스타일 (옵션)
#color : 선 색상 (옵션)
#label : 범례에 표시될 이름

## 그래프에 제목 추가
plt.title('Daily temperature trend')

# 축 레이블 추가
plt.xlabel('Time (hour)')
plt.ylabel('Temperature (C)')

# 범례 표시
plt.legend()

# 그래프 표시
plt.grid(True)
# plt.show()
plt.savefig("./results/linechart.png")

#2
import matplotlib.pyplot as plt

#데이터 생성
categories = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [25, 30, 15, 20, 35] # 각 카테고리에 대한 값 # 대응 안되면 그래프 안 만들어짐

# plot 초기화
plt.clf()

# 막대 그래프 생성
plt.bar(categories, values, color='skyblue') # 순서대로 X축, Y축, 옵션 지정

# 그래프 제목 추가
plt.title('Fruit Sales')

# 축 레이블 추가
plt.xlabel('Fruit')
plt.ylabel('Sales')

# 그래프 표시
# plt.show()
plt.savefig("./results/bar_chart.png")

#3
import matplotlib.pyplot as plt #matplotlib.pyplot 를 plt라고 부를게
import numpy as np #numpy 를 np 라고 부를게

# 데이터 생성 (랜덤 데이터 예시)
data = np.random.randn(1000) # 1000개의 랜덤 데이터 생성

# plot 초기화
plt.clf()

# 히스토그램 생성
plt.hist(data, bins = 20, color  = 'skyblue', edgecolor = 'black')

# 그래프에 제목 추가
plt.title('Histogram Chart')

# 축 레이블 추가
plt.xlabel('Values')
plt.ylabel('Frequency')

# 그래프 표시
# plt.show()
plt.savefig('./results/histogram.png')