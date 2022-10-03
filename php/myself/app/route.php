<?php 
    require "vendor/autoload.php";
    require_once 'backend/actions.php';

    use eftec\bladeone\BladeOne;
    
    session_start();

    class Route {
        public $data;
        function __construct($data) {
            $views = __DIR__ . '/views';
            $cache = __DIR__ . '/cache';
            $this->data = $data;
            $this->blade = new BladeOne($views,$cache,BladeOne::MODE_DEBUG);
        }
        function __call($method,$args){
            if($method == 'logout'){
                session_destroy();
            }
        }
        function get($template){
            echo $this->blade->run($template, $this->data);
            unset($_SESSION['msg']);
            unset($_SESSION['error']);
        }
        public function isLogged(){
            return isset($_SESSION['username']) && !empty($_SESSION['username']);
        }
    }    

    class RouteTodo extends Route {
        function __construct($data){
            $this-> Todos = $Todos = new Todos();
            parent::__construct($data);
        }
        function post() {
            extract($_POST);
            if(isset($action) && !empty($action)){
                switch ($action) {
                    case 'add':
                        $this->Todos ->addTodo($todo,$date);
                        break;
                    case 'delete':
                        $this->Todos->deleteTodo($todoId);
                        break;
                    case 'update':
                        $this->Todos->updateTodo($todoId,$status,$dueDate,$todo);
                        break;
                    default:
                        break;
                }
            }
            die();
        }

        function get($template){
            $this->data['todos'] = $this->Todos->getTodos();            
            echo $this->blade->run($template, $this->data);
            unset($_SESSION['msg']);
            unset($_SESSION['error']);
            die();
        }
    }

    class RouteHome extends Route  {
        function __construct($data){
            parent::__construct($data);
        }
    }

    class RouteLogin extends Route {
        function __construct($data){
            parent::__construct($data);

        }

        function post(){
            extract($_POST);
            $Authentication = new Authentication($username, $password);
    
            if(!empty($username) && !empty($password)) {
                if($Authentication->checkAccount()){
                    $_SESSION['username'] = $username;
                    header("Location: /home.php");
                    die();
                }
                $_SESSION['error'] = 'Invalid username or password!';
                return;
            }
            $_SESSION['error'] = 'Username and password required!';
        }

    }

    class RouteRegister extends Route {
        function __construct($data){
            parent::__construct($data);
        }

        function post() {
            extract($_POST);
            if(!empty($username) && !empty($password)) {
                $Authentication = new Authentication($username, $password);

                if($Authentication->newAccount()) {
                    $_SESSION['msg'] = 'Successfully adding your account!';
                    return;
                }
                $_SESSION['error'] = 'Your account has been added!';
            }else{
                $_SESSION['error'] = 'Username and password required!';
            }
        }
    }
?>