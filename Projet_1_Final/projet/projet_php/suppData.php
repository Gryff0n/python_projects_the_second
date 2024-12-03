<?php
session_start();

  $servername = "localhost" ;
  $username = "root" ;
  $password= "" ;
  $name = "Repertoire" ;
  $connection  = mysqli_connect($servername, $username, $password, $name);

  if (!$connection) {
      die("connection Failed: ". mysqli_connect_error());
  }
  echo "Connected Sucessfully";

  #sql query prepare  and bind :
  $stmt = $connection -> prepare("DELETE FROM contact WHERE numero_portable=?");

  $stmt->bind_param('s',$supp);

  $supp = $_POST["supp"];
  #execution de la commande
  $stmt->execute();
  #on la ferme
  $stmt -> close();
  header("Location: ../index.php?SucessSupp");

?>
