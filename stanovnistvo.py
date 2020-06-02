import matplotlib.pyplot as plt

godine = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
          2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
          2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,
          2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040,
          2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050]

broj_stan = [4305494, 4305384, 4305725, 4310861, 4312487, 4313530, 4311967, 4309796, 4302847, 4289857,
             4275984, 4262140, 4246809, 4225316, 4190669, 4154213, 4105493, 4076246, 4050000]

razlike = []

for i, num in enumerate(broj_stan):
    if i == 0:
        osn = num
    else:
        raz = num - broj_stan[i - 1]
        razlike.append(raz)

diffs = []
broj_godina_real = len(broj_stan)
broj_godina = len(godine)

for j in range(broj_godina_real):
    if j < broj_godina_real - 2:
        old = razlike[j]
        new = razlike[j + 1]
        diff = new - old
        diffs.append(diff)

prosjek_stanovnika = int(sum(diffs) / len(diffs))
print(f"Prosjek novoodseljenih na godinu: {prosjek_stanovnika}")

for i in range(broj_godina - 1):
    print(f"Godina: {godine[i]} | {broj_stan[i]}")
    last_value = razlike[-1]
    new_value = last_value + prosjek_stanovnika
    new_nez = broj_stan[-1] + new_value
    razlike.append(int(new_value))
    broj_stan.append(int(new_nez))

print(razlike)
plt.bar(godine, broj_stan[:broj_godina])
plt.xlabel('Vrijeme')
plt.ylabel('Broj stanovnika u mil.')
plt.legend('Broj stanovnika')
plt.show()
