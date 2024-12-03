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
                        <font color=#fffffff>
                        <a href="listesupp.php">Supprimer</a>
                        <a href="contact_list_by_attribut.php">Lister par criteres</a>
                        <a href="edit.php">Modifier</a>
                    <center>
                </div>
            <br>
            <br>
            <center>
                <form action="" method="POST">
                    <label for="criteres">Criteres : </label>
                    <select name="criteres" id="crtieres">
                        <option value="prenom">Prenom par ordre alphabetique</option>
                        <option value="nom">Nom par ordre alphabetique</option>
                    </select>
                    <input type="submit" value="Valider" />
                </form>
            </center>
            <br>
            
            <?php if(isset($_POST['criteres']) && $_POST['criteres'] == 'nom'):?>
                <center>
                    <table>
                        <thead>
                            <tr>
                                <th>Nom</th>
                                <th>Prenom </th>
                                <th>Date de naissance</th>
                                <th>Adresse</th>
                                <th>Mail</th>
                                <th>Profession</th>
                                <th>Numero portable</th>
                                <th>Numero fixe</th>
                            </tr>   
                        </thead>
                        <tbody>              
                            <?php
                            //affiche la base de donnees trier par nom en oredre croissant 
                            $last_name = $_POST['criteres'];
                            $result = $connection->query("SELECT * FROM contact ORDER BY nom");
                            while($row = $result->fetch_assoc()):
                            ?>
                            <tr>
                                <td><?php echo htmlspecialchars($row['nom']); ?></td>
                                <td><?php echo htmlspecialchars($row['prenom']); ?></td>
                                <td><?php echo htmlspecialchars($row['birthday']); ?></td>
                                <td><?php echo htmlspecialchars($row['adresse']); ?></td>
                                <td><?php echo htmlspecialchars($row['mail']); ?></td>
                                <td><?php echo htmlspecialchars($row['profession']); ?></td>
                                <td><?php echo htmlspecialchars($row['numero_portable']); ?></td>
                                <td><?php echo htmlspecialchars($row['numero_fixe']); ?></td>
                            </tr>
                            <?php endwhile;?>
                        </tbody>
                    </table>
                </center>
            <?php endif;?>
            <?php if(isset($_POST['criteres']) && $_POST['criteres'] == 'prenom'):?>
                <center>
                    <table>
                        <thead>
                            <tr>
                                <th>Nom</th>
                                <th>Prenom </th>
                                <th>Date de naissance</th>
                                <th>Adresse</th>
                                <th>Mail</th>
                                <th>Profession</th>
                                <th>Numero portable</th>
                                <th>Numero fixe</th>
                            </tr>   
                        </thead>
                        <tbody>
                                          
                            <?php
                            // affiche la base de donnees trier par prenom en oredre croissant 
                            $last_name = $_POST['criteres'];
                            $result = $connection->query("SELECT * FROM contact ORDER BY prenom");
                            while($row = $result->fetch_assoc()):
                            ?>
                            <tr>
                                <td><?php echo htmlspecialchars($row['nom']); ?></td>
                                <td><?php echo htmlspecialchars($row['prenom']); ?></td>
                                <td><?php echo htmlspecialchars($row['birthday']); ?></td>
                                <td><?php echo htmlspecialchars($row['adresse']); ?></td>
                                <td><?php echo htmlspecialchars($row['mail']); ?></td>
                                <td><?php echo htmlspecialchars($row['profession']); ?></td>
                                <td><?php echo htmlspecialchars($row['numero_portable']); ?></td>
                                <td><?php echo htmlspecialchars($row['numero_fixe']); ?></td>
                            </tr>
                            <?php endwhile;?>
                        </tbody>
                    </table>
                </center>
            <?php endif;?>
        </body>
    </div>
</html>