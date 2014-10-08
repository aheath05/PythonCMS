<!DOCTYPE>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title id='title'>Chapter 3</title>
 
    </head>
    <body>
    

<?php
echo "<h1>Chapter 3</h1>";
echo "<hr>";
echo "<h2>Musical Notes</h2>\n";
$MusicalScale = array("do", "re", "mi", "fa", "so", "la", "ti");
$OutputString ="The notes of the musical scale are: " ;
foreach( $MusicalScale as $CurrentNote)
	 $OutputString .= " " . $CurrentNote;
	 echo "<p>$OutputString</p>";
for($i = 0; $i < count($MusicalScale); ++$i)
	echo "<p> {$MusicalScale[$i]} </p>";
echo "<hr>";
echo "<h2>Formatted Text</h2>\n";

$DisplayValue=9.876;
echo "<pre>\n";
echo "Unformatted Text line 1. ";
echo "Unformatted text line 2. ";
echo "$DisplayValue = $DisplayValue";
echo "</pre>\n";

echo "<pre>\n";
echo "Formatted Text line 1. \r\n";
echo "\tFormatted text line 2. \r\n";
echo "\$DisplayValue = $DisplayValue";
echo "</pre>\n";


echo "<hr>";
echo "<h2>Books and Authors</h2>\n";

$Books = array("The Adventures of Hucleberry Finn", "Nineteen Eighty-Four", "Alice's Adventures in Wonderland", "The Cat in the Hat");
$Authors = array("Mark Twain", "George Orwell", "Lewis Carroll", "Dr. Seuss");
$RealNames = array("Samuel Clemens", "Eric Blaire", "Charles Dodgson - The Mathemetician", "Theodor Geisel");

for($i = 0; $i < count($Books); ++$i)
	echo "<p>The ream name of {$Authors[$i]}, " . 
			"the author of {$Books[$i]}, " . "is {$RealNames[$i]}.</p>";
			
			
echo "<hr>";
echo "<h2>Title Information</h2>\n";

for($i = 0; $i < count($Books); ++$i)
	echo "<p>The Title \"{$Books[$i]}\" contains " .
	strlen($Books[$i]) . " characters and " .
	str_word_count($Books[$i]) . " words.</p>";
	
echo "<hr>";
echo "<h2>Word Play</h2>\n";

$startingText ="mAdAm, i'M aDaM.";

$uppercaseText = strtoupper($startingText);
$lowercaseText = strtolower($startingText);
echo "<p>$uppercaseText</p>\n";
echo "<p>$lowercaseText</p>\n";

echo "<p>" . ucfirst($lowercaseText) . "</p>\n";
echo "<p>" . lcfirst($uppercaseText) . "</p>\n";
$workingText = ucwords($lowercaseText);
echo "<p>$workingText</p>\n";
echo "<hr>";

echo "<p>" . md5($workingText) . "</p>\n";
echo "<p>" . substr($workingText,0,6) . "</p>\n";
echo "<p>" . substr($workingText,7) . "</p>\n";
echo "<p>" . strrev($workingText) . "</p>\n";
echo "<p>" . str_shuffle($workingText) . "</p>\n";

echo "<hr>";
echo "<h2>E-Mail Validator</h2>\n";

$emailAddresses = array("johnsmith@php.test", "mary.smith.mail.php.example",
"john.jones@php.invalid", "alan.smithee@test", "jsmith456@example.com", 
"jsmith456@test", "mjones@example", "mjones@example.org");

function validateAddress($address){
if(strpos($address, '@') !== FALSE && strpos($address, '.') !== FALSE)
	return TRUE;
else
	return FALSE;
}

foreach ($emailAddresses as $address)
{
	if(validateAddress($address) ==FALSE)
		echo "<p>The email address <em>$address</em> does not appear to be valid.</p>\n";
}

?>
</body>
</html>
