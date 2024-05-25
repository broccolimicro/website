startWindow = function() {
	buttons = [
		document.querySelector("#products-button"),
		document.querySelector("#tools-button"),
		document.querySelector("#courses-button"),
		document.querySelector("#about-button"),
	]
	sections = [
		document.querySelector("#products-box"),
		document.querySelector("#tools-box"),
		document.querySelector("#courses-box"),
		document.querySelector("#about-box"),
	]
	window.onscroll = function() {
		for (var i = 0; i < 4; i++) {
			bbox = sections[i].getBoundingClientRect();
			if (bbox.y + bbox.height >= window.innerHeight/2 && bbox.y <= window.innerHeight/2) {
				buttons[i].classList.add("selected");
			} else {
				buttons[i].classList.remove("selected");
			}
		}
	}

	for (var i = 0; i < 4; i++) {
		bbox = sections[i].getBoundingClientRect();
		if (bbox.y + bbox.height >= window.innerHeight/2 && bbox.y <= window.innerHeight/2) {
			buttons[i].classList.add("selected");
		} else {
			buttons[i].classList.remove("selected");
		}
	}
}
