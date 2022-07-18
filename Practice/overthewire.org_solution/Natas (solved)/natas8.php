<?php
$secret = "3d3d516343746d4d6d6c315669563362";
print(base64_decode(strrev(hex2bin(($secret)))));