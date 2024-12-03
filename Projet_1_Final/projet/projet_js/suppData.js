function valisupp() {

    if (document.getElementById('supp').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer le numéro de téléphone portable du contact a supprimer !";
        return false;
    }

    if (document.getElementById('supp').value.length != 10 ){
        document.getElementById("alert").innerHTML ="Veuillez entrer un numéro de portable valide !";
        return false;
    }

    if (isNaN(document.getElementById('supp').value)) { 
        document.getElementById('alert').innerHTML = "votre numéro de telephone doit être numérique";
        return false;

    }


}