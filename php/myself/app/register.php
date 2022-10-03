<?php
    require_once 'route.php';

    $RouteRegister = new RouteRegister(['title' => 'Register']);
    if(!$RouteRegister->isLogged()){
        if($_SERVER['REQUEST_METHOD'] === 'POST'){
            $RouteRegister->post('auth');
        }
        $RouteRegister-> get('auth');
        die();
    }
    header("Location: $RouteRegister->baseUrl/home.php");
?>