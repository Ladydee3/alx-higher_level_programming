!#/usr/bin/node

let numberOfTimes = parseInt(process.argv[2]);
if (!isNaN(numberOfTimes)) {
	while (numberOfTimes > 0) {
		console.log('C is fun');
		numberOftimes -= 1;
	}
} else {
	console.log('Missing number of occurences');
}
