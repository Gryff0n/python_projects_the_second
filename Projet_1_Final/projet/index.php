<?php
session_start();
#etablissement de la connection avec la base de donnee
$servername = "localhost" ;
$username = "root" ;
$password= "" ; 
$name = "Repertoire" ;
$connection  = mysqli_connect($servername, $username, $password, $name);

if (!$connection) {
    $connectStatus = "Not Connected";
    die("connection Failed: ". mysqli_connect_error());
}
$connectStatus = "Connected";
#echo "Connected Sucessfully";
?>
<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="project_css/accueil.css"/>
        <link rel="icon" type="image/x-icon" href="icon.ico">
        <title>Hermès</title>
    </head>
        <body>
            <header>
                <div class="topnav">
                        <a class="active" href="index.php">Accueil</a>
                        <a href="sub.php">ajouter un contact</a>
                        <a href="liste.php">répertoire</a>
                </div>
                <div id="title">
                    <h1>Hermès</h1>
                    <p>Votre répertoire en ligne.</p>
                    <?php   
                        print_r("<br>");
                        #Affiche l'etat de la connection avec la base de donnees                        
                        printf("<center><font color=##eef5ed><strong>État de la connection avec la base de données : </strong></font>".
                            "<font color=#1bde0d0>".$connectStatus."</font><br></center><br>");
                        #Affiche un message si on essaye d'acceder a la page sub sans passer par le menu de navigation
                        #si pendant la redirection ily a eut une  erreur un  message ou
                        if(isset($_GET['AddCmsg'])) {
                            $message = "Utiliser le bouton 'ajouter contact' présent dans la barre de navigation ";
                            printf("<center><font color=#ff0000>".$message."</font><center>");
                            session_destroy();
                        #Affiche un message si la requette SQL c'est deroule sans erreur.
                        }
                        if (isset($_GET['Sucess'])) {
                            $Sucess = "Tout s'est bien passé, votre contact à été ajouter a votre repertoire";
                            printf("<center><font color=#1bde0d0>".$Sucess."</font><center>");
                            session_destroy();
                        }
                        if (isset($_GET['SucessSupp'])) {
                            $SucessSupp = "Tout s'est bien passe, le contact à été supprimer de la base de données";
                            printf("<center><font color=#1bde0d0>".$SucessSupp."</font><center>");
                            session_destroy();
                        }
                        if (isset($_GET['Error'])) {
                            $ERROR = "ERREUR, SUPPRESSION DU CONTACT IMPOSSIBLE.";
                            printf("<center><font color=#ff0000>".$ERROR."</font><center>");
                            session_destroy();
                        }
                        if (isset($_GET['SucessEdit'])) {
                            $SucessSupp = "Le contact à été modifier avec succès !";
                            printf("<center><font color=#1bde0d0>".$SucessSupp."</font><center>");
                            session_destroy();
                        }
                    ?>
                </div>
            </header>
        </body>
    </div>
</html>