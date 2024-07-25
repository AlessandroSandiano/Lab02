import dictionary
class Translator:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def printMenu(self):
        print("______________________________\n" +
              "   Translator Alien-Italian\n"+
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n"+
              "______________________________\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        file = open (dict, 'r', encoding="utf-8")
        righe = file.readlines()
        parole = {}
        for r in righe:
            parole.update({r.split(" ", 1)[0]: r.split(" ", 1)[1]})
        self.dictionary.parole = parole
        file.close()

    def printDictionary(self, dict):
        for key, value in self.dictionary.parole.items():
            print(key, value, end = "")
        #print(f"{key} {value}" for key, value in self.dictionary.parole.items()) NON STAMPA IL DIZIONARIO

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        int = self.dictionary.addWord(entry)
        if int == 0:
            print("La parola e tutte le traduzioni inserite erano già presenti nel dizionario.\n")
        elif int == 1:
            print("È stata aggiunta una traduzione a questa parola, la quale era già presente nel dizionario.\n")
        elif int == -1:
            print("È stata aggiunta una nuova parola al dizionario con la/e relativa/e traduzione/i.\n")
        else:
            print(f"Sono state aggiunte {int} traduzioni a questa parola, la quale era già presente nel dizionario.\n")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        r = self.dictionary.translate(query)
        if r == None:
            print("La parola cercata non è presente nel dizionario.\n")
        else:
            print(self.dictionary.translate(query))


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        t = self.dictionary.translateWordWildCard(query)
        if type(t) is int:
            print("Il numero di punti interrogativi inseriti è diverso da 1. Operazione fallita.\n")
        else:
            for p in t:
                print(p)