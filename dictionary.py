class Dictionary:
    def __init__(self, parole = {}):
        self.parole = parole

    def addWord(self, tupla):
        try:
            traduzioniEsistenti = self.parole.get(tupla[0].lower()).split()
            counter = 0
            for p in tupla[1].lower().split():
                if (not p in traduzioniEsistenti):
                    self.parole.update({tupla[0].lower():f"{self.parole.get(tupla[0].lower())[0:-1]} {p}\n"})
                    counter += 1
            file = open('dictionary.txt', 'w', encoding='utf-8')
            for key, value in self.parole.items():
                file.write(f"{key} {value}")
            file.close()
            if counter == 0:
                return 0
            elif counter == 1:
                return 1
            else:
                return counter
        except:
            #metodo della classe predefinita Dictionary equivalente ad "update"
            self.parole[tupla[0].lower()] = f"{tupla[1].lower()}\n"
            file = open('dictionary.txt', 'w', encoding='utf-8')
            for key, value in self.parole.items():
                file.write(f"{key} {value}")
            file.close()
            return -1

    def translate(self, termine):
        return self.parole.get(termine.lower())

    def translateWordWildCard(self, termine):
        if termine.count("?")!=1:
            return 0
        paroleTrovate = []
        for p in self.parole.keys():
            if len(termine) == len(p):
                if termine.lower()[0:termine.find("?")] == p[0:termine.find("?")] and termine.lower()[termine.find("?")+1:len(termine)] == p[termine.find("?")+1:len(termine)]:
                    paroleTrovate.append(f"Parola trovata: {p} = {self.parole.get(p)}")
        return paroleTrovate