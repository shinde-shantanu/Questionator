window.onload=function(){
 var img=document.getElementById("caption-img2")
 var info=JSON.parse(window.localStorage['imginfo']);
 //delete window.localStorage['imginfo'];
 img.src=info.src;
 
 }

 function captiongen(){
 	console.log('clicked')


 }
