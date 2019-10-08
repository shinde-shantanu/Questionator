<!DOCTYPE html>
<html lang="zxx">
<head>
	<title>Questionator.ai</title>
	<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<meta charset="UTF-8">
	<meta name="description" content="EndGam Gaming Magazine Template">
	<meta name="keywords" content="endGam,gGaming, magazine, html">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Favicon -->
	<link href="img/favicon.ico" rel="shortcut icon"/>

	<!-- Google Font -->
	<link href="https://fonts.googleapis.com/css?family=Roboto:400,400i,500,500i,700,700i,900,900i" rel="stylesheet">


	<!-- Stylesheets -->
	<link rel="stylesheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/font-awesome.min.css"/>
	<link rel="stylesheet" href="css/slicknav.min.css"/>
	<link rel="stylesheet" href="css/owl.carousel.min.css"/>
	<link rel="stylesheet" href="css/magnific-popup.css"/>
	<link rel="stylesheet" href="css/animate.css"/>

	<!-- Main Stylesheets -->
	<link rel="stylesheet" href="css/style.css"/>


	<!--[if lt IE 9]>
		  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->

	<style type="text/css">
		.bar {
  width: 100%;
  height: 20px;
  border: 1px solid #2980b9;
  border-radius: 3px;
  background-image: 
    repeating-linear-gradient(
      -45deg,
      #2980b9,
      #2980b9 11px,
      #eee 10px,
      #eee 20px /* determines size */
    );
  background-size: 28px 28px;
  animation: move .5s linear infinite;
}

