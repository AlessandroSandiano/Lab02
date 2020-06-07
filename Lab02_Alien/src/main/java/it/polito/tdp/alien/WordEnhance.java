package it.polito.tdp.alien;

import java.util.*;

public class WordEnhance {
	
	private String alienWord;
	private List<String> translations = new LinkedList<>();
	
	
	
	public WordEnhance(String alienWord) {
		this.alienWord = alienWord;
	}



	public WordEnhance(String alienWord, List<String> translations) {
		this.alienWord = alienWord;
		this.translations = translations;
	}



	@Override
	public boolean equals(Object obj) {
		WordEnhance w = (WordEnhance) obj;
		if (alienWord.toLowerCase().compareTo(w.getAlienWord().toLowerCase()) == 0)
			return true;
		return false;
	}
	
	public boolean traduzioneGiaPresente(String s) {
		for (String st: translations)
			if (s.toLowerCase().compareTo(st.toLowerCase()) == 0)
				return true;
		return false;
	}



	public String getAlienWord() {
		return alienWord;
	}



	public List<String> getTranslations() {
		return translations;
	}



	@Override
	public String toString() {
		String s = "";
		if (translations.size() > 0) {
			for (int i=0; i<translations.size()-1; i++)
				s += translations.get(i) +", ";
			s += translations.get(translations.size()-1);
		}
		return s;
	}
	
	

}
