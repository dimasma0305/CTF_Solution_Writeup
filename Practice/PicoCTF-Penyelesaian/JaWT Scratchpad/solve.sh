#!/bin/sh
wordlist="/usr/share/wordlists/rockyou.txt"
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYXNkIn0.IVXHienlYe-IglDGEe3PCWiS3BJl5yzhlYLep1TlN0g">token.jwt
john token.jwt --format=HMAC-SHA256 --wordlist=$wordlist
