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
		List<String> l = new LinkedList<>();
		int n=0, i;
		char[] c = alienWord.toCharArray();
		for (i=0; i<alienWord.length(); i++)
			if (c[i] == '?')
				n++;
		if (n > 1)
			throw new IllegalStateException("È stato inserito più di un punto interrogativo!");
		if (n == 1) {
			for (i=0; i<alienWord.length(); i++)
				if (c[i] == '?')
					break;
			if (i == 0) {
				for (WordEnhance w: parole) {
					String w1 = w.getAlienWord().subSequence(1, alienWord.length()).toString();
					if ((w1.compareTo(alienWord.subSequence(1, alienWord.length()).toString()) == 0))
						l.addAll(w.getTranslations());
				}
				return l;
			}
			if (i == alienWord.length()-1) {
				for (WordEnhance w: parole) {
					String w1 = w.getAlienWord().subSequence(0, alienWord.length()-1).toString();
					if ((w1.compareTo(alienWord.subSequence(0, alienWord.length()-1).toString()) == 0))
						l.addAll(w.getTranslations());
				}
				return l;
			}
			for (WordEnhance w: parole) {
				String w1 = w.getAlienWord().subSequence(0, i).toString();
				String w2 = w.getAlienWord().subSequence(i+1, alienWord.length()).toString();
				if ((w1.compareTo(alienWord.subSequence(0, i).toString()) == 0) && (w2.compareTo(alienWord.subSequence(i+1, alienWord.length()).toString()) == 0))
					l.addAll(w.getTranslations());
			}
			return l;
		}
		for (WordEnhance w: parole)
			if (w.equals(word))
				return w.getTranslations();
		return null;
	}

	public List<WordEnhance> getParole() {
		return parole;
	}
	
}
