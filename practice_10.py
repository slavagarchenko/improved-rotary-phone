import numpy as np
import matplotlib.pyplot as plt

# 1. Параметры


def f(L, K): return np.sqrt(L*K)        # функция выпуска


Qs = [1.0, 1.5, 2.0]                    # уровни изоквант
PL, PK, C = 5, 10, 50                  # цены и бюджет

# 2. Сетка
L = np.linspace(0.1, 10, 200)
K = np.linspace(0.1, 10, 200)
LL, KK = np.meshgrid(L, K)
F = f(LL, KK)

# 3. Рисуем изокванты
plt.figure(figsize=(6, 6))
contours = plt.contour(LL, KK, F, levels=Qs, linestyles='-')
plt.clabel(contours, inline=True)

# 4. Рисуем изокосту
L_iso = np.array([0, C/PL])
K_iso = np.array([C/PK, 0])
plt.plot(L_iso, K_iso, label='Isocost')

# 5. Точки A и B (примерные)
L0, K0 = 4, (C - PL*4)/PK
plt.scatter([L0], [K0], color='black')
plt.text(L0, K0, ' A', va='bottom')

# Оптимум: решим MPL/PL = MPK/PK => K_opt = (PL/PK)*(MPL/MPK)*L_opt,
# в примере при f=L^0.5K^0.5 MPL/MPK = K/L => оптимум на линии K=L*PK/PL
L_opt = C/(PL + PK*(PK/PL))
K_opt = (PK/PL)*L_opt
plt.scatter([L_opt], [K_opt], color='black')
plt.text(L_opt, K_opt, ' B', va='bottom')

# 6. Оформление
plt.xlabel('L')
plt.ylabel('K')
plt.legend()
plt.title('Изокванты и изокоста')
plt.show()
