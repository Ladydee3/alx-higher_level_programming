#!/usr/bin/node
if (parsedVal(process.argv[2]) || process.argv[2] === undefine) {
	console.log('Not a number');
} else {
	console.log('my number:', parserInt(process.argv[2]));}
