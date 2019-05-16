
# Otetaan käyttäjältä muutama numero talteen laskutoimitusta varten

numero1 = ""
numero2 = ""
eka_input = ""
toka_input = ""
choise = ""

while True:
    print ("Anna kaksi numeroa, q lopettaa")
    eka_input = input ("Anna numero ")
    if (eka_input == "q"):
        break
    else:
         numero1 = eka_input

    toka_input = input("Anna toinen numero ")
    if (toka_input == "q"):
        break
    else:
        numero2 = toka_input

print (numero1)
print (numero2)

# Tässä tehdään python scripti joka myöhemmin ajetaan slavella

scripti =  "f= open(\"tulokset\",\"w+\")\ntulos = (" + numero1 + " + " + numero2 + ")\nf.write(str (tulos))\nf.close()"

f= open("job.py","w+")
f.write(scripti)
f.close()

# Siirretään salt-statella tiedosto minionille ja ajetaan scripti

import os
command = "sudo salt \'worker-slave\' state.apply givejob"
os.system(command)
