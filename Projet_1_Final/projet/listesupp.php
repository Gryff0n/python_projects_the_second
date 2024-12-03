<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="project_css/default.css"/>
        <link rel="icon" type="image/x-icon" href="icon.ico">
        <script src="projet_js/suppData.js"></script>
        <action="suppData.php" method="POST"></action>
        <title>Hermes</title>
    </head>
        <body>
            <header>
                <div class="topnav">
                    <a class="active" href="index.php">Accueil</a>
                    <a href="sub.php">ajouter un contact</a>
                    <a href="liste.php">répertoire</a>
                </div>
                <br>
                <center><h2>Voici la liste de tous vos contacts et leurs informations :</h2><center>
                <br>
                <div class="redirection">
                    <center>
                        <font color=#ffffff>
                        <a href="listesupp.php">Supprimer</a>
                        <a href="contact_list_by_attribut.php">Lister par critères</a>
                        <a href="edit.php">Modifier</a>
                    <center>
                </div>
                <br>
                <div id="form">
            <form action="projet_php/suppData.php" method="POST" name="info" onsubmit="return valisupp()">
                <tr>

                <label for="supp">Numéro de téléphone portable du contact a supprimer : </label>
                <input type="text" id="supp" name="supp"/>

                </tr><br/><br/>

                <input type="submit" value="supprimer" onclick=valisupp()>

                <font color=#ff0000>
                    <p id="alert"></p>
                </font>

            </form>
            </div>
                <br>
            </header>
            <div id="liste">                   
                <?php include "./projet_php/AllData.php" //cherche la code php qui affiche la base de donnes dans le fichier AllData.php?>
            </div>
        </body>
    </div>
</html>