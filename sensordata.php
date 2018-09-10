<html>
<head>
<title>Sensor data</title>
<meta http-equiv="refresh" content="5"/>
</head>
<body>
<h3>PIR sensor detection data</h3>
<?php
$dsn='mysql:dbname=test;host=localhost';
$user='root';
$password='mypass';
try{
        $dbh=new PDO($dsn, $user, $password);

        $sql='select * from sensor1';
	foreach($dbh->query($sql) as $row){
        	print($row['tstamp'].'     -     ');
        	print($row['sensorval'].'.');
        	print('<br/>');
	}

}
catch (PDOException $e){
        print('Error:'.$e->getMessage());
        die();
}
$dbh = null;

?>

</body>
</html>
