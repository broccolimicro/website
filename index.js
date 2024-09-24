startWindow = function() {
	let scrollHeight = Math.max(
		document.body.scrollHeight, document.documentElement.scrollHeight,
		document.body.offsetHeight, document.documentElement.offsetHeight,
		document.body.clientHeight, document.documentElement.clientHeight
	);
	downarrow = document.querySelector("#downarrow");
	cellimgs = document.querySelector("#layout-example-imgs");
	cellidx = 0;
	cellcount = 6;
	const interval = setInterval(function() {
		cellidx++;
		cellstr = (cellidx%cellcount+1).toString().padStart(2,'0');
		cellimgs.src = "photo/cell_" + cellstr + ".png";
	}, 5000);

	buttons = [
		document.querySelector("#loom-button"),
		document.querySelector("#download-button"),
		document.querySelector("#sponsor-button"),
		document.querySelector("#about-button"),
	]
	sections = [
		document.querySelectorAll(".loom-box"),
		document.querySelectorAll("#download-box"),
		document.querySelectorAll("#sponsor-box"),
		document.querySelectorAll("#about-box"),
	]

	synthesize();
	simulate();
	layout();

	window.onscroll = function() {
		var value = Math.max(0, 300 - window.pageYOffset)/300;
		if (value > 0) {
			downarrow.style.display = "inline-block";
			downarrow.style.opacity = value;
		} else {
			downarrow.style.display = "none";
		}
			
		for (var i = 0; i < sections.length; i++) {
			bboxes = [...sections[i]]
				.map(el => el.getBoundingClientRect());
			var inside = false;
			for (const bbox of bboxes) {
				inside = inside || (bbox.y + bbox.height >= window.innerHeight/2 && bbox.y <= window.innerHeight/2);
			}
			if (inside) {
				buttons[i].classList.add("selected");
			} else {
				buttons[i].classList.remove("selected");
			}
		}
	}

	for (var i = 0; i < sections.length; i++) {
		bboxes = [...sections[i]]
				.map(el => el.getBoundingClientRect());

		var inside = false;
		for (const bbox of bboxes) {
			inside = inside || (bbox.y + bbox.height >= window.innerHeight/2 && bbox.y <= window.innerHeight/2);
		}
		if (inside) {
			buttons[i].classList.add("selected");
		} else {
			buttons[i].classList.remove("selected");
		}
	}
}

