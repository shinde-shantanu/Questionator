(function(W){
 	function init(){
		W.document.getElementById('caption-img').addEventListener('click',sendimg,false);
 	}
	function sendimg(e){
	var a=e.target;
	console.log(JSON.stringify({src:a.src,id:a.id}));
	W.localStorage['imginfo']=JSON.stringify({src:a.src,id:a.id});
	W.location.href="caption.php";
 	}
 W.addEventListener('load',init,false)
})(window)
