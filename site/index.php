<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<?php
	$dateYesterday = date("d.m.Y", strtotime("yesterday"));
	
	$dateYesterdayForFilenameGeneration = date("Y-m-d", strtotime("yesterday"));
	$bigImageFilename = $dateYesterdayForFilenameGeneration.".gif";
	$smallImageFilename = $dateYesterdayForFilenameGeneration."--small.gif";
	
	function filesize_formatted($path)
	{
    	$size = filesize($path);
    	$units = array( 'B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB');
    	$power = $size > 0 ? floor(log($size, 1024)) : 0;
    	return number_format($size / pow(1024, $power), 2, '.', ',') . ' ' . $units[$power];
	}
	
	$bigImageFileSize = filesize_formatted($bigImageFilename);
	
	$doBig = $_COOKIE["alwaysBig"];
?>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
	
	<link href='http://fonts.googleapis.com/css?family=Exo:200,400|Open+Sans:300,400,600' rel='stylesheet' type='text/css'>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js" ></script>
	<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
	<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
	<link href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
	
	<script type="text/javascript">
		function setCookie(c_name,value,expiredays) {
        	var exdate=new Date()
			exdate.setDate(exdate.getDate()+expiredays)
			document.cookie=c_name+ "=" +escape(value)+((expiredays==null) ? "" : ";expires="+exdate)
		}
		function getCookie(c_name) {
        	if (document.cookie.length>0) {
            	c_start=document.cookie.indexOf(c_name + "=")
				if (c_start!=-1) { 
                	c_start=c_start + c_name.length+1 
					c_end=document.cookie.indexOf(";",c_start)
					if (c_end==-1) c_end=document.cookie.length
                    	return unescape(document.cookie.substring(c_start,c_end))
					} 
				}
			return null
		}
		onload=function(){
			document.getElementById('alwaysBig').checked = getCookie('alwaysBig')==1? true : false;
		}
		function set_check(){
			setCookie('alwaysBig', document.getElementById('alwaysBig').checked? 1 : 0, 100);
		}
	
		(function($) {
			jQuery.fn.exchangePicture = function() {
				return this.each(function() {
					$(this).click(function(event) {
						event.preventDefault();
						$("#picture").animate({
							height: '480',
							width: '640'
						}, 300, function() {});
						$("#picture").attr('src',"<?php echo $bigImageFilename ?>");
						$("#picture").attr('width',"640");
						$("#picture").attr('height',"480");
						$(".centralimages").css("width", "640");
						$("#magnify").css("display", "none");
/*
						$('.switchToBig').attr("title", "Shrink it again.");
						$('a.switchToBig').html("Make it small again...");
						$('.switchToBig').attr("class", "switchToSmall");
*/
						$('.switchToBig').remove();
						$('#sizeManipulation').append('<br/><input type="checkbox" id="alwaysBig" onchange="set_check();" <?php if ($doBig) {echo "checked";} ?> >Always do big!');
					});
				});
			};
		})(jQuery);
				
		$( document ).ready(function() {
			$('.switchToBig').exchangePicture();
			$('#magnify').exchangePicture();
		});
				
		$(function() {
			$( document ).tooltip({
				content: function() {
					return $(this).attr('title');
				},
				position: {
					my: "center bottom-20",
					at: "center top",
					using: function( position, feedback ) {
						$( this ).css( position );
						$( "<div>" )
						.addClass( "arrow" )
						.addClass( feedback.vertical )
						.addClass( feedback.horizontal )
						.appendTo( this );
					}
				}
			});
		});
		
		$(document).ready(function(){
			$('#bigQuestions').click(function() {
				$('#bigAnswers').slideToggle('slow');
			});
		});
		
		

/*
		$( document ).ready(function() {
			$('#magnify').exchangePicture();
			$('#magnify').click(function(event) {
				event.preventDefault();
				$(".centralimages").css("width", "640");
				$("#magnify").css("display", "none");
			});
		});
*/
	</script>

	<link rel="stylesheet" href="style.css" type="text/css" />
	
	<title>
		fair.andreasherten.de
	</title>
