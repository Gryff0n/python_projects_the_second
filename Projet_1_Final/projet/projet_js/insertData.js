function validate() {

    if (document.getElementById('last_name').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer le nom du nouveau contact !";
        return false;
    }
    if (document.getElementById('first_name').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer le prénom du nouveau contact !";
        return false;
    }
    if (document.getElementById('birth_date').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer la date de naissance du nouveau contact !";
        return false;
    }
    if (document.getElementById('work').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer la profession du nouveau contact !";
        return false;
    } 
    //condition de verifiction du numero de telephone fixe
    if (document.getElementById('telfixe').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer le numéro de téléphone fixe du nouveau contact !";
        return false;
    }
    if (document.getElementById('telfixe').value.length != 10 ){
        document.getElementById("alert").innerHTML ="Veuillez entrer un numéro de fixe valide !";
        return false;
    }
    if (isNaN(document.getElementById('telfixe').value)){
        document.getElementById("alert").innerHTML ="Veuillez entrer un numéro fixe correct !";
        return false;
    }
    //condition de verifiction du numero de telephone
    if (document.getElementById('tel').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer le numéro de téléphone portable du nouveau contact !";
        return false;
    }
    if (document.getElementById('tel').value.length != 10 ){
        document.getElementById("alert").innerHTML ="Veuillez entrer un numéro de portable valide !";
        return false;
    }
    if (isNaN(document.getElementById('tel').value)){
        document.getElementById("alert").innerHTML ="Veuillez entrez un numéro portable correct !";
        return false;
    }
        //verification si les champs sont nul ou pas 
    if (document.getElementById('adress').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer l'adresse du nouveau contact !";
        return false;
    }
    if (document.getElementById('mail').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer l'e-mail du nouveau contact !", document.getElementById('tel').value.length;
        return false;
    }
    
}