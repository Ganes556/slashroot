<?php 
    class Config {
        public function __construct() {
            $dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
            $dotenv->load();
            $this->connect();
        }
        public function __destruct() {
            $this->link = null;
        }
        public function connect() {
            extract($_ENV);
            try{
                $this->link = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
                $this->link->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);                
            }catch(PDOException $e){
                echo "Connection failed: " . $e->getMessage();
            }
        }

    }
?>