package it.polito.tdp.alien;

import java.net.URL;
import java.util.*;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class FXMLController {
	
	AlienDictionary dizionario = new AlienDictionary();

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private TextField inserting;

    @FXML
    private TextArea textArea;

    @FXML
    void doReset(ActionEvent event) {
    	textArea.setText("Welcome to Alien Dictionary v2020");
    	dizionario.getParole().clear();
    	inserting.clear();
    }

    @FXML
    void doTranslate(ActionEvent event) {
    	String alienWord;
    	String translation;
    	if (inserting.getText().length() == 0) {
    		textArea.appendText("\nNon è stata inserita nessuna parola.");
    		return;
    	}
    	if (inserting.getText().contains(" ")) {
    		int i;
    		char[] c = inserting.getText().toCharArray();
    		for (i=0; i<inserting.getText().length(); i++)
    			if (c[i] == ' ')
    				break;
    		if (i==0 || i==inserting.getText().length()-1) {
    			textArea.appendText("\nErrore di inserimento.");
    			return;
    		}
    		alienWord = inserting.getText().substring(0, i);
    		translation = inserting.getText().substring(i+1, inserting.getText().length());
    		dizionario.addWord(alienWord, translation);
    	}
    	else {
    		if (dizionario.translateWord(inserting.getText()) != null) {
    			textArea.appendText("\n" + dizionario.translateWord(inserting.getText()));
    		}
    		else
    			textArea.appendText("\nLa parola inserita non è ancora stata decifrata.");
    	}
    		
    }

    @FXML
    void initialize() {
        assert inserting != null : "fx:id=\"inserting\" was not injected: check your FXML file 'Scene.fxml'.";
        assert textArea != null : "fx:id=\"textArea\" was not injected: check your FXML file 'Scene.fxml'.";

    }
}