<?php
$servername = "localhost" ;
$username = "root" ;
$password= "" ;
$name = "Repertoire" ;
$connection  = mysqli_connect($servername, $username, $password, $name);

if (!$connection) {
    die("connection Failed: ". mysqli_connect_error());
}
//echo "Connected Sucessfully";
$cible = $_POST['numero_contact'];
if(isset($_POST['infos'])) {
    //modifie le  numero portable :
    if($_POST['infos'] == "numero_portable") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET numero_portable = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie le numero fixe 
    if($_POST['infos'] == "numero_fixe") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET numero_fixe = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie la profession
    if($_POST['infos'] == "profession") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET profession = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie la l'adresse  
    if($_POST['infos'] == "adresse") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET adresse = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    // nodifie le mail
    if($_POST['infos'] == "mail") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET mail = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie la date de naissance
    if($_POST['infos'] == "birthday") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET birthday = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie le nom
    if($_POST['infos'] == "nom") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET nom = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
    //modifie le prenom
    if($_POST['infos'] == "prenom") {
        $new_value = $_POST['edited_information'];
        $stmt = $connection -> prepare("UPDATE contact SET prenom = (?) WHERE numero_portable = (?)");
        #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
        $stmt->bind_param("ss",$new_value,$cible);
        $stmt->execute();

    }
        
}
header("Location: ../index.php?SucessEdit");
?>