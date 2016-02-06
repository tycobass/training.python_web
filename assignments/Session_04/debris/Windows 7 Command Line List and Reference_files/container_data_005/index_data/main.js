'use strict';

function startBanner() {	
	function $(id) {return document.getElementById(id);}
	
	var bnr = $('banner');
	var add = bnr.addEventListener ? 'addEventListener' : 'attachEvent';
	var st = setTimeout;
	var ctaArea = $('activeArea');
	var legalHoverArea = $('legalHoverArea');
	var legalCopy = $('legalCopy');
	var bgExitArea = $("bgExitArea");
	
			
	//bgExitArea[add]('click', onExit);
	
	ctaArea[add]('mouseenter', onHover);
	legalHoverArea[add]('mouseover', showLegal);
	legalHoverArea[add]('mouseout', hideLegal);
	//ctaArea[add]('click', onExit);	
	
	startAnim();
	
	function startAnim(){

		st(function(){$('laptop').className = 'In'}, 500);
		st(function(){$('footer').className += ' In'}, 1000);
		st(function(){$('copy1').className = 'In'}, 1800);
		
		st(function(){$('copy1').className = 'Out'}, 3800);
	
		st(function(){$('copy2').className = 'In'}, 4000);
		st(function(){$('copy2b').className = 'In'}, 4500);
		st(function(){$('copy2').className = 'Out'}, 7000);
		st(function(){$('copy2b').className = 'Out'}, 7000);
		
		st(function(){$('upTo').className = 'In'}, 7500);
		st(function(){$('copy3').className = 'In'}, 7700);
		st(function(){$('copy4').className = 'In'}, 9000);
		
		st(function(){$('logo').className = 'In'}, 8300);
		st(function(){$('details_hit').className = 'In'}, 8500);
		st(function(){$('cta').className = 'In'}, 8800);	
		st(function(){$('ctaContainer').className = 'In'}, 10800);	

		st(function(){$('shimmer').className = 'on'}, 9500);
		st(function(){ $("legalHoverArea").style.display = "block" }, 9500);
	
	}
		
	//LEGAL
		function showLegal(){
		legalCopy.className = "visible";
		
		legalHoverArea.style.width = "300px";
		legalHoverArea.style.height = "145px";		
	}
	
	function hideLegal(){
		legalCopy.className = "";
		
		legalHoverArea.style.width = "54px";
		legalHoverArea.style.height = "15px";		
	}
		
	function onHover(){
		$('shimmer').className = '';
		st( function(){$('shimmer').className = 'on'} , 100);
	}
}
