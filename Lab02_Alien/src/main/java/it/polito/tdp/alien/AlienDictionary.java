package it.polito.tdp.alien;

import java.util.*;

public class AlienDictionary {
	
	private List<WordEnhance> parole = new LinkedList<>();
	
	public void addWord(String alienWord, String translation) {
		List<String> l = new LinkedList<>();
		l.add(translation);
		WordEnhance word = new WordEnhance(alienWord, l);
		for (WordEnhance w: parole)
			if (w.equals(word))
					if (w.traduzioneGiaPresente(translation))
						return;
					else {
						w.getTranslations().add(translation);
						return;
					}
		parole.add(word);
	}
	
	public List<String> translateWord (String alienWord) {
		WordEnhance word = new WordEnhance(alienWord);
		for (WordEnhance w: parole)
			if (w.equals(word))
				return w.getTranslations();
		return null;
	}

	public List<WordEnhance> getParole() {
		return parole;
	}
	
}
