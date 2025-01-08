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