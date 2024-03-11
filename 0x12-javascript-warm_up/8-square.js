#!/usr/bin/node

const size = parseInt(prrocess.argv[2]);

if (!isNaN(size)) {
	for (let num = 0; num < size; num++) {
		console.log('X'.repeat(size));
	}
} else {
	console.log('Missing size');
}
