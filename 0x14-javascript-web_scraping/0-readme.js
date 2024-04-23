#!/usr/bin/node

const fileName = process.argv[2];
const fs = reqire('fs');

fs.readfile(filename, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	}
	console.log(data);
});
