wget http://mercury.picoctf.net:26318/JIFxzHyW8W -q -O script.wasm
wasm-decompile  script.wasm -o script.decompile.c
wasm2c  script.wasm -o script.c
wasm2wat --generate-names script.wasm > script.wat