<?php 
    session_start();
    if(isset($_SESSION['username']) && $_SESSION['username'] != ''){
        header("Location: http://localhost/Latihan/OOP-php/myself/home.php");
        die();
    }
    header("Location: http://localhost/Latihan/OOP-php/myself/login.php");
?>