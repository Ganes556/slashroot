<?php
  if($_SERVER['REQUEST_METHOD'] == "POST" && isset($_POST['e'])){
    $input_user = $_POST['e'];
    if(preg_match('/[^\x20-\x7e]/i',$input_user)){
      die("Not Printable!");
    }
    if(preg_match('/[0-9|a-z|\x7c|A-Z|\x22|\x40|\x21|\x20|\5b|\x5d]/i',$input_user)){      
      die("bad char!");
    }
    if(strlen(count_chars($input_user,3)) > 0x12){
      die("char too long!");
    };
    if(strlen($input_user) > 0x87){      
      die("string too long!");
    }
    eval('echo '. eval('return ' . $input_user . ';') . ';');
  }
?>
