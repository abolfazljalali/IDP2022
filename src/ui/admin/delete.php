<?php
ob_start();
include_once "inc/autoload.php";
$msg = "";
if (isset($_POST['delete'])) {

	$filename = $_POST['img'];
	$id = $_POST['id'];
    
    @unlink("../images/".$filename);

    $sql = "DELETE FROM images WHERE id = $id";

    $q = mysqli_query($con,$sql);
    if ($q) {
    	$_SESSION['msg'] = '<div class="alert alert-success border-0 mb-4" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><svg> ... </svg></button>Image successfully deleted.
        </div>';
    }else{
    	$_SESSION['msg'] = '<div class="alert alert-danger border-0 mb-4" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><svg> ... </svg></button>
            Something wrong.</button>
        </div> ';
    } 

}
header("Location: image_list.php");
?>