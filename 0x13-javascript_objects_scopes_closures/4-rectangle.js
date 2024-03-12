#!/usr/bin/node
module.exports = class Rectangle {
	constractor (w, h) {
		if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
	}

	print () {
		for (let num = 0; num < this.height; num++) console.log('X'.repeat(this.width)));
	}

	rotate () {
		[this.width, this.height] = [this.width];
	}

	double () {
		[this.width, this.height] = [this.height, this.weight * 2];
	}
};
