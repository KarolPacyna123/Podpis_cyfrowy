import rsa
import hashlib

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

def gui_szyfrowanie_RSA():
    import PySimpleGUI as sg
    uklad = [[sg.Text("Wpisz nazwę pliku do podpisania:")],
             [sg.Input(key="dane")],
             [sg.Text("Wpisz nazwę pliku zawierającego Twój klucz prywatny:")],
             [sg.Input(key="klucz_prywatny")],
             [sg.Text("Informacja:", size=(50))],
             [sg.MLine(size=(40,8), key='-MSG-')],
             [sg.Button('Wykonaj'), sg.Exit()]]
    okno = sg.Window("Podpis RSA", uklad)

    while True:
        event, values = okno.read()

        if event == 'Exit' or event is None:
            break
        if event == 'Wykonaj':
          
            plik = values["dane"]
            with open(plik, "rb") as f:
                zawartosc = f.read() 

            klucz_plik = values["klucz_prywatny"]
            with open(klucz_plik, "rb") as f:
                klucz = rsa.PrivateKey.load_pkcs1(f.read()) 

            sha256_hash = rsa.compute_hash(zawartosc, "SHA-256")
            
            signature = rsa.sign_hash(sha256_hash, klucz, "SHA-256")

            with open("signature", "wb") as f:
                f.write(signature)
            
            okno["-MSG-"].update("Wybrany przez Ciebie plik został podpisany")
    okno.close()
gui_szyfrowanie_RSA()