async function submitWhitepaper(event) {
	event.preventDefault();
	document.querySelector("#submit-whitepaper").setAttribute("disabled","");

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
			document.querySelector("#submit-whitepaper").removeAttribute("disabled");
			const errorText = await response.text();
			console.error('Error:', errorText);
			alert('Login failed: ' + errorText);
		}
	} catch (error) {
		document.querySelector("#submit-whitepaper").removeAttribute("disabled");
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

function textAreaAdjust(element) {
  element.style.height = "1px";
  element.style.height = (25+element.scrollHeight)+"px";
}

function synthesize() {
	var term = document.querySelector("#synthesis-example");
	var button = document.querySelector("#synthesis-button");
	if (button.hasAttribute("dataview")) {
		button.removeAttribute("dataview");
		term.innerHTML = `<b>$ lm wchb1b.hse</b> # generate the production rules
require driven, stable, noninterfering
@_12&R.t<1>|_Reset<3>&L.t<3>&R.e<3>->v3-
@_13&~R.t<1>|~_Reset<1>|~L.t<2>&~R.e<2>->v3+
@_12&R.f<1>|_Reset<3>&L.f<3>&R.e<3>->v2-
@_13&~R.f<1>|~_Reset<1>|~L.f<2>&~R.e<2>->v2+
_Reset<3>&v0<3>&L.e'1<3>->v1- {v0}
~_Reset<1>|~v0<1>|~L.e'1<1>->v1+
_Reset<3>&v1<3>&L.e'1<3>->v0- {v1}
~_Reset<1>|~v1<1>|~L.e'1<1>->v0+
R.f'1<1>|R.t'1<1>->R.e'1-
~R.t'1<2>&~R.f'1<2>->R.e'1+
v3<1>->R.t-
~v3<1>->R.t+
v2<1>->R.f-
~v2<1>->R.f+
R.f<1>|R.t<1>->L.e-
~R.t<2>&~R.f<2>->L.e+
v1<1>->L.t'1-
~v1<1>->L.t'1+
v0<1>->L.f'1-
~v0<1>->L.f'1+
Vdd<0.1>->_12- [weak]
~GND<0.1>->_13+ [weak]



<b>$ lm -n wchb1b.hse sky130.py</b> # generate the spice netlist
.subckt top GND Vdd
x0 L_0f_31 v0 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x1 L_0f_31 v0 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x2 L_0t_31 v1 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x3 L_0t_31 v1 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x4 L_0e R_0t GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x5 L_0e R_0f GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x6 L_0e R_0f __0 Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x7 __0 R_0t Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x8 R_0f v2 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x9 R_0f v2 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x10 R_0t v3 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x11 R_0t v3 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x12 R_0e_31 R_0t_31 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x13 R_0e_31 R_0f_31 GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x14 R_0e_31 R_0f_31 __1 Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x15 __1 R_0t_31 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x16 v0 L_0e_31 __2 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x17 __2 v1 __3 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x18 __3 __Reset GND GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x19 v0 L_0e_31 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x20 v0 v1 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x21 v0 __Reset Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x22 v1 L_0e_31 __4 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x23 __4 v0 __5 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x24 __5 __Reset GND GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x25 v1 L_0e_31 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x26 v1 v0 Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x27 v1 __Reset Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x28 v2 R_0e __6 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x29 __6 L_0f __7 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x30 __7 __Reset GND GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x31 v2 R_0e __8 Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x32 __8 L_0f Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x33 v2 __Reset Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x34 v3 R_0e __9 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x35 __9 L_0t __10 GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x36 __10 __Reset GND GND sky130_fd_pr__nfet_01v8 w=1.35u l=0.15u
x37 v3 R_0e __11 Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x38 __11 L_0t Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.9u l=0.15u
x39 v3 __Reset Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x40 __12 Vdd GND GND sky130_fd_pr__nfet_01v8 w=0.45u l=1.5u
x41 __13 GND Vdd Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=1.5u
x42 v2 R_0f __12 GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x43 v2 R_0f __13 Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
x44 v3 R_0t __12 GND sky130_fd_pr__nfet_01v8 w=0.45u l=0.15u
x45 v3 R_0t __13 Vdd sky130_fd_pr__pfet_01v8 w=0.45u l=0.15u
.ends
.end`
	} else {
		button.setAttribute("dataview","");
		term.innerHTML = `<b>$ cat wchb1b.hse</b>
(L.f-,L.t-; [L.e];
*[[ 1->L.f+
  : 1->L.t+
  ]; [~L.e]; L.f-,L.t-; [L.e]
 ])'1 ||

L.e+,R.f-,R.t-; [R.e & ~L.f & ~L.t];
*[[  R.e & L.f -> R.f+
  [] R.e & L.t -> R.t+
  ]; L.e-; [~R.e & ~L.f & ~L.t]; R.f-,R.t-; L.e+
 ] ||

(R.e+; [~R.f & ~R.t];
*[[R.f | R.t]; R.e-; [~R.f & ~R.t]; R.e+])'1`
	}
}

function layout() {
	var term = document.querySelector("#layout-example");
	var imgs = document.querySelector("#layout-example-imgs");
	var button = document.querySelector("#layout-button");
	if (button.hasAttribute("dataview")) {
		button.removeAttribute("dataview");
		term.style.display = "none";
		imgs.style.display = "inline-block";
 	} else {
		button.setAttribute("dataview","");
		term.style.display = "inline-grid";
		imgs.style.display = "none";
	}
}

function simulate(view) {
	var hsesim = `<b>$ lm sim wchb1b.hse</b> 
(hsesim)reset
(0) {3 8 2 1} ~L.f'1&~L.t'1&L.e'1&L.e&~R.f&~R.t&R.e&~L.f&~L.t&R.e'1&~R.f'1&~R.t'1
(hsesim)reset 0
(hsesim)tokens
L.e+,R.f-,R.t-,R.e+,L.f-,L.t- {
	(0) P3	L.e+; <here> [R.e&L.f->R.f+...[]R.e&L.t->R.t+...]
}
R.e'1+,R.f'1-,R.t'1- {
	(1) P8	[~R.f'1&~R.t'1]; R.e'1+; <here> R.f'1|R.t'1->R.e'1-
}
L.f'1-,L.t'1-,L.e'1+ {
	(2) P2	[~L.e'1]; L.t'1-; <here> [L.e'1->L.t'1+...[]L.e'1->L.f'1+...]
	(3) P1	[~L.e'1]; L.f'1-; <here> [L.e'1->L.f'1+...[]L.e'1->L.t'1+...]
}
(hsesim)enabled
(0) T1.0:L.e'1->L.t'1+

(1) T0.0:L.e'1->L.f'1+


(hsesim)fire 0
0	T1.0	L.e'1 -> L.t'1+
(hsesim)tokens
L.e+,R.f-,R.t-,R.e+,L.f- {
	(0) P3	L.e+; <here> [R.e&L.f->R.f+...[]R.e&L.t->R.t+...]
}
R.e'1+,R.f'1-,R.t'1- {
	(1) P8	[~R.f'1&~R.t'1]; R.e'1+; <here> R.f'1|R.t'1->R.e'1-
}
L.f'1-,L.t'1+,L.e'1+ {
	(2) P0	[...[L.e'1]; L.f'1+[]...[L.e'1]; L.t'1+]; <here> ~L.e'1->L.f'1-
	(3) P10	[...[L.e'1]; L.f'1+[]...[L.e'1]; L.t'1+]; <here> ~L.e'1->L.t'1-
}
(hsesim)enabled
(0) T5.0:R.e&L.t->R.t+


(hsesim)step 100
282	T5.0	R.e&L.t -> R.t+
1158	T6.0	1 -> L.e-
6697	T3.0	~L.e'1 -> L.t'1-
7987	T10.0	R.t'1 -> R.e'1-
10374	T8.0	~R.e&~L.f&~L.t -> R.t-
15836	T11.0	~R.f'1&~R.t'1 -> R.e'1+
15903	T9.0	1 -> L.e+
16983	T1.0	L.e'1 -> L.t'1+
17820	T5.0	R.e&L.t -> R.t+
19395	T6.0	1 -> L.e-
19534	T3.0	~L.e'1 -> L.t'1-
20833	T10.0	R.t'1 -> R.e'1-
24842	T8.0	~R.e&~L.f&~L.t -> R.t-
24917	T11.0	~R.f'1&~R.t'1 -> R.e'1+
27183	T9.0	1 -> L.e+
28924	T0.0	L.e'1 -> L.f'1+
29060	T4.0	R.e&L.f -> R.f+
30736	T10.0	R.f'1 -> R.e'1-
30842	T6.0	1 -> L.e-
32289	T2.0	~L.e'1 -> L.f'1-
38749	T7.0	~R.e&~L.f&~L.t -> R.f-
40202	T11.0	~R.f'1&~R.t'1 -> R.e'1+
40541	T9.0	1 -> L.e+
46842	T1.0	L.e'1 -> L.t'1+
52522	T5.0	R.e&L.t -> R.t+
54122	T6.0	1 -> L.e-
54426	T10.0	R.t'1 -> R.e'1-
54660	T3.0	~L.e'1 -> L.t'1-
57011	T8.0	~R.e&~L.f&~L.t -> R.t-
59191	T11.0	~R.f'1&~R.t'1 -> R.e'1+
60167	T9.0	1 -> L.e+
63362	T1.0	L.e'1 -> L.t'1+
63638	T5.0	R.e&L.t -> R.t+
63976	T6.0	1 -> L.e-
65154	T10.0	R.t'1 -> R.e'1-
67849	T3.0	~L.e'1 -> L.t'1-
70194	T8.0	~R.e&~L.f&~L.t -> R.t-
71616	T9.0	1 -> L.e+
75310	T0.0	L.e'1 -> L.f'1+
75562	T11.0	~R.f'1&~R.t'1 -> R.e'1+
80737	T4.0	R.e&L.f -> R.f+
81030	T6.0	1 -> L.e-
81919	T10.0	R.f'1 -> R.e'1-
82339	T2.0	~L.e'1 -> L.f'1-
82722	T7.0	~R.e&~L.f&~L.t -> R.f-
82780	T9.0	1 -> L.e+
82862	T1.0	L.e'1 -> L.t'1+
83780	T11.0	~R.f'1&~R.t'1 -> R.e'1+
85533	T5.0	R.e&L.t -> R.t+
89026	T6.0	1 -> L.e-
90274	T3.0	~L.e'1 -> L.t'1-
93486	T10.0	R.t'1 -> R.e'1-
93502	T8.0	~R.e&~L.f&~L.t -> R.t-
93675	T11.0	~R.f'1&~R.t'1 -> R.e'1+
95883	T9.0	1 -> L.e+
96289	T0.0	L.e'1 -> L.f'1+
97052	T4.0	R.e&L.f -> R.f+
97983	T10.0	R.f'1 -> R.e'1-
100135	T6.0	1 -> L.e-
107983	T2.0	~L.e'1 -> L.f'1-
109823	T7.0	~R.e&~L.f&~L.t -> R.f-
111488	T9.0	1 -> L.e+
115723	T0.0	L.e'1 -> L.f'1+
116743	T11.0	~R.f'1&~R.t'1 -> R.e'1+
121488	T4.0	R.e&L.f -> R.f+
126354	T10.0	R.f'1 -> R.e'1-
128594	T6.0	1 -> L.e-
135987	T2.0	~L.e'1 -> L.f'1-
137146	T7.0	~R.e&~L.f&~L.t -> R.f-
140599	T9.0	1 -> L.e+
142793	T0.0	L.e'1 -> L.f'1+
142892	T11.0	~R.f'1&~R.t'1 -> R.e'1+
143119	T4.0	R.e&L.f -> R.f+
146144	T10.0	R.f'1 -> R.e'1-
147139	T6.0	1 -> L.e-
149484	T2.0	~L.e'1 -> L.f'1-
150039	T7.0	~R.e&~L.f&~L.t -> R.f-
150352	T11.0	~R.f'1&~R.t'1 -> R.e'1+
150364	T9.0	1 -> L.e+
152278	T0.0	L.e'1 -> L.f'1+
155681	T4.0	R.e&L.f -> R.f+
158079	T10.0	R.f'1 -> R.e'1-
162326	T6.0	1 -> L.e-
162599	T2.0	~L.e'1 -> L.f'1-
163396	T7.0	~R.e&~L.f&~L.t -> R.f-
168226	T11.0	~R.f'1&~R.t'1 -> R.e'1+
170156	T9.0	1 -> L.e+
170500	T1.0	L.e'1 -> L.t'1+
170862	T5.0	R.e&L.t -> R.t+
171896	T10.0	R.t'1 -> R.e'1-
172541	T6.0	1 -> L.e-
176008	T3.0	~L.e'1 -> L.t'1-
176015	T8.0	~R.e&~L.f&~L.t -> R.t-
186015	T9.0	1 -> L.e+
186505	T0.0	L.e'1 -> L.f'1+
186666	T11.0	~R.f'1&~R.t'1 -> R.e'1+
188943	T4.0	R.e&L.f -> R.f+
190233	T10.0	R.f'1 -> R.e'1-
191863	T6.0	1 -> L.e-
193067	T2.0	~L.e'1 -> L.f'1-`;

	var prsim = `<b>$ lm sim wchb1b.prs</b>
(prsim)reset
(prsim)tokens
GND-,Vdd+,L.f'1~,v0~,L.t'1~,v1~,L.e~,R.f~,R.t~,v2~,v3~,R.e'1~,R.f'1~,R.t'1~,_Reset-,L.e'1~,L.f~,R.e~,L.t~,_0~,_1~,_2~,_3~,_4~,_5~,_6~,_7~,_8~,_9~,_10~,_11~
(prsim)s100
478	~_Reset->v3+
1407	~_Reset->v1+
prs/simulator.cpp:382: error: interference L.e
prs/simulator.cpp:382: error: interference R.e'1
2157	v3->R.t-
2659	~_Reset->v0+
4769	~_Reset->v2+
4977	v1->L.t'1-
5275	v0->L.f'1-
5778	~_Reset->v3+
6171	~_Reset->v2+
6989	~_Reset->v1+
10137	v2->R.f-
11159	~R.t->L.e+
11730	~_Reset->v0+
11850	~_Reset->v1+
14897	~R.t'1->R.e'1+
15589	1->L.f-
16368	1->L.t-
16755	~_Reset->v2+
17397	~_Reset->v3+
(prsim)tokens
GND-,Vdd+,L.f'1-,v0+,L.t'1-,v1+,L.e+,R.f-,R.t-,v2+,v3+,R.e'1+,R.f'1-,R.t'1-,_Reset-,L.e'1+,L.f-,R.e+,L.t-,_0+,_1+,_2-,_3-,_4-,_5-,_6~,_7-,_8~,_9~,_10-,_11~
(prsim)run
(prsim)enabled
(3) _Reset->v0- {v1}
(5) _Reset->v1- {v0}
(prsim)fire 3
18975	_Reset->v0- {v1}
(prsim)enabled
(2) ~v0->L.f'1+
(5) ~v0->v1+
(prsim)tokens
GND-,Vdd+,L.f'1-,v0-,L.t'1-,v1+,L.e+,R.f-,R.t-,v2+,v3+,R.e'1+,R.f'1-,R.t'1-,_Reset+,L.e'1+,L.f-,R.e+,L.t-,_0+,_1+,_2-,_3-,_4~,_5-,_6~,_7-,_8~,_9~,_10-,_11~
(prsim)step 100
17564	~v0->v1+
18568	~v0->L.f'1+
18728	_Reset->v2-
21974	~v2->R.f+
22183	R.f'1->R.e'1-
22573	~L.t->v3+
26582	R.f->L.e-
26847	~L.e'1->v0+
28720	~L.e'1->v1+
28757	v0->L.f'1-
38757	~L.f->v2+
39133	v2->R.f-
40834	~R.t'1->R.e'1+
43894	~R.t->L.e+
44067	_Reset->v0- {v1}
46233	~v0->v1+
52361	~v0->L.f'1+
54499	_Reset->v2-
55544	~v2->R.f+
55716	R.f'1->R.e'1-
57713	R.f->L.e-
59013	~L.t->v3+
61249	~L.e'1->v0+
61727	~L.e'1->v1+
62685	v0->L.f'1-
72576	~L.f->v2+
72820	v2->R.f-
73220	~R.t'1->R.e'1+
73774	~R.t->L.e+
76090	_Reset->v1- {v0}
77882	~v1->L.t'1+
78057	~v1->v0+
79465	_Reset->v3-
82731	~v3->R.t+
83400	R.t'1->R.e'1-
83905	R.t->L.e-
84665	~L.e'1->v1+
84831	~L.f->v2+
86075	v1->L.t'1-
88755	~L.t->v3+
88846	v3->R.t-
89351	~R.t'1->R.e'1+
92820	~R.t->L.e+
93905	_Reset->v0- {v1}
96589	~v0->v1+
97580	~v0->L.f'1+
98529	_Reset->v2-
101601	~v2->R.f+
102408	R.f->L.e-
102834	~L.e'1->v0+
103399	v0->L.f'1-
103746	R.f'1->R.e'1-
104173	~L.e'1->v1+
105596	~L.t->v3+
106103	~L.f->v2+
106339	v2->R.f-
109003	~R.t->L.e+
109261	~R.t'1->R.e'1+
109639	_Reset->v0- {v1}
109808	~v0->L.f'1+
112725	_Reset->v2-
113322	~v2->R.f+
113465	~v0->v1+
114272	R.f'1->R.e'1-
114454	R.f->L.e-
115989	~v0&~L.e'1->v1+
116471	~L.t->v3+
117119	~L.e'1->v0+
117709	~L.e'1->v1+
118285	v0->L.f'1-
119437	~L.f->v2+
120047	v2->R.f-
121167	~R.t->L.e+
121358	_Reset->v1- {v0}
121485	~R.t'1->R.e'1+
121572	~v1->v0+
126774	~v1->L.t'1+
127054	_Reset->v3-
127227	~v3->R.t+
130332	R.t'1->R.e'1-
131421	R.t->L.e-
131671	~L.e'1->v1+
132058	~L.f->v2+
132957	~L.e'1->v0+
137646	v1->L.t'1-
147646	~L.t->v3+
147944	v3->R.t-
151608	~R.t'1->R.e'1+
153129	~R.t->L.e+
155650	_Reset->v0- {v1}
157613	~v0->v1+
159127	~v0->L.f'1+
160043	_Reset->v2-
165887	~v2->R.f+
167214	R.f->L.e-
169289	R.f'1->R.e'1-
172922	~L.t->v3+
173069	~L.e'1->v0+
174438	v0->L.f'1-
176217	~L.f->v2+`;

	var term = document.querySelector("#simulate-example");
	var term2 = document.querySelector("#simulate-example-main");
	var imgs = document.querySelector("#simulate-example-imgs");
	var button = document.querySelector("#simulate-button");
	console.log(button.getAttribute("datastep"));
	var step = (Number(button.getAttribute("datastep"))+1)%4;
	console.log(step);	
	button.setAttribute("datastep", step);
	if (step == 0) {
		term.innerHTML = hsesim;
		imgs.src="photo/hsesim.png";
		term2.style.display = "none";
		imgs.style.display = "inline-block";
	} else if (step == 1) {
		term2.style.display = "inline-grid";
		imgs.style.display = "none";
	} else if (step == 2) {
		term.innerHTML = prsim;
		imgs.src="photo/prsim.png";
		term2.style.display = "none";
		imgs.style.display = "inline-block";
	} else {
		term2.style.display = "inline-grid";
		imgs.style.display = "none";
	}
}
