<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Convert HTML To Image</title>
    <script src = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js">
    </script>
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.js">
    </script>
  </head>
  <style media="screen">
    #htmlContent{
      display: flex;
      align-items: center;
      justify-content: center;
    }
  </style>
  <body onload = "autoClick();">

    <div id = "htmlContent">
    	<div id="output"> </div>
    </div>
    <a id="download">Download</a>


    <script type="text/javascript">
      function autoClick(){
        $("#download").click();
      }

      $(document).ready(function(){
        var element = $("#htmlContent");

        $("#download").on('click', function(){

          html2canvas(element, {
            onrendered: function(canvas) {
              var imageData = canvas.toDataURL("image/jpg");
              var newData = imageData.replace(/^data:image\/jpg/, "data:application/octet-stream");
              $("#download").attr("download", "image.jpg").attr("href", newData);
            }
          });

        });
      });

    </script>

    <img style="display: none;" src="images/<?php echo $_GET["img"] ?>" id="eeveelutions"/>
    <canvas style="display: none;" id="canvas"></canvas>

    <script type="text/javascript">
    	const img = document.getElementById("eeveelutions");
		const canvas = document.getElementById("canvas");
		const ctx = canvas.getContext("2d");

		img.onload = function () {
		  let canvas = document.createElement("canvas");
			let context = canvas.getContext("2d");
			canvas.width = event.target.width;
			canvas.height = event.target.height;
			document.getElementById("output").appendChild(canvas);
			context.drawImage(event.target, 0, 0);
			let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
			let data = imageData.data;
			for (var i = 0; i < data.length; i += 4) {
		      var avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
		      data[i]     = avg; // red
		      data[i + 1] = avg; // green
		      data[i + 2] = avg; // blue
		    }
		    context.putImageData(imageData, 0, 0);
		};
    </script>
  </body>
</html>