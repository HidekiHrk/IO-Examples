process.stdin.setRawMode(true); // Caso não queira pegar todas as teclas instantaneamente, remova esta linha

process.stdin.on('data', (data) => {
    if(data == '\u0003'){
        process.exit(0);
    }
    process.stdout.write(`Tecla: ${data}\n`);
});
