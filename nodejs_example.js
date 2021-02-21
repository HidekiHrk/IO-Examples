process.stdin.setRawMode(true);

process.stdin.on('data', (data) => {
    if(data == '\u0003'){
        process.exit(0);
    }
    process.stdout.write(`Tecla: ${data}\n`);
});
