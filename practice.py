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