<?php
include_once "inc/autoload.php";
$msg = "";
if (isset($_POST['submit'])) {
    $id = $_POST['id'];
	$newfilename = "";
    if (isset($_FILES["image_file"]["name"]) && !empty($_FILES["image_file"]["name"])) {
        if (!empty($_FILES["image_file"]["name"])) {

            @unlink("../images/".$_POST['input_img']);
            $temp = explode(".",$_FILES["image_file"]["name"]);
            $newfilename = uniqid('', true).'.' . end($temp);
            $target = "../images/".$newfilename;  
            move_uploaded_file($_FILES['image_file']['tmp_name'], $target);
        }
        $file = getimagesize("../images/".$newfilename);

        $title = $_POST['title'];
        $description = $_POST['description'];
        $width = $file[0];
        $height = $file[1];

        $file_size = $_FILES["image_file"]["size"];

        $sql = "UPDATE `images` set `title`='$title', `description`='$description', `img`='$newfilename', `width`='$width', `height`='$height', `filesize`='$file_size' where id = $id";
    }else{
        

        $title = $_POST['title'];
        $description = $_POST['description'];
        
        $sql = "UPDATE `images` set `title`='$title', `description`='$description' where id = $id";

    }
    

    $q = mysqli_query($con,$sql);
    if ($q) {
    	$_SESSION['msg'] = '<div class="alert alert-success border-0 mb-4" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><svg> ... </svg></button>Image successfully deleted.
        </div>';
        header("Location: image_list.php");
    }else{
    	$msg = "";
    } 

}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no">
    <title>Admin | Image edit </title>
    <link rel="icon" type="image/x-icon" href="assets/img/favicon.ico"/>
    <!-- BEGIN GLOBAL MANDATORY STYLES -->
    <link href="https://fonts.googleapis.com/css?family=Nunito:400,600,700" rel="stylesheet">
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="assets/css/plugins.css" rel="stylesheet" type="text/css" />
    <!-- END GLOBAL MANDATORY STYLES -->

    <!-- BEGIN PAGE LEVEL CUSTOM STYLES -->
    <link href="assets/css/scrollspyNav.css" rel="stylesheet" type="text/css" />
    <!-- BEGIN PAGE LEVEL CUSTOM STYLES -->
</head>
<body data-spy="scroll" data-target="#navSection" data-offset="100">
    
    <?php include_once "inc/header.php" ?>

    <!--  BEGIN MAIN CONTAINER  -->
    <div class="main-container" id="container">

        <div class="overlay"></div>
        <div class="search-overlay"></div>

        <?php include_once "icc/sidebar.php" ?>

        <!--  BEGIN CONTENT AREA  -->
        <div id="content" class="main-content">
            <div class="row">
                <div id="custom_styles" class="col-lg-12 layout-spacing col-md-12">
                    <div class="statbox widget box box-shadow">
                        <div class="widget-header">
                            <div class="row">
                                <div class="col-xl-12 col-md-12 col-sm-12 col-12">
                                    <h4>New image upload</h4>
                                </div>                 
                            </div>
                        </div>
                        <div class="widget-content widget-content-area">
                            <?php 
                            $id = $_REQUEST['id'];
                            $sql = "SELECT * FROM images where id = $id ORDER BY id DESC";
                                $result = mysqli_query($con, $sql);
                                if (mysqli_num_rows($result) > 0) {
                                  // output data of each row
                                  while($row = mysqli_fetch_assoc($result)) {
                            ?>                    
                            <form class="needs-validation" novalidate method="post" action="" enctype="multipart/form-data">
                                <input type="hidden" name="id" value="<?php echo $row['id'] ?>">
                                <div class="form-row">
                                    <div class="col-md-8 mb-4">
                                        <label for="validationCustom01">Title</label>
                                        <input type="text" name="title" class="form-control" id="validationCustom01" placeholder="Title" value="<?php echo $row['title'] ?>" required>
                                        <div class="valid-feedback">
                                            Please provide a valid title
                                        </div>
                                    </div>
                                    <div class="col-md-4 mb-4">
                                        <label for="validationCustom02">Image file</label>
                                        <input type="file" name="image_file" class="form-control-file" id="validationCustom02" required>
                                        <div class="valid-feedback">
                                            Please provide a valid image file
                                        </div>
                                        <img src="../images/<?php echo $row['img'] ?>" style="height: 100px;width: 100px;">
                                        <input type="hidden" name="input_img" value="<?php echo $row['img'] ?>">
                                    </div>
                                </div>
                                <div class="form-row">
                                    <div class="col-md-12 mb-4">
                                        <label for="validationCustom03">Description</label>
                                        <textarea name="description" class="form-control" id="validationCustom03" placeholder="Description" required><?php echo $row['description'] ?></textarea>
                                        <div class="invalid-feedback">
                                            Please provide a valid description.
                                        </div>
                                    </div>
                                </div>
                                <button class="btn btn-primary mt-3" type="submit" name="submit">Submit</button>
                            </form>
                            <?php } } ?>
                        </div>
                    </div>
                </div>
            </div>
            <?php include_once "inc/footer.php"; ?>
        </div>
        <!--  END CONTENT AREA  -->
    </div>
    <!-- END MAIN CONTAINER -->
       
    <!-- BEGIN GLOBAL MANDATORY SCRIPTS -->
    <script src="assets/js/libs/jquery-3.1.1.min.js"></script>
    <script src="bootstrap/js/popper.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <script src="plugins/perfect-scrollbar/perfect-scrollbar.min.js"></script>
    <script src="assets/js/app.js"></script>
    
    <script>
        $(document).ready(function() {
            App.init();
        });
    </script>
    <script src="plugins/highlight/highlight.pack.js"></script>
    <script src="assets/js/custom.js"></script>
    <!-- END GLOBAL MANDATORY SCRIPTS -->
    
    <!--  BEGIN CUSTOM SCRIPTS FILE  -->
    <script src="assets/js/scrollspyNav.js"></script>
    <script src="assets/js/forms/bootstrap_validation/bs_validation_script.js"></script>
    <!--  END CUSTOM SCRIPTS FILE  -->

</body>

</html>