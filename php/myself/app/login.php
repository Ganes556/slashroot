<?php
    require_once 'route.php';

    $RouteLogin = new RouteLogin(['title'=>'Login']);
    if(!$RouteLogin->isLogged()) {
        if($_SERVER['REQUEST_METHOD'] === 'POST') {
            $RouteLogin->post('auth');
        }
        $RouteLogin->get('auth');
        die();
    }
    header("Location: $RouteLogin->baseUrl/home.php");
?>