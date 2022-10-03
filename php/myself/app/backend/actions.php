<?php 

    require_once 'config.php';
    require_once dirname(__FILE__) . '../../vendor/autoload.php';

    class Authentication extends Config{        
        private $username, $password;

        public function __construct($username, $password){
            parent::__construct();
            $this->username = $username;
            $this->password = $password;
        }
                
        public function checkAccount($checkUsername=false){
            $query = "SELECT username, password FROM users WHERE username = ?";
            $stmt = $this->link->prepare($query);
            $stmt->execute(array($this->username));
            if($stmt->rowCount() > 0){
                if($checkUsername){
                    return true;
                }
                $password = ($stmt->fetch())['password'];
                return password_verify($this->password, $password);
            }
            return false;
        }

        public function newAccount(){
            if(!$this->checkAccount(true)){
                try{
                    $query = "INSERT INTO users (username, password) VALUES (?,?)";
                    $stmt = $this->link->prepare($query);
                    $stmt -> execute(array($this->username, password_hash($this->password, PASSWORD_BCRYPT)));
                    return true;
                }catch(Exception $e){
                    return false;
                }
            }
            return false;
        }
    }

    class Todos extends Config{
        private $userId;

        public function __construct(){
            parent::__construct();
            $this->userId = $this->setUserId();
        }
        
        public function addTodo($todo,$date) {
            if(!empty($todo) && !empty($date)) { 
                $query = "INSERT INTO todos (todo, due_date, status, created_by) VALUES (?,?,?,?)";
                $stmt = $this->link->prepare($query);
                $stmt -> execute(array($todo,$date, 'active', $this->userId));
            }
        }

        public function setUserId() {
            try{
                $query = "SELECT user_id FROM users WHERE username = ?"; 
                $stmt = $this->link->prepare($query);
                $stmt->execute(array($_SESSION['username']));
                return ($stmt->fetch())['user_id'];
            }catch(Exception $e){
                return false;
            }
        }
        
        public function getTodos(){
            $query = "SELECT * FROM todos WHERE created_by = ?"; 
            $stmt = $this->link->prepare($query);
            $stmt->execute(array($this->userId));
            return $stmt->fetchAll();
            
        }
        public function updateTodo($todoId,$status,$dueDate,$todo){
            $query = "UPDATE todos SET todo = ? , status = ?, due_date = ?  WHERE todo_id = ?";
            $stmt = $this->link->prepare($query);
            $stmt->execute(array($todo,$status,$dueDate,$todoId));

        }
        // public function updateStatusTodo($status){
        //     $query = "UPDATE todos SET  WHERE created_by = ?"; 
        //     $stmt = $this->link->prepare($query);
        //     $stmt->execute(array($this->userId));
        // }
        public function deleteTodo($todoId){
            $query = "DELETE FROM todos WHERE todo_id = ?"; 
            $stmt = $this->link->prepare($query);
            $stmt->execute(array($todoId));
        }

        
    }

?>