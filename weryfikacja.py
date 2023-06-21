import rsa

def gui_szyfrowanie_RSA():
    import PySimpleGUI as sg
    uklad = [[sg.Text("Wpisz nazwę pliku do sprawdzenia:")],
             [sg.Input(key="dane")],
             [sg.Text("Wpisz nazwę pliku zawierającego Twój klucz publiczny:")],
             [sg.Input(key="klucz_publiczny")],
             [sg.Text("Wpisz nazwę pliku z podpisem:")],
             [sg.Input(key="sygnatura")],
             [sg.Text("Informacja:", size=(50))],
             [sg.MLine(size=(40,8), key='-MSG-')],
             [sg.Button('Wykonaj'), sg.Exit()]]
    okno = sg.Window("Weryfikacja RSA", uklad)

    while True:
        event, values = okno.read()

        if event == 'Exit' or event is None:
            break
        if event == 'Wykonaj':
          
            plik = values["dane"]
            with open(plik, "rb") as f:
                zawartosc = f.read() 

            klucz_plik = values["klucz_publiczny"]
            with open(klucz_plik, "rb") as f:
                klucz = rsa.PublicKey.load_pkcs1(f.read())

            sign_plik = values["sygnatura"]
            with open(sign_plik, "rb") as f:
                signature = f.read()

        try:
            rsa.verify(zawartosc, signature, klucz)
            odp = "Weryfikacja przebigła pomyślnie"
        except rsa.VerificationError:
            odp = "Weryfikacja nie powiodła się"
            
                
        okno["-MSG-"].update(odp)
    okno.close()
gui_szyfrowanie_RSA()