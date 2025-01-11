import numpy as np
import matplotlib.pyplot as plt

ani = [1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 ]
rata_inflatie = [0.0, 0.7, 1.1, 0.2, 0.6, 0.6, 1.6, 2.0, 2.1, 3.1, 17.8, 4.1, 1.1, 0.8, 1.0, 0.9, 2.2, 1.1, 5.1, 170.2, 210.4, 256.1, 136.7, 32.3, 38.8, 154.8, 59.1, 45.8, 45.7, 34.5, 22.5, 15.3, 11.9, 9.0, 6.6, 4.8, 7.9, 5.6, 6.1, 5.8, 3.3, 4.0, 1.1, -0.6, -1.5, 1.3, 4.6, 3.8, 2.6, 5.1, 13.8, 10.4 ]

medie_inflatie = np.mean(rata_inflatie)
deviatia_standard = np.std(rata_inflatie)

suma_economisita = 100
peste_ani = 5
numar_simulari = 100_000

# pentru simularea inflatiei este folosita distributia normala (gaussiana)
# vezi documentatie https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html
# sau in cartea `Probability and Statistics for Computer Scientists` p.90
# sau cursul de la facultate (8 sau 9)
simulare_inflatie = np.random.normal(medie_inflatie, deviatia_standard, size = (numar_simulari, peste_ani))
simulare_inflatie = np.clip(simulare_inflatie, 0, None)

# vreau un array doar cu `suma_economisita`
values = np.full([], suma_economisita, dtype=np.float64)
for i in range(peste_ani):
    # puterea de cumparare la timpul t este dat de: P(t) = suma_economisita / (1+i_1) * (1+i_2) * ... * (1 + i_n)
    # i_n = rata inflatiei pentru anul n
    values = values / (1 + simulare_inflatie[:, i] / 100)

medie_viitor = np.mean(values)
deviatie_viitor = np.std(values)

print(f'Peste {peste_ani} ani, {suma_economisita} lei vor insemna {round(medie_viitor, 2)} lei (± {round(deviatie_viitor, 2)} lei)')

plt.figure(figsize=(10, 6))
plt.hist(values, bins=50, edgecolor='black', alpha=0.75, color = 'paleturquoise', label='Distribuția valorii economiilor')
plt.axvline(medie_viitor, color='red', linestyle='dashed', linewidth=2, label=f'Media: {medie_viitor:.2f} lei')
plt.axvline(medie_viitor - deviatie_viitor, color='midnightblue', linestyle='dotted', linewidth=2, label=f'-1σ: {medie_viitor - deviatie_viitor:.2f} lei')
plt.axvline(medie_viitor + deviatie_viitor, color='midnightblue', linestyle='dotted', linewidth=2, label=f'+1σ: {medie_viitor + deviatie_viitor:.2f} lei')
plt.xticks(np.arange(0, 101, 5))
plt.title('Distribuția valorii viitoare a economiilor', fontsize=14)
plt.xlabel('Valoarea reală (lei)', fontsize=12)
plt.ylabel('Frecvența', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(ani, rata_inflatie, marker='o', linestyle='-', color='navy', label='Rata inflației (%)')
plt.axhline(medie_inflatie, color='red', linestyle='dashed', linewidth=1.5, label=f'Media istorică: {medie_inflatie:.2f}%')
plt.fill_between(ani, medie_inflatie - deviatia_standard, medie_inflatie + deviatia_standard, color='gray', alpha=0.2, label='±1σ')
plt.title('Evoluția ratei inflației în timp', fontsize=14)
plt.xlabel('Ani', fontsize=12)
plt.ylabel('Rata inflației (%)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()