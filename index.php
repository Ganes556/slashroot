<?php     
    if($_SERVER['REQUEST_METHOD'] == "POST" && isset($_POST['cmd'])){
        $input_user = $_POST['cmd'];    

        if(preg_match_all('/[^\x20-\x7e]/',$input_user)){
            die("Not Printable!");
        }
        if(preg_match_all('/[0-9|a-z|A-Z|"|@|!|\x20|\x21-\x23|\x25-\x26|\x2a-\2b|\x2d-\x2f|\x3a|\x3c|\x3e-\x40|\x5b-\x5d|\x60|\x7e]/',$input_user)){      
            die("bad char!");
        }
        if(strlen(count_chars($input_user,3)) > 12 ){            
            die("char too long!");
        };
        
        if(strlen($input_user) > 777){  
            die("string too long!");
        }        
        
        eval($input_user);
    }

?>