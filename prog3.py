u_in_number = input('Enter a number:')

try:
    float(u_in_number)
    print(abs(float(u_in_number)))
except:
    print('invalide getal, probeer het nogmaals')
