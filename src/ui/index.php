<?php
include_once "config.php";
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no">
    <title>Spectral image </title>
    <link rel="icon" type="image/x-icon" href="admin/assets/img/favicon.ico"/>
    <link href="admin/assets/css/loader.css" rel="stylesheet" type="text/css" />
    <script src="admin/assets/js/loader.js"></script>

    <!-- BEGIN GLOBAL MANDATORY STYLES -->
    <link href="https://fonts.googleapis.com/css?family=Nunito:400,600,700" rel="stylesheet">
    <link href="admin/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="admin/assets/css/plugins.css" rel="stylesheet" type="text/css" />
    <!-- END GLOBAL MANDATORY STYLES -->

    <!-- BEGIN PAGE LEVEL PLUGINS/CUSTOM STYLES -->
    <!-- END PAGE LEVEL PLUGINS/CUSTOM STYLES -->
    <style type="text/css">
        .b-l-card-1 .card-img-top:hover {
            -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
            filter: grayscale(100%);
        }
        .card-img-black {
            -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
            filter: grayscale(100%);
        }
    </style>
    <script src = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js">
    </script>
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.js"></script>
</head>
<body class="alt-menu">
    <!-- BEGIN LOADER -->
    <div id="load_screen"> <div class="loader"> <div class="loader-content">
        <div class="spinner-grow align-self-center"></div>
    </div></div></div>
    <!--  END LOADER -->

    <?php include_once "inc/header.php"; ?>

    <!--  BEGIN MAIN CONTAINER  -->
    <div class="main-container sidebar-closed sbar-open" id="container">

        <div class="overlay"></div>
        <div class="search-overlay"></div>

        <?php include_once "inc/sidebar.php"; ?>
        
        <!--  BEGIN CONTENT PART  -->
        <div id="content" class="main-content">
            <div class="layout-px-spacing">

                <div class="row layout-top-spacing" id="imageDIV">
                    <?php 
                    $sql = "SELECT * FROM images ORDER BY id DESC";
                    $result = mysqli_query($con, $sql);
                    if (mysqli_num_rows($result) > 0) {
                      // output data of each row
                      while($row = mysqli_fetch_assoc($result)) {
                    ?>
                    <div class="col-xl-4 col-lg-6 col-md-6 mb-4" title="<?php echo $row["width"] ?> x <?php echo $row["height"] ?>, Size: <?php echo $row["filesize"] ?> kb">

                        <div class="card b-l-card-1 h-100" style="border: none;-webkit-box-shadow: 0 0.1px 0px rgba(0, 0, 0, 0.002), 0 0.2px 0px rgba(0, 0, 0, 0.003), 0 0.4px 0px rgba(0, 0, 0, 0.004), 0 0.6px 0px rgba(0, 0, 0, 0.004), 0 0.9px 0px rgba(0, 0, 0, 0.005), 0 1.2px 0px rgba(0, 0, 0, 0.006), 0 1.8px 0px rgba(0, 0, 0, 0.006), 0 2.6px 0px rgba(0, 0, 0, 0.007), 0 3.9px 0px rgba(0, 0, 0, 0.008), 0 7px 0px rgba(0, 0, 0, 0.01); -moz-box-shadow: 0 0.1px 0px rgba(0, 0, 0, 0.002), 0 0.2px 0px rgba(0, 0, 0, 0.003), 0 0.4px 0px rgba(0, 0, 0, 0.004), 0 0.6px 0px rgba(0, 0, 0, 0.004), 0 0.9px 0px rgba(0, 0, 0, 0.005), 0 1.2px 0px rgba(0, 0, 0, 0.006), 0 1.8px 0px rgba(0, 0, 0, 0.006), 0 2.6px 0px rgba(0, 0, 0, 0.007), 0 3.9px 0px rgba(0, 0, 0, 0.008), 0 7px 0px rgba(0, 0, 0, 0.01); box-shadow: 0 0.1px 0px rgba(0, 0, 0, 0.002), 0 0.2px 0px rgba(0, 0, 0, 0.003), 0 0.4px 0px rgba(0, 0, 0, 0.004), 0 0.6px 0px rgba(0, 0, 0, 0.004), 0 0.9px 0px rgba(0, 0, 0, 0.005), 0 1.2px 0px rgba(0, 0, 0, 0.006), 0 1.8px 0px rgba(0, 0, 0, 0.006), 0 2.6px 0px rgba(0, 0, 0, 0.007), 0 3.9px 0px rgba(0, 0, 0, 0.008), 0 7px 0px rgba(0, 0, 0, 0.01); ">
                            <h5 class="card-title mt-2"><?php echo $row["title"] ?></h5>
                            <div id='pnt<?php echo $row["id"] ?>' >
                                <img id='my_img<?php echo $row["id"] ?>' class="card-img-top" src="images/<?php echo $row["img"] ?>" alt="">
                            </div>
                            <div class="card-body">
                                <strong class="card-category"><?php echo $row["width"] ?> x <?php echo $row["height"] ?>, Size: <?php echo $row["filesize"] ?> kb </strong>
                               
                                <p class="card-text meta-info meta-time mb-2"><small class="">White picture <a class="btn btn-success btn-sm" target="_blank" href="img.php?img=<?php echo $row["img"] ?>">download</a></small></p>
                                <p class="card-text mb-4"><?php echo $row["description"] ?></p>
                            </div>
                        </div>
                    </div>
                    <?php
                        }
                    } else {
                      echo "0 results";
                    }
                    ?>
                </div>

                <script>
                    function printDiv(id,img) {
                        var element = document.getElementById("my_img"+id);
                        element.classList.add("card-img-black");
                        var divContents = document.getElementById("pnt"+id).innerHTML;
                        var a = window.open('', '', 'height=500, width=500');
                        a.document.write('<html>');
                        a.document.write('<body ><img style="-webkit-filter: grayscale(100%);filter: grayscale(100%);" id="my_img7" class="card-img-top" src="images/'+img+'" alt="">');
                        // a.document.write(divContents);
                        a.document.write('</body></html>');
                        a.document.close();
                        a.print();
                    }
                </script>
            </div>
            <div class="footer-wrapper">
                <div class="footer-section f-section-1">
                    <p class="">Copyright © 2021 <a target="_blank" href="#"></a>, All rights reserved.</p>
                </div>
                <div class="footer-section f-section-2">
                    <p class="">Coded with <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></p>
                </div>
            </div>
        </div>
        <!--  END CONTENT PART  -->

    </div>
    <!-- END MAIN CONTAINER -->

    <!-- BEGIN GLOBAL MANDATORY SCRIPTS -->
    <script src="admin/assets/js/libs/jquery-3.1.1.min.js"></script>
    <script src="admin/bootstrap/js/popper.min.js"></script>
    <script src="admin/bootstrap/js/bootstrap.min.js"></script>
    <script src="admin/plugins/perfect-scrollbar/perfect-scrollbar.min.js"></script>
    <script src="admin/assets/js/app.js"></script>
    <script>
        $(document).ready(function() {
            App.init();
        });
    </script>
    <script src="admin/assets/js/custom.js"></script>
    <!-- END GLOBAL MANDATORY SCRIPTS -->


</body>

</html>