@keyframes move {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 28px 0;
  }
}
	</style>

	<script type="text/javascript">
		function generateAll() {
			generateCaption();
			generateFace();
			return false;
		}
		function generateCaption(){
			document.getElementById('captionLoadingDiv').style.display ='block';
			var img = document.getElementById('caption-img2');

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6503';
			var params = 'url=' + img.src;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			        var genCaption = data['success']['data'];
			        document.getElementById('caption').innerHTML = genCaption;
			        document.getElementById('captionLoadingDiv').style.display = 'none';
			        document.getElementById('captionDiv').style.display ='block';
			        generateQuestion(genCaption);
			    }
			}
			http.send(params);
		}
		function generateFace(){
			document.getElementById('faceLoadingDiv').style.display ='block';
			var img = document.getElementById('caption-img2');

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6504';
			var params = 'url=' + img.src;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			        var faceData = data['success']['data']['Person details'][0];
			        if(!faceData){
			        	document.getElementById("faceRecognized").style.display ='none';;
			        	document.getElementById('faceNotRecognized').style.display ='block';
			        	//document.getElementById('faceNotRecognized').style.color = white;

			        }
			        var table = document.getElementById("face");
			        var i = 1;
			        for(key in faceData){
						var row = table.insertRow(i);
						var cell1 = row.insertCell(0);
						var cell2 = row.insertCell(1);
						cell1.innerHTML = key;
						cell2.innerHTML = faceData[key];
						i++;
			        }
			        document.getElementById('faceLoadingDiv').style.display = 'none';
			        document.getElementById('faceDiv').style.display ='block';
			        console.log(faceData['Name'].split(" ")[0]);
			        generateFaceOptions(faceData['Name'].split(" ")[0].toLowerCase());
			    }
			}
			http.send(params);
		}
		function generateQuestion(sentence){
			console.log(sentence);
			document.getElementById('questionLoadingDiv').style.display ='block';

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6502/sentence';
			var params = 'sentence=' + sentence;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			    	console.log(data['success']['data']);
			        var question = data['success']['data']['question'];
			        var answer = data['success']['data']['answer'];
			        document.getElementById('question').innerHTML = question;
			        document.getElementById('questionLoadingDiv').style.display = 'none';
			        document.getElementById('questionDiv').style.display ='block';
			        generateOptions(answer);
			        
			    }
			}
			http.send(params);
		}
		function generateFaceOptions(opt){
			//document.getElementById('optionsLoadingDiv').style.display ='block';

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6505';
			var params = 'answer=' + opt;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			        var correctPos = Math.floor(Math.random() * data.length);
			        console.log(correctPos);
			        var insertedCorrect = false;
			    	for(var i = 0; i < data.length; i++){
			    		var node = document.createElement("input");  
						node.setAttribute('type', 'radio');
						node.setAttribute('name', 'radioFaceAnswer');  
						node.setAttribute('value', opt);
						var textnode;
						if(i == correctPos && insertedCorrect == false){
							i--;
							textnode = document.createTextNode(' ' + opt);
							node.id = 'correct';
							node.setAttribute('value', opt);
							insertedCorrect = true;
						}
						else
							textnode = document.createTextNode(' ' + data[i]);
						document.getElementById("faceOptions").appendChild(node);
						document.getElementById("faceOptions").appendChild(textnode);
						var node = document.createElement("br");
						document.getElementById("faceOptions").appendChild(node);


			    	}
			        //document.getElementById('optionsLoadingDiv').style.display = 'none';
			        //document.getElementById('optionsDiv').style.display ='block';
			        
			    }
			}
			http.send(params);
		}
		function generateOptions(opt){
			document.getElementById('optionsLoadingDiv').style.display ='block';

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6505';
			var params = 'answer=' + opt;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			        var correctPos = Math.floor(Math.random() * data.length);
			        console.log(correctPos);
			        var insertedCorrect = false;
			    	for(var i = 0; i < data.length; i++){
			    		var node = document.createElement("input");  
						node.setAttribute('type', 'radio');
						node.setAttribute('name', 'radioAnswer');  
						node.setAttribute('value', opt);
						var textnode;
						if(i == correctPos && insertedCorrect == false){
							i--;
							textnode = document.createTextNode(' ' + opt);
							node.id = 'correct';
							node.setAttribute('value', opt);
							insertedCorrect = true;
						}
						else
							textnode = document.createTextNode(' ' + data[i]);
						document.getElementById("options").appendChild(node);
						document.getElementById("options").appendChild(textnode);
						var node = document.createElement("br");
						document.getElementById("options").appendChild(node);


			    	}
			        document.getElementById('optionsLoadingDiv').style.display = 'none';
			        document.getElementById('optionsDiv').style.display ='block';
			        
			    }
			}
			http.send(params);

		}
		function checkAnswer(){
			var correct, right = false;
			var radios = document.getElementsByName('radioAnswer');
		    for(var i = 0; i < radios.length; i++ ) {
		    	if(radios[i].id == 'correct')
		    		correct = radios[i];
		        if(radios[i].checked) {
		            if(radios[i].id == 'correct')
		            	right = true;
					
				}
		    }
			if(right)
					swal("Correct!", "You're right!", "success");
			else
				swal("Wrong", "Correct answer is " + correct.value + '.', "error");	
		}
		function checkFaceAnswer(){
			var correct, right = false;
			var radios = document.getElementsByName('radioFaceAnswer');
		    for(var i = 0; i < radios.length; i++ ) {
		    	if(radios[i].id == 'correct')
		    		correct = radios[i];
		        if(radios[i].checked) {
		            if(radios[i].id == 'correct')
		            	right = true;
					
				}
		    }
			if(right)
					swal("Correct!", "You're right!", "success");
			else
				swal("Wrong", "Correct answer is " + correct.value + '.', "error");	
		}
	</script>

