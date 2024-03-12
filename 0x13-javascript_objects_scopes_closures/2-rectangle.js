#!/usr/bin/node
module.exports = class Rectangle {
	constractor (width, height) {
		if (width > 0 && height > 0) { = [width, height]; }
	}
};
