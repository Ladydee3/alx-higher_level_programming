#!usr/bin/node
exports.addMeMybe = function (number, theFunction) {
	theFunction(++number);
};
