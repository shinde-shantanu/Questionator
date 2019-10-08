<!DOCTYPE html>
<html lang="zxx">
<head>
	<title>EndGam - Gaming Magazine Template</title>
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
					<img src="./img/logo.png" alt="">
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
			<h2>Wildlife</h2>
			<div class="site-breadcrumb">
				<a href="">Home</a>  /
				<span>Wildlife</span>
			</div>
		</div>
	</section>
	<!-- Page top end-->


	<!-- Blog page -->
	<section class="blog-page">
		<div class="container">
			<div class="row">	
				<div class="col-xl-9 col-lg-8 col-md-7">
					<ul class="blog-filter">
						<li><a href="sports.php">Sports</a></li>
						<li><a href="Entertainment.php">Entertainment</a></li>
						<li><a href="vehicle.php">Vehicle</a></li>
					</ul>
				<?php
					echo "<div class='big-blog-item' id='caption-img' >";
					$urls = array("http://news-events.sleeping-out.co.za/wp-content/uploads/2014/09/Dog-Playing-At-Beach-Wallpaper.jpg",
						"https://c402277.ssl.cf1.rackcdn.com/photos/2330/images/hero_small/polar-bear-hero.jpg?1345901694",
						"https://cosmos-magazine.imgix.net/file/spina/photo/553/210414_Zebra_1.jpg?ixlib=rails-1.1.0&h=573&w=859",
						"https://www.sciencenews.org/sites/default/files/main/blogposts/gd_Girafeskoure_free.jpg");
					echo "<div class='big-blog-item' >";
					foreach($urls as $url)
					{
						echo "<a href='#'><img style = 'height:400px;width:400px;padding:15px;	' src='" .$url ."' alt='#' class='blog-thumbnail' ></a>";
					}
					
					echo "</div>";
				?>	
				</div>
				<div class="col-xl-3 col-lg-4 col-md-5 sidebar">
					<div id="stickySidebar">
						<div class="widget-item">
							<form class="search-widget">
								<input type="text">
								<button>search</button>
							</form>
						</div>
						<div class="widget-item">
							<h4 class="widget-title">Trending Topics In Wildlife</h4>
							<div class="trending-widget">
								<div class="tw-item">
									<div class="tw-thumb">
										<img src="./img/blog-widget/1.jpg" alt="#">
									</div>
									<div class="tw-text">
										<div class="tw-meta">11.11.18  /  in <a href="">Wildlife</a></div>
										<h5>Echoes of Jaws as Cape Cod learns to live with  shark</h5>
									</div>
								</div>
								<div class="tw-item">
									<div class="tw-thumb">
										<img src="./img/blog-widget/2.jpg" alt="#">
									</div>
									<div class="tw-text">
										<div class="tw-meta">11.11.18  /  in <a href="">Wildlife</a></div>
										<h5>What is the point of rewilding lynxes? </h5>
									</div>
								</div>
								<div class="tw-item">
									<div class="tw-thumb">
										<img src="./img/blog-widget/3.jpg" alt="#">
									</div>
									<div class="tw-text">
										<div class="tw-meta">11.11.18  /  in <a href="">Wildlife</a></div>
										<h5>Namibia forced by drought to auction 1,000 wild animals</h5>
									</div>
								</div>
								</div>
						</div>
						
						<!--
							
						<div class="widget-item">
							<div class="categories-widget">
								<h4 class="widget-title">categories</h4>
								<ul>
									<li><a href="">Games</a></li>
									<li><a href="">Gaming Tips & Tricks</a></li>
									<li><a href="">Online Games</a></li>
									<li><a href="">Team Games</a></li>
									<li><a href="">Community</a></li>
									<li><a href="">Uncategorized</a></li>
								</ul>
							</div>

						</div>
						-->
						<!--
						<div class="widget-item">
							<h4 class="widget-title">Latest Comments</h4>
							<div class="latest-comments">
								<div class="lc-item">
									<img src="./img/blog-widget/1.jpg" class="lc-avatar" alt="#">
									<div class="tw-text"><a href="">Maria Smith</a> <span>On</span> The best online game out there </div>
								</div>
								<div class="lc-item">
									<img src="./img/blog-widget/2.jpg" class="lc-avatar" alt="#">
									<div class="tw-text"><a href="">Maria Smith</a> <span>On</span> The best online game out there </div>
								</div>
								<div class="lc-item">
									<img src="./img/blog-widget/3.jpg" class="lc-avatar" alt="#">
									<div class="tw-text"><a href="">Maria Smith</a> <span>On</span> The best online game out there </div>
								</div>
								<div class="lc-item">
									<img src="./img/blog-widget/4.jpg" class="lc-avatar" alt="#">
									<div class="tw-text"><a href="">Maria Smith</a> <span>On</span> The best online game out there </div>
								</div>
							</div>
						</div>
						-->
						<div class="widget-item">
						</div>
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
	<script src="js/selection.js"></script>
	
	</body>
</html>
