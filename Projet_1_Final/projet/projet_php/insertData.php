<?php
session_start();
if (isset($_SESSION['redirect'])) {
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
  $stmt = $connection -> prepare("INSERT INTO contact (numero_portable,numero_fixe,birthday,adresse,mail,profession,nom,prenom) VALUES (?,?,?,?,?,?,?,?)");
  #on bind les parametre avec les variable php,en precisant leur type, i pour int et s pour string
  $stmt->bind_param("ssssssss",$tel,$telfixe,$birth,$adress,$mail,$profession,$name,$fname);

  #attribution des variables
  $name = $_POST["last_name"];
  $fname = $_POST["first_name"];
  $birth = $_POST["birth_date"];
  $adress = $_POST["adress"];
  $tel = $_POST["tel"];
  $telfixe = $_POST["telfixe"];
  $mail = $_POST["mail"];
  $profession = $_POST["work"];

  #execution de la commande
  $stmt->execute();
  #on la ferme
  $stmt -> close();
  header("Location: ../index.php?Sucess");
}else {
  header("Location: ../index.php?AddCmsg");
};
?>
