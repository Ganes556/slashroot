<?php 
    $allowed = [];
    for($i=0;$i < 256; $i++){
        $input = chr($i);
        if(preg_match('/[^\x20-\x7e]/', $input)){
            continue;
        }
        if(preg_match_all('/[0-9|a-z|A-Z|"|@|!|\x20|\x21-\x23|\x25-\x26|\x2a-\2b|\x2d-\x2f|\x3a|\x3c|\x3e-\x40|\x5b-\x5d|\x60|\x7e]/',$input)){      
            die("bad char!");
        }
        // if(preg_match('/[0-9|a-z|A-Z|"|@|!|\x20|\x21-\x23|\x25-\x26|\x2a-\2b|\x2d-\x2f|\x3a|\x3c|\x3e-\x40|\x5b-\x5d|\x60|\x7e]/',$input)){      
        //     continue;
        // }

        echo chr($i) . '\n';
        array_push($allowed,chr($i));
        var_dump($allowed);
    }
?>