</head>
<body>
	<!-- Page Preloder -->
	<div id="preloder">
		<div class="loader"></div>
	</div>

	<!-- Header section -->
	<header class="header-section">
		<div class="header-warp">
			<div class="header-bar-warp d-flex">
				<!-- site logo -->
				<a href="home.php" class="site-logo">
					<img src="./img/logo.png" alt="">
				</a>
				<nav class="top-nav-area w-100">
					<!-- Menu -->
					<ul class="main-menu primary-menu">
						<li><a href="home.php">Home</a></li>
						<li><a href="caption_gen.php">Caption Generator</a></li>
						<li><a href="question.php">Question Generator</a></li>
						<li><a href="option.php">Options</a></li>
						<li><a href="about.php">About</a></li>
					</ul>
				</nav>
			</div>
		</div>
	</header>
	<!-- Header section end -->

	<!-- Page top section -->
	
	<section class="page-top-section set-bg" data-setbg="img/page-top-bg/1.jpg">
		<div class="page-info">
			<h2>Captioning Images</h2>
			<div class="site-breadcrumb">
				<a href=""></a>  				
				<span></span>
			</div>
		</div>
	</section>

	<!-- Page top end-->


	<!-- Games section -->
	<section class="games-single-page">
		<div class="container">
			<div class="game-single-preview">
				<img src="" alt="" id="caption-img2">
			</div>		
			<div class="row">
				<div style="text-align:center">
					<div class="site-btn" style="" onclick="generateAll()">Generate <img src="img/icons/double-arrow.png" alt="#">

					</div>
				</div>
			<div class="col-xl-3 col-lg-4 col-md-5 sidebar game-page-sideber">
					<div id="stickySidebar">
						<div class="widget-item">
						</div>
					</div>
			</div>

			</div>
			<br>
			<br>
			<br>

			<div id='captionLoadingDiv' style="display: none;">
				<h4>Generating caption</h4>
				<div class="bar"></div>
			</div>
			<div id='captionDiv' style="display: none;">
				<h4>Generated caption:</h4>
				<h3 id='caption' style="color: white;"></h3>
			</div>

			<div id='faceLoadingDiv' style="display: none; margin-top: 50px;">
				<h4>Recognizing faces</h4>
				<div class="bar"></div>
			</div>
			<div id='faceDiv' style="display: none; color: white; margin-top: 50px;">
				<h4>Face:</h4>
				<h3 id='faceNotRecognized' style="display: none;color:white">Face not recognized</h3>
				<div id="faceRecognized">
					<table id="face">
						<tr>
							<th style="width: 200px;">Field</th>
							<th style="width: 200px;">Value</th>
						</tr>
					</table>
					<h4>Guess this person:</h4>
					<div id="faceOptions" style="color: white; font-size: 20px;"></div>
					<div class="site-btn" style="" onclick="checkFaceAnswer()">Submit<img src="img/icons/double-arrow.png" alt="#">
				</div>
			</div>
			
			<div id='questionLoadingDiv' style="display: none; margin-top: 50px;">
				<h4>Generating question</h4>
				<div class="bar"></div>
			</div>
			<div id='questionDiv' style="display: none; margin-top: 50px;">
				<h4>Generated question:</h4>
				<h3 id='question' style="color: white;"></h3>
			</div>

			<div id='optionsLoadingDiv' style="display: none; margin-top: 50px;">
				<h4>Generating options</h4>
				<div class="bar"></div>
			</div>
			<div id='optionsDiv' style="display: none; margin-top: 50px;">
				<h4>Select one:</h4>
				<div id="options" style="color: white; font-size: 20px;"></div>

				<div class="site-btn" style="" onclick="checkAnswer()">Submit<img src="img/icons/double-arrow.png" alt="#">
			</div>

		</div>

		
	</section>

	<!-- Games end-->

	<section class="game-author-section">
		<div class="container">
			<div class="game-author-pic set-bg" data-setbg="img/author.jpg"></div>
			<div class="game-author-info">
				<h4>Website by: M-vision</h4>
				<p>Questionator.ai is a advance question generating bot which can generate images for images as well as text, the first of its kind.It used a number of machine learning and semantic approaches to achieve these results</p>
			</div>
		</div>
	</section>


	<!-- Newsletter section end -->


	<!-- Footer section -->
	<footer class="footer-section">
		<div class="container">
			<div class="copyright"><a href="">M-vision</a> 2019 @ All rights reserved</div>
		</div>
	</footer>
	<!-- Footer section end -->


	<!--====== Javascripts & Jquery ======-->
	<script src="js/jquery-3.2.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.slicknav.min.js"></script>
	<script src="js/owl.carousel.min.js"></script>
	<script src="js/jquery.sticky-sidebar.min.js"></script>
	<script src="js/jquery.magnific-popup.min.js"></script>
	<script src="js/main.js"></script>
	<script src="js/caption.js"></script>
	</body>
</html>
