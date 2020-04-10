import matplotlib.pyplot as plt

datumi = ['23.3.', '24.3.', '25.3.', '26.3.', '27.3.', '30.3.', '31.3.', '1.4.', '2.4.', '3.4.', '4.4.', '7.4.', '8.4.',
          '9.4.', '10.4.', '11.4.', '12.4.', '13.4.', '14.4.', '15.4.', '16.4.', '17.4.', '18.4.', '19.4.', '20.4.',
          '21.4.', '22.4.', '23.4.', '24.4.', '25.4.', '26.4.', '27.4.', '28.4.', '29.4.', '30.4.', '1.5.', '2.5.',
          '3.5.', '4.5.', '5.5.', '6.5.', '7.5.', '8.5.', '9.5.', '10.5.', '11.5.', '12.5.', '13.5.', '14.5.', '15.5.',
          '16.5.', '17.5.', '18.5.', '19.5.', '20.5.', '21.5.', '22.5.', '23.5.', '24.5.', '25.5.', '26.5.', '27.5.',
          '28.5.', '29.5.', '30.5.', '31.5.']
broj_novonez = [565, 784, 867, 951, 1140, 382, 1153, 1019, 1358, 1658, 1098, 1682, 1115, 867]
osn_broj_nez = 136071
broj_nez = [136071]

for i, num in enumerate(broj_novonez):
    if i >= 1:
        osn_broj_nez += num
        broj_nez.append(osn_broj_nez)

print(sum(broj_novonez))

diffs = []
broj_dana_real = len(broj_novonez)
broj_datuma = len(datumi)

for j in range(broj_dana_real):
    if j <= broj_dana_real - 2:
        old = broj_novonez[j]
        new = broj_novonez[j + 1]
        diff = new - old
        diffs.append(diff)

prosjek_novonezaposlenih = sum(diffs) / len(diffs)
print(f"Prosjek novonezaposlenih na dan: {prosjek_novonezaposlenih}")

for i in range(broj_datuma-1):
    last_value = broj_novonez[-1]
    new_value = last_value + prosjek_novonezaposlenih
    new_nez = broj_nez[-1] + new_value
    broj_novonez.append(int(new_value))
    broj_nez.append(int(new_nez))

print(broj_nez)
fig, (plot1, plot2) = plt.subplots(nrows=2, ncols=1)

plot1.bar(datumi[:40], broj_novonez[:40], label="Broj novonezaposlenih", color="green")
plot1.set_title("Broj novonezaposlenih s vremenom")

plot2.plot(datumi[:40], broj_nez[:40], label="Broj nezaposlenih", color="red")
#plot2.set_ylim(135000, 220000)
plot2.set_title("Broj nezaposlenih s vremenom")

plt.setp([plot1.get_xticklabels(), plot2.get_xticklabels()], rotation=60, ha="right")
fig.legend()
plt.xlabel("Vrijeme")
plt.show()