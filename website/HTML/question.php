<!DOCTYPE html>
<html lang="zxx">
<head>
	<title>Questionator.ai</title>
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
		function generateQuestion(){
			
			document.getElementById('questionLoadingDiv').style.display ='block';

			var http = new XMLHttpRequest();
			var url = 'http://52.230.120.146:6502/sentence';
			var params = 'sentence=' + document.getElementById('questionSentence').value;
			http.open('POST', url, true);

			http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

			http.onreadystatechange = function() {
			    if(http.readyState == 4 && http.status == 200) {
			    	var data = JSON.parse(http.response);
			    	console.log(data['success']['data']);
			        var question = data['success']['data']['question'];
			        var answer = data['success']['data']['answer'];
			        document.getElementById('question').innerHTML = question;
			        document.getElementById('answer').innerHTML = answer;
			        document.getElementById('questionLoadingDiv').style.display = 'none';
			        document.getElementById('questionDiv').style.display ='block';
			        document.getElementById('answerDiv').style.display ='block';
			        //generateOptions(answer);
			    }
			}
			http.send(params);
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
			<!--
			<div class="header-social d-flex justify-content-end">
				<p>Follow us:</p>
				<a href="#"><i class="fa fa-pinterest"></i></a>
				<a href="#"><i class="fa fa-facebook"></i></a>
				<a href="#"><i class="fa fa-twitter"></i></a>
				<a href="#"><i class="fa fa-dribbble"></i></a>
				<a href="#"><i class="fa fa-behance"></i></a>
			</div> -->
			<div class="header-bar-warp d-flex">
				<!-- site logo -->
				<a href="home.php" class="site-logo">
					<img src="./img/questionlogo_small.jpg" alt="" style="margin-top:-25px;">
				</a>
				<nav class="top-nav-area w-100">
					<div class="user-panel">
						<a href="">Login</a> / <a href="">Register</a>
					</div>
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
	<section class="page-top-section set-bg" data-setbg="img/page-top-bg/3.jpg">
		<div class="page-info">
			<h2>Question Generator</h2>
			<div class="site-breadcrumb">
				<a href="">Home</a>  /
				<span>Caption Generator</span>
			</div>
		</div>
	</section>
	<!-- Page top end-->


	<!-- Blog page -->
	<section class="blog-page">
		<div class="container">
			<div class="row">	
				<div class="col-xl-12 col-lg-12 col-md-12">
					<section class="newsletter-section">
						<div class="container">
							<h2>Enter sentence for question</h2>
							<div class="newsletter-form">
								<input type="text" placeholder="ENTER SENTENCE FOR QUESTION" id="questionSentence">
								<br><br><br>
								<button class="site-btn" onclick="generateQuestion();">Generate question  <img src="img/icons/double-arrow.png" alt="#"/></button>
							</div>
						</div>
					</section>
					
					<img src="" id="captionImage" style="display: block;margin: 0 auto">

					<div id='questionLoadingDiv' style="display: none; margin-top: 50px;">
						<h4>Generating question</h4>
						<div class="bar"></div>
					</div>
					<div id='questionDiv' style="display: none; margin-top: 50px;">
						<h4>Generated question:</h4>
						<h3 id='question' style="color: white;"></h3>
					</div>
						</div>

					<div id='answerDiv' style="display: none; margin-top: 50px;">
						<h4>Answer:</h4>
						<h3 id='answer' style="color: white;"></h3>
					</div>
						</div>
						
			</div>
		</div>
	</section>
	<!-- Blog page end-->


	<!--
	<section class="newsletter-section">
		<div class="container">
			<h2>Subscribe to our newsletter</h2>
			<form class="newsletter-form">
				<input type="text" placeholder="ENTER YOUR E-MAIL">
				<button class="site-btn">subscribe <img src="img/icons/double-arrow.png" alt="#"/></button>
			</form>
		</div>
	</section>	
-->

	<!-- Footer section -->
	<!--
	<footer class="footer-section">
		<div class="container">
			<div class="footer-left-pic">
				<img src="img/footer-left-pic.png" alt="">
			</div>
			<div class="footer-right-pic">
				<img src="img/footer-right-pic.png" alt="">
			</div>
			<a href="#" class="footer-logo">
				<img src="./img/logo.png" alt="">
			</a>
			<ul class="main-menu footer-menu">
				<li><a href="">Home</a></li>
				<li><a href="">Games</a></li>
				<li><a href="">Reviews</a></li>
				<li><a href="">News</a></li>
				<li><a href="">Contact</a></li>
			</ul>
			<div class="footer-social d-flex justify-content-center">
				<a href="#"><i class="fa fa-pinterest"></i></a>
				<a href="#"><i class="fa fa-facebook"></i></a>
				<a href="#"><i class="fa fa-twitter"></i></a>
				<a href="#"><i class="fa fa-dribbble"></i></a>
				<a href="#"><i class="fa fa-behance"></i></a>
			</div>
			<div class="copyright"><a href="">Colorlib</a> 2018 @ All rights reserved</div>
		</div>
	</footer> -->
	<!-- Footer section end -->


	<!--====== Javascripts & Jquery ======-->
	<script src="js/jquery-3.2.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.slicknav.min.js"></script>
	<script src="js/owl.carousel.min.js"></script>
	<script src="js/jquery.sticky-sidebar.min.js"></script>
	<script src="js/jquery.magnific-popup.min.js"></script>
	<script src="js/main.js"></script>
	
	
	</body>
</html>
