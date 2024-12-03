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
?>
<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="project_css/default.css"/>
        <link rel="icon" type="image/x-icon" href="icon.ico">
        <script src="projet_js/editData.js"></script>
        <title>Hermès</title>
    </head>
        <body>
            <header>
                <div class="topnav">
                    <a class="active" href="index.php">Accueil</a>
                    <a href="sub.php">ajouter un contact</a>
                    <a href="liste.php">répertoire</a>
                </div>
            </header>
            <br>
            <center><h2>Voici la liste de tous vos contacts et leurs informations :</h2><center>
            <br>
            <div class="redirection">
                    <center>
                        <font color=#ffffff>
                        <a href="listesupp.php">Supprimer</a>
                        <a href="contact_list_by_attribut.php">Lister par critère</a>
                        <a href="edit.php">Modifier</a>
                    <center>
                </div>
                <br>
                <br>
            <center>
            <form action="./projet_php/editing.php" method="POST" onsubmit="return validate()">

                <label for='numero_contact'>Numéro du contact à éditer : </label>
                <input type='text' id='numero_contact' name='numero_contact'/>

                <br><br>

                <label for="infos">infos : </label>
                <select name="infos" id="infos">
                    <option value="numero_portable">Numéro portable</option>
                    <option value="numero_fixe">Numéro fixe</option>
                    <option value="profession">Profession</option>
                    <option value="adresse">Adresse</option>
                    <option value="mail">Adresse mail</option>
                    <option value="birthday">date de naissance</option>
                    <option value="nom">Nom</option>
                    <option value="prenom">Prénom</option>
                </select>
                <input type='text' id="edited_information" name="edited_information">
                <input type="submit" value="Valider" onclick=validate() />
                <div class="alert">
                <font color=#ff0000>
                <p id="alert"></p>
                </font>
            </div>
            </form>
            <br>
            <?php
            ?>
            <center>
            <br>
            <?php include "./projet_php/AllData.php"?>
        </body>
    </div>
</html>