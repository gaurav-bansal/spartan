<?php

try{
	$pdo=new PDO ("mysql:host=localhost;dbname=test","root","mypass");
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e){
	die("ERROR: COULD NOT CONNECT. ".$e->getMessage());
}

try{
	$sql="INSERT INTO sensor1 (sensorval) VALUES (:sensorval)";
	$stmt=$pdo->prepare($sql);

	$stmt->bindParam(':sensorval', $_POST['sensorval'], PDO::PARAM_STR);
	$sensorval=$_POST['sensorval'];
	$stmt->execute();
	echo "Inserted Successfully.";
} catch(PDOException $e){
	die("ERROR: COULD NOT EXECUTE $sql. ".$e->getMessage());
}

unset($stmt);
unset($pdo);
?>
