<?php
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
?>
<font color=#ffffff>
<center>
    <table>
        <thead>
            <tr>
                <th>Nom</th>
                <th>Prénom </th>
                <th>Date de naissance</th>
                <th>Adresse</th>
                <th>Mail</th>
                <th>Profession</th>
                <th>Numéro portable</th>
                <th>Numéro fixe</th>
            </tr>   
        </thead>
        <tbody>              
            <?php 
            $result = $connection->query("SELECT * FROM contact");
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
