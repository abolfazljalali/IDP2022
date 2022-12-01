<?php 
session_start();
include_once "../config.php";
if(isset($_SESSION['admin']) && $_SESSION['admin']!=true){
    header("Location: auth_login.php");
}
?>