class Dictionary:
    def __init__(self, parole):
        self.parole = parole

    def addWord(self, tupla):
        paroleInserite = [tupla[0].lower()]
        counter = 0
        while(counter<len(tupla[1].split())):
            paroleInserite.append(tupla[1].lower().split()[counter])
            counter += 1
        try:
            traduzioniEsistenti = self.parole.get(paroleInserite[0]).split()
            counter = 0
            for p in paroleInserite:
                if (not p in traduzioniEsistenti) and (paroleInserite.index(p)!=0 or paroleInserite.count(paroleInserite[0])>1):
                    self.parole.update({paroleInserite[0]:f"{self.parole.get(paroleInserite[0])[0:-1]} {p}\n"})
                    traduzioniEsistenti = self.parole.get(paroleInserite[0]).split()
                    counter += 1
            file = open('dictionary.txt', 'w', encoding='utf-8')
            for key, value in self.parole.items():
                file.write(f"{key} {value}")
            #[print(f"{key} {value}\n") for key, value in parole.items()]
            #l'istruzione di sopra è da testare sulla console
            file.close()
            if counter == 0:
                return 0
            elif counter == 1:
                return 1
            else:
                return counter
        except:
            stringUpdate = paroleInserite[1]
            if len(paroleInserite)>2:
                for p in paroleInserite:
                    if paroleInserite.index(p)>1:
                        stringUpdate += f" {p}"
            self.parole.update({paroleInserite[0]:f"{stringUpdate}\n"})
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