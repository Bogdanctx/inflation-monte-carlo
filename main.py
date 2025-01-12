import numpy as np
import matplotlib.pyplot as plt

PERIOADA_EXPERIMENT = 5 # 5 ani

class Inflation:
    def __init__(self, ani, rata_inflatie, suma_economisita, numar_simulari = 100_000):
        self.ani = ani
        self.rata_inflatie = rata_inflatie
        self.numar_simulari = numar_simulari
        self.suma_economisita = suma_economisita

        self.medie_inflatie = np.mean(self.rata_inflatie)
        self.deviatia_standard = np.std(self.rata_inflatie)
        print(f'Media inflatiei in Romania (2000 -> 2023): {round(self.medie_inflatie, 2)}%')
        print(f'Deviatia standard a mediei (2000 -> 2023): ±{round(self.deviatia_standard, 2)}%')

        # generez o matrice cu perioada_experiment coloane si numar_simulari linii
        self.simulare_inflatie = np.random.normal(self.medie_inflatie, self.deviatia_standard, size=(numar_simulari, PERIOADA_EXPERIMENT))

    def compute(self, nivel_de_incredere = 0.95, marja_eroare = 0.02):
        # `suma_viitoare` = array de dimensiune `numar_simulari` cu valoarea `suma_economisita`
        suma_viitoare = np.full(self.numar_simulari, self.suma_economisita, dtype = np.float64)

        for i in range(PERIOADA_EXPERIMENT): # se aplica inflatia fiecarui an
            suma_viitoare = suma_viitoare / (1 + self.simulare_inflatie[:, i] / 100)

        medie_viitor = np.mean(suma_viitoare) # calculez media inflatiei peste cei 5 ani.
        deviatia_standard_viitor = np.std(suma_viitoare) # calculez deviatia standard a inflatiei din urmatorii 5 ani

        # chernoff-hoeffding
        # vezi cursul 11 "Q4: Pot imbunatati estimarile din Q2 si Q3?"
        numar_necesar_simulari = 2 * (marja_eroare ** 2)
        numar_necesar_simulari = np.log(2 / (1 - nivel_de_incredere)) / numar_necesar_simulari # ln(2 / (1-alpha)) / (2 * epsilon^2)

        print(f'Peste {PERIOADA_EXPERIMENT} ani, {self.suma_economisita} lei vor insemna {round(medie_viitor, 2)} lei (± {round(deviatia_standard_viitor, 2)} lei)')
        print(f'Pentru o eroare de ±{round(marja_eroare * 100, 2)}% cu nivelul de încredere {round(nivel_de_incredere * 100, 2)}%, sunt necesare cel putin {round(numar_necesar_simulari)} simulari')

    def plot(self):
        # Grafic 1: Evoluția ratei inflației în timp
        lower_bound = self.medie_inflatie - self.deviatia_standard
        upper_bound = self.medie_inflatie + self.deviatia_standard

        plt.figure(figsize=(10, 6))
        plt.plot(self.ani, self.rata_inflatie, marker='o', linestyle='-', color='navy', label='Rata inflației (%)')
        plt.axhline(self.medie_inflatie, color='red', linestyle='dashed', linewidth=1.5,
                    label=f'Media istorică: {round(self.medie_inflatie, 2)}%')
        plt.fill_between(self.ani, lower_bound, upper_bound, color='gray', alpha=0.2,
                         label=f'Deviatia σ: {round(self.deviatia_standard, 2)}%')
        plt.title('Evoluția ratei inflației în timp', fontsize=14)
        plt.xlabel('Ani', fontsize=10)
        plt.ylabel('Rata inflației (%)', fontsize=12)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

        # Grafic 2: Distribuția simulărilor inflației
        medie_simulari = np.mean(self.simulare_inflatie)
        std_simulari = np.std(self.simulare_inflatie)
        lower_bound = medie_simulari - std_simulari
        upper_bound = medie_simulari + std_simulari

        plt.figure(figsize=(10, 6))
        plt.hist(self.simulare_inflatie.flatten(), bins=100, color='skyblue', edgecolor='black', alpha=0.7,
                 density=True)
        plt.axvline(medie_simulari, color='red', linestyle='dashed', linewidth=1.5,
                    label=f'Medie inflatie: {medie_simulari:.2f}%')
        plt.axvline(lower_bound, color='orange', linestyle='dashed', linewidth=1.2, label=f'Derivatia (σ): {round(std_simulari, 2)}%')
        plt.axvline(upper_bound, color='orange', linestyle='dashed', linewidth=1.2)
        plt.title('Distribuția simulărilor inflației', fontsize=14)
        plt.xlabel('Rata inflației simulate (%)', fontsize=10)
        plt.ylabel('Densitate', fontsize=12)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()


ani = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
rata_inflatie = [45.7, 34.5, 22.5, 15.3, 11.9, 9.0, 6.6, 4.8, 7.9, 5.6, 6.1, 5.8, 3.3, 4.0, 1.1, -0.6, -1.5, 1.3, 4.6, 3.8, 2.6, 5.1, 13.8, 10.4]

inflatie = Inflation(ani, rata_inflatie, 100, 4611)
inflatie.compute()
inflatie.plot()
