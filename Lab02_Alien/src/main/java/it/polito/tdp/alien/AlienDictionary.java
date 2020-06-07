package it.polito.tdp.alien;

import java.util.*;

public class AlienDictionary {
	
	private List<Word> parole = new LinkedList<>();
	
	public void addWord(String alienWord, String translation) {
		Word word = new Word(alienWord, translation);
		if (parole.size() > 0) {
			Iterator<Word> iteratore = parole.iterator();
			do {
				Word w = iteratore.next();
				if (w.equals(word))
					iteratore.remove();
			} while (iteratore.hasNext());
		}
		parole.add(word);
	}
	
	public String translateWord (String alienWord) {
		Word word = new Word(alienWord);
		for (Word w: parole)
			if (w.equals(word))
				return w.getTranslation();
		return null;
	}

	public List<Word> getParole() {
		return parole;
	}
	
}
