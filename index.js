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

async function submitWhitepaper(event) {
	event.preventDefault();

	// Get form data
	const form = event.target;
	const formData = new FormData(form);
	const data = new URLSearchParams(formData);

	try {
		// Send the POST request to the backend
		const response = await fetch('/whitepaper.py', {
			method: 'POST',
			body: data,
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
			},
		});

		if (response.ok) {
			// Handle successful response
			document.cookie = 'whitepaper=1; path=/;';
			window.location.href = '/BroccoliWhitepaper.pdf'; // Redirect to the index page
		} else {
			// Handle errors
			const errorText = await response.text();
			console.error('Error:', errorText);
			alert('Login failed: ' + errorText);
		}
	} catch (error) {
		console.error('Error:', error);
		alert('An error occurred: ' + error.message);
	}
}

function toggleMenu() {
	var menu = document.querySelector("#menu");
	if (menu.style.display == 'block') {
		menu.style.display = 'none';
	} else {
		menu.style.display = 'block';
	}
}