</head>


<body>
<div id="page">
	<h1><strong>FAIR</strong>progress</h1>
	<h2>The FAIR accelerator complex is currently constructed.<br/>Here's an <strong>animated gif</strong> of yesterday's construction site.</h2>
	<div class="centralimages" <?php if ($doBig) {echo "style='width: 640px;'";} ?> >
		<?php if ($doBig) : ?>
		<img id="picture" src="<?php echo $bigImageFilename ?>" alt="640x480" width="640" height="480"/>
		<?php else : ?>
		<i class="icon-resize-full" id="magnify" title="It actually is quite BIG! <br> <?php echo$bigImageFileSize ?>!"></i>
		<img id="picture" src="<?php echo $smallImageFilename ?>" alt="320x280" width="320" height="280"/>
		<?php endif; ?>
	</div>
	<p class="date"><small>Picture from <?php echo $dateYesterday ?></small></p>
	<p id="sizeManipulation">
		<?php if ($doBig) : ?>
		<br/><input type="checkbox" id="alwaysBig" onchange="set_check();" <?php if ($doBig) {echo "checked";} ?> >Always do big!
		<?php else : ?>
		<a href="" class="switchToBig" title="It actually is quite BIG! <br> <?php echo$bigImageFileSize ?>!"><button>Make it bigger!</button></a></p>
		<?php endif; ?>
	<div id="footer">
		<h2 id="bigQuestions">What? More? How? Who?!<!-- <i class="icon-collapse"></i> --></h2>
		<div id="bigAnswers">
			<h3>Background</h3>
			<p>Since 2012, the buildings for the international accelerator facility <a href="http://fair-center.eu/">FAIR</a> are being constructed. First, woodland was cleared, then the civil engineering started. In <a href="http://www.fair-center.eu/construction/how-fair-is-being-built.html">a few years</a>, where once stood trees one of the world's most advanced basic research facility will be located.<br/>
				There's a <a href="http://www.fair-center.eu/construction/webcam.html">webcam</a> taking pictures every 15 minutes. Based on these pictures FAIRprogress provides animated gifs for each day.</p>
			<h3>Archives</h3>
			<p>For the time being, all quarter-hourly pictures are archived as well as the animated gifs. Just check out the <a href="/images/">/images/ directory</a> of this website and go through the listings. They are sorted by year/month/date.</p>
			<h3>Techniques</h3>
			<p>A cronjob <span class="code">wgets</span> the picture every 15 minutes. Every night, ImageMagick's <span class="code">convert</span> produces a small, lossy gif animation as well as a big lossless one. (Do you have ideas for <a href="techniques.html">better looking configurations</a> of <span class="code">convert</span>? Just let me know.)<br/>This website per default shows the small one. A click will display the big picture - but prepare for long loading time, the file is about <?php echo$bigImageFileSize ?>.</p>
			<h3>Who?</h3>
			<p>Hi. I'm <a href="http://www.andreasherten.de/">Andreas</a>.<br/>
			I'm doing my PhD at <a href="http://www-panda.gsi.de/">PANDA</a>, one of the experiments located at FAIR.<br/>
			Say <a href="http://www.andreasherten.de/fb">hi</a>!</p>
		</div>
	</div>
</div>
<footer>
	Made with 
	<?php
		$madeWith = array(
			'Electrons',
			'Coda',
			'jQuery and PHP',
			'Photons',
			'Rare Earths',
			'Pi',
			'CP Violation',
			'Newton\'s Laws',
			'Stardust',
		);
		shuffle($madeWith);
		echo reset($madeWith);
	?>
	<br/>
	by <a href="http://www.andreasherten.de/">Andreas Herten</a>.
</footer>
</body> 
</html> 
        