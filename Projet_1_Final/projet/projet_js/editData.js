function validate() {
    if(document.getElementById('infos').value == "numero_portable") {
        if(document.getElementById('edited_information') == "") {
            document.getElementById('alert').innerHTML = "Entrez un  numéro de telephone"; 
            return false ;

        }else if (isNaN(document.getElementById('edited_information').value)) { 
            document.getElementById('alert').innerHTML = "votre numéro de telephone doit être numérique";
            return false;

        }else if (document.getElementById('edited_information').value.lenght !=10 ) {
            document.getElementById('alert').innerHTML = "votre numéro de telephone doit contenir 10 chiffre";
            return false;
        }
    }
    if(document.getElementById('infos').value == "numero_fixe") {
        if (document.getElementById('edited_information') == "") {
            document.getElementById('alert').innerHTML = "Entrez un numéro de telephone"; 
            return false ;

        }else if (isNaN(document.getElementById('edited_information').value)) { 
            document.getElementById('alert').innerHTML = "votre numéro de telephone doit être numérique";
            return false;

        }else if (document.getElementById('edited_information').value.lenght !=10 ) {
            document.getElementById('alert').innerHTML = "votre numéro de telephone doit contenir 10 chiffre";
            return false;
        }
    }
    if((document.getElementById('infos').value == "profession") 
        || (document.getElementById('infos').value == "adresse") 
        || (document.getElementById('infos').value == "mail") 
        || (document.getElementById('infos').value == "birthday") 
        || (document.getElementById('infos').value == "nom") 
        || (document.getElementById('infos').value == "prenom")) {
  
        if(document.getElementById('edited_information').value == "") {
            document.getElementById('alert').innerHTML="Le champs est vide veuillez le remplir";
            return false;
        }

    }
} 