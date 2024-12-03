<!DOCTYPE html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="project_css/default.css"/>
    <link rel="stylesheet" href="project_css/form.css"/>
    <link rel="icon" type="image/x-icon" href="icon.ico">
    <title>L'Aurora</title>
</head>
<action="Getinfos.php" method="POST"></action>
<script src="./projet_js/insertData.js"></script>
<body>
    <header>
        <div class="topnav">
            <a class="active" href="index.php">Accueil</a>
            <a href="sub.php">ajouter un contact</a>
            <a href="liste.php">répertoire</a>
        </div>
    </header>
    <br>
    <div id="form">
        <form action="./projet_php/insertData.php" method="POST" name="info" onsubmit="return validate()">
            <tr>
                <label for="last_name">Nom : </label>
                <input type="text" id="last_name" name="last_name"/>
            </tr><br/><br/>
            <tr>
                <label for="first_name">Prénom : </label>
                <input type="text"  id="first_name" name="first_name"/>
            </tr><br/><br/>
            <tr>
                <label for="birth_date">Date de naissance : </label>
                <input type="date" id="birth_date" name="birth_date"/>
            </tr><br/><br/>
            <tr>
                <label for="work">Profession : </label>
                <input type="text"  id="work" name="work"/>
            </tr><br/><br/>
            <tr>
                <label for="telfixe">Numéro de téléphone fixe :</label>
                <input type="text" id="telfixe" name="telfixe"/>
            </tr><br/><br/>
            <tr>
                <label for="tel">Numéro de téléphone portable :</label>
                <input type="text" id="tel" name="tel"/>
            </tr><br/><br/>
            <tr>
                <label for="adress">Adresse : </label>
                <input type="text" id="adress" name="adress"/>
            </tr><br/><br/>
            <tr>
                <label for="mail">Adresse mail : </label>
                <input type="email" id="mail" name="mail"/>
            </tr><br/><br/>
            <input type="submit" onclick=validate()>
            <div class="alert">
                <font color=#ff0000>
                <p id="alert"></p>
                </font>
            </div>
        </form>
    </div>
</body>
<?php
session_start();
$_SESSION['redirect'] = True;
?>
</html>