import translator as tr
import dictionary

parole = dict()
d = dictionary.Dictionary(parole)
t = tr.Translator(d)


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()
    # Add input control here!
    while not (txtIn == "1" or txtIn == "2" or txtIn == "3" or txtIn == "4"):
        print("\nNon è stato digitato nessuno dei numeri previsti dal menù. Riprovare:")
        txtIn = input()

    if int(txtIn) == 1:
        print("\nAggiungi una o più traduzioni, scrivendo per prima la parola da tradurre.")
        print("Le parole vanno separate con uno spazio e si possono aggiungere al massimo tre traduzioni.")
        print("Sono ammessi solo caratteri alfabetici.")
        txtIn = input()
        while(True):
            counter = 0
            flag = 0
            while counter<len(txtIn)-1:
                if txtIn[counter].isspace() and txtIn[counter+1].isspace():
                    flag = 1
                    break
                counter += 1
            if flag == 1:
                print("Sono stati inseriti almeno due spazi consecutivi. Operazione fallita.\n")
                break
            if txtIn[0] == " " or txtIn[len(txtIn)-1] == " ":
                print("È stato inserito uno spazio all'inizio o alla fine del testo inserito. Operazione fallita.\n")
                break
            testo = txtIn.split()
            if len(testo) < 2:
                print("Non è stata inserita nemmeno una traduzione. Operazione fallita.\n")
                break
            if len(testo) > 4:
                print("Sono state inserite troppe parole. Operazione fallita.\n")
                break
            for g in testo:
                if not g.isalpha():
                    flag = 1
            if flag == 1:
                print ("È stato inserito almeno un carattere non alfabetico. Operazione fallita.\n")
                break
            i=1
            while (i < len(testo)):
                j=1
                while (j < len(testo)):
                    if i != j and testo[i] == testo[j]:
                        flag = 1
                    j += 1
                i += 1
            """
            Il codice qui sotto riportato per adempiere al compito del doppio ciclo while annidato scritto sopra
            non è valido, in quanto il metodo index restituisce il minimo valore di indice in cui viene
            trovata una determinata stringa
            
            for g in testo:
                for h in testo:
                    if (testo.index(g) != testo.index(h)) and g == h:
                        flag = 1
            """
            if flag == 1:
                print("Una stessa traduzione è stata inserita due volte. Operazione fallita.\n")
                break
            tupla = (txtIn.split(" ", 1)[0], txtIn.split(" ", 1)[1])
            t.handleAdd(tupla)
            break

    elif int(txtIn) == 2:
        print("\nInserire la parola da cercare:")
        t.handleTranslate(input())
    elif int(txtIn) == 3:
        print("\nLa ricerca con Wild Card consente di usare un punto interrogativo in sostituzione di un carattere all'interno della parola.")
        print("Inserire la parola da cercare con Wild Card:")
        t.handleWildCard(input())
    elif int(txtIn) == 4:
        break
