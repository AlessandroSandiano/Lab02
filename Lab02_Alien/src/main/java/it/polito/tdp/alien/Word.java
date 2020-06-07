package it.polito.tdp.alien;



public class Word {
	
	private String alienWord;
	private String translation = new String();
	
	
	
	public Word(String alienWord) {
		this.alienWord = alienWord;
	}



	public Word(String alienWord, String translation) {
		this.alienWord = alienWord;
		this.translation = translation;
	}



	@Override
	public boolean equals(Object obj) {
		Word w = (Word) obj;
		if (alienWord.toLowerCase().compareTo(w.getAlienWord().toLowerCase()) == 0)
			return true;
		return false;
	}



	public String getAlienWord() {
		return alienWord;
	}


	public String getTranslation() {
		return translation;
	}
	

}
