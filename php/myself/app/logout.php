<?php 
    require_once './route.php';
    $RouteLogout = new Route([]);
    $RouteLogout->logout();
    header("Location: $RouteLogout->baseUrl/login.php")
?>