import matplotlib.pyplot as plt
import numpy as np

# 3D 그래프를 그리기 위해 필요한 모듈
from mpl_toolkits.mplot3d import Axes3D

# 3차원 공간에서 일정한 간격으로 점을 생성
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
z = np.arange(-5, 5, 0.5)

# meshgrid를 이용해 좌표 생성
X, Y, Z = np.meshgrid(x, y, z)

# 3D 가우시안 분포를 계산하기 위한 함수
def gaussian_3d(x, y, z, mu=0, sigma=1):
    return 1 - np.exp(-((x - mu)**2 + (y - mu)**2 + (z - mu)**2) / (2 * sigma**2))

# 가우시안 블롭 생성
blob = gaussian_3d(X, Y, Z)

# 투명도를 가우시안 분포 값에 따라 설정
#alpha = blob / blob.max()

# 그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 가우시안 블롭 시각화
scatter = ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=blob.flatten(), alpha=0.5)

# 그래프 제목 및 축 레이블 설정
ax.set_title('3D Gaussian Blob')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 그래프 축 범위 설정
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# 그래프 표시
plt.show()

