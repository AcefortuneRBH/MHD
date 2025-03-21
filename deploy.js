const { exec } = require('child_process');

exec('bash untitled:/deploy.sh', (error, stdout, stderr) => {
  if (error) {
	console.error(`Error: ${error.message}`);
	return;
  }
  if (stderr) {
	console.error(`Stderr: ${stderr}`);
	return;
  }
  console.log(`Stdout: ${stdout}`);
});