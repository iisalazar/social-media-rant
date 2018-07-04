$(document).ready(function(){
	var pixelScroll = 200;
	$(window).scroll(function(){
		var x = document.getElementById("main-menu");
		if ($(window).scrollTop() > pixelScroll){
			console.log("Baba: " + x);
		}
		else{
			console.log("Balik: "+ x);
		}
	});
});