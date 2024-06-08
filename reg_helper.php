<?php

session_start();

$con = mysqli_connect('localhost','admin','admin');

mysqli_select_db($con,'testusers');

$email = $_POST['email'];
$pass = $_POST['pswd'];
$fn = $_POST['fname'];
$ln = $_POST['lname'];
$dat = $_POST['dob'];
$g = $_POST['gender'];
$height = $_POST['ht'];
$weight = $_POST['wt'];
$uid = uniqid("uid");
$s = " select * from users where email = '$email'";
$result = mysqli_query($con,$s);
$num = mysqli_num_rows($result);
echo "</br>";
echo "$num";
if($num==1)
{
	echo "Email already registered";
}
else
{
	$reg = "insert into users(password,uid,fname,lname,birthdate,gender,height,weight,email) values('$pass' , '$uid','$fn','$ln','$dat','$g','$height','$weight','$email')";
    mysqli_query($con,$reg);
    echo "Registration successful by akshay";
}

?>