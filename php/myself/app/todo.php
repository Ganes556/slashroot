<?php 
    require_once 'route.php';
    $RouteTodo = new RouteTodo(['title'=>'Todo']);
    if($RouteTodo->isLogged()){
        if($_SERVER['REQUEST_METHOD'] === 'POST') {
            $RouteTodo->post();
        }
        $RouteTodo->get('todo');
    }
    header("Location: $RouteTodo->baseUrl/login.php");
?>
