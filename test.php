<?php
chdir(".\\Sign-Language-Recognition-master\\Sign-Language-Recognition\\code\\");
$pyscript = "predict_from_file.py";
$python = "C:\\Python27\\python.exe";
$svm = "svm";
$cod = "$python $pyscript $svm";
$output = shell_exec("py2_env\\Scripts\\activate && python predict_from_file.py svm 2>&1 ");

preg_match_all('#labelx=([^\s]+)#', $output, $matches);

$result = implode(' ', $matches[1]);
echo "$result";
//echo "$output hello";
//echo "$output";
//$python $pyscript $svm
?>