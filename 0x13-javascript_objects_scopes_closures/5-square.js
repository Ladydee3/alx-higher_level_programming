#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
	constractor (size) {
		super(size, size);
	}
};
