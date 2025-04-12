'''
Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
• zapytaj użytkownika o wzrost i wagę,
• stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
• stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
otyłość) na podstawie wskaźnika BMI,
• zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.
'''

print("Obliczanie wskaznika BMI")

weight_in_kg=float(input("Jaką masz wagę (kg): "))
hight_in_cm=float(input("Podaj swój wzrost (cm): "))

def calculate_bmi(weight_in_kg,hight_in_cm):
    return weight_in_kg/hight_in_cm **2

def determine_bmi_category(bmi):
    if bmi <18.5:
        return "niedowaga"
    elif bmi<25:
        return "waga prawidłowa"
    elif bmi<30:
        return "nadwaga"
    else:
        return "otyłość"

bmi=calculate_bmi(weight_in_kg, hight_in_cm * 0.01)
cathegory=determine_bmi_category(bmi)

print("Wskaznik BMI: ", round(bmi,2))
print("Kategoria: ",cathegory)