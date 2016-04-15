<?php
	$result = shell_exec('python boat_scrapy.py \'{"Marinas":"Carrick on Shannon", "nights":3, "people":4, "date":"24/03/2016"}\'');

	print $result;
?>
