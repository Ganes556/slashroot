<?php 
    require_once 'route.php';
    $RouteHome = new RouteHome(['title'=>'Home']);
    if($RouteHome->isLogged()){
        $RouteHome->get('home');
        die();
    }
    header("Location: $RouteHome->baseUrl/login.php");
?>