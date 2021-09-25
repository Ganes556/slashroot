<?php
  if($_SERVER['REQUEST_METHOD'] == "POST" && isset($_POST['cmd'])){
    $input_user = $_POST['cmd'];  
    if(preg_match_all('/[^\x20-\x7e]/',$input_user)){
      die("Not Printable!");
    }
    if(preg_match_all('/[0-9|a-z|A-Z|"|@|!|\x20|\]]/',$input_user)){      
      die("bad char!");
    }
    if(strlen(count_chars($input_user,3)) > 20){
      die("char too long!");
    };
    if(strlen($input_user) > 145){      
      die("string too long!");
    }
    eval('echo '. eval('return ' . $input_user . ';') . ';');
  }
?>