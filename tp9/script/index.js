/**############################################################################################################## */
const header = `
	<header class="d-none d-md-block py-lg-1 py-xl-1 px-lg-5 px-xl-5">
		<h1 class="c-marron-2 font-italic font-weight-bold text-center align-middle py-2 padding bg-light m-0 border">
			Chocolates
		</h1>
	</header>
`;
document.getElementById("idHeader").outerHTML = header;

/**############################################################################################################## */
const botonNavBar = (obj) => {
	return `
		<li class="nav-item col-xl-2 col-lg-2 col-md-12 text-center p-0">
		<a class="nav-link m-1 p-0 text-white border btn bc-marron-4 hbc-marron-1"
			href="${obj.referencia}">${obj.etiqueta}</a>
		</li>
	`
};

const cuerpoNavBar = (arrayDeBotones) => {
	return `
		<nav class="sticky-top col-lg-12 col-md-4 col-sm-12 py-0 px-sm-2 px-md-2 px-lg-0 px-xl-0
					navbar navbar-expand-md bg-white bc-marron-md-2 align-items-md-start">

			<div class="c-marron-2 font-italic font-weight-bold d-sm-block d-md-none navbar-brand">
				Chocolates
			</div>

			<!-- Boton hamburguesa -->
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
				<span class="fa fa-bars c-marron-2"></span>
			</button>

			<div class="m-0 p-0 w-100 collapse navbar-collapse" id="collapsibleNavbar">
				<ul class="	navbar-nav w-100 d-flex flex-md-column flex-lg-row m-0 p-0 justify-content-between
							c-marron-2 bc-marron-2 bc-transparente-lg">
					${arrayDeBotones}
				</ul>
			</div>
		</nav>
	`
};

const referencias = () => {
	return [{
			referencia: "index.html",
			etiqueta: "Inicio"
		},
		{
			referencia: "about.html",
			etiqueta: "Acerca de"
		},
		{
			referencia: "contact.html",
			etiqueta: "Contacto"
		},
		{
			referencia: "form.html",
			etiqueta: "Registrese"
		},
		{
			referencia: "location.html",
			etiqueta: "Sucursales"
		},
		{
			referencia: "client.html",
			etiqueta: "Clientes"
		}
	];
}

document.getElementById("idNav").outerHTML = cuerpoNavBar(referencias().map(botonNavBar).join(""));

/**############################################################################################################## */
const footer = `
<footer class="py-3 d-flex flex-column bc-marron-3">
	<p class="m-auto">
		<a class="text-decoration-none fa fa-2x fa-inverse fa-twitter" href="https://twitter.com"></a>
		<a class="text-decoration-none fa fa-2x fa-inverse fa-facebook" href="https://es-la.facebook.com"></a>
		<a class="text-decoration-none fa fa-2x fa-inverse fa-pinterest" href="https://ar.pinterest.com"></a>
		<a class="text-decoration-none fa fa-2x fa-inverse fa-instagram" href="https://www.instagram.com"></a>
		<a class="text-decoration-none fa fa-2x fa-inverse fa-linkedin" href="https://www.linkedin.com"></a>
	</p>
	<p class="m-auto">Derechos reservados @2020</p>
</footer>
`;
document.getElementById("idFooter").outerHTML = footer;

/**############################################################################################################## */
/** carousel para el index */
const carousel = (lista) => {
	let numeracionCarousel = `<li data-target="#carousel" data-slide-to="0" class="active"></li>`;
	let listaImagenesCarousel = `<div class="carousel-item active"><img src="${lista[0]}"></div>`

	for (let i = 1; i < lista.length; i++) {
		numeracionCarousel += `<li data-target="#carousel" data-slide-to="${i}"></li>`;
		listaImagenesCarousel += `<div class="carousel-item"> <img src="${lista[i]}"></div>`
	}

	return `
		<div id="carousel" class="carousel slide mx-auto" data-ride="carousel">
			<ul class="carousel-indicators">${numeracionCarousel}</ul>
			<div class="carousel-inner">${listaImagenesCarousel}</div>
			<a class="carousel-control-prev" href="#carousel" data-slide="prev">
				<span class="carousel-control-prev-icon"></span>
			</a>
			<a class="carousel-control-next" href="#carousel" data-slide="next">
				<span class="carousel-control-next-icon"></span>
			</a>
		</div>
	`;
}

if (document.getElementById("carousel")) {
	document.getElementById("carousel").outerHTML = carousel(listaCarousel);
}

/**############################################################################################################## */
/** seccion para el index */
const recuadro = (obj) => {
	let href = !obj.href ? "producto.html" : ""; // chanchada, corregir luego
	return `
		<a	class="m-2 text-decoration-none text-black-50"
			onclick="localStorage.setItem('id_producto', '${obj.id}')" href="${href}"
		>
			<img class="rounded border shadow-lg bg-white" src="${obj.src}" alt="imagen no disponible">
			<h4 class="mt-n5 text-center">"${obj.h4}"</h4>
		</a>
	`;
};

const seccion = (titulo, arrayElementos) => {
	return `
		<section class="my-4">
		<h5 class="p-1 text-white bc-marron-2">${titulo}</h5>
		<div class="d-flex flex-wrap justify-content-around">
			${arrayElementos}
		</div>
		</section>
	`;
};

if (document.getElementById("seccion1") && document.getElementById("seccion2")) {
	document.getElementById("seccion1").outerHTML = seccion("Seccion 1", indexSeccion1.map(recuadro).join(""));
	document.getElementById("seccion2").outerHTML = seccion("Seccion 2", indexSeccion2.map(recuadro).join(""));
}

/**############################################################################################################## */
/** productos */
const item = (producto) => {
	return `
		<main class="col-lg-12 col-md-8 col-sm-12 p-2 d-flex flex-column align-items-center justify-items-center"> <br>
			<h4 class="c-marron-2 font-italic font-weight-bold">${producto.titulo}</h4>
			<img class="m-2 rounded border shadow-lg bg-white" src="${producto.imagen}">
			<p class="font-italic">${producto.descripcion}</p>
			<p class="font-italic font-weight-bold c-marron-3">${producto.precio}</p>
		</main>
	`;
}

if (document.getElementById("producto")) {
	let producto = productos[localStorage.getItem('id_producto')];
	document.getElementById("producto").outerHTML = item(producto);
}

/**############################################################################################################## */
/** cajas para el sucursales */
/** La verdad no se si amerita, qué tan rapido cambian los clientes? */
const recuadroMap = (obj) => {
	return `
		<div class="card m-2">
			<div class="card-header">${obj.titulo}</div>
			<div class="card-body p-0">
				<iframe src="${obj.referencia}" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0" frameborder="0"></iframe>
			</div>
		</div>
	`;
}

if (document.getElementById("sucursales")) {
	document.getElementById("sucursales").outerHTML = `
		<div class="d-flex flex-wrap justify-content-around">
			${listaDeSucursales.map(recuadroMap).join("")}
		</div>
	`;
}

/**############################################################################################################## */
/** cajas para el clientes */
/** La verdad no se si amerita, qué tan rapido cambian los clientes? */
if (document.getElementById("clientes")) {
	document.getElementById("clientes").outerHTML = `
		<div class="d-flex flex-wrap justify-content-around">
			${listaDeClientes.map(recuadro).join("")}
		</div>
	`;
}

/**############################################################################################################## */
document.getElementById("idBody").className = `
	d-flex
	flex-column
	m-0
	h-100
`;

document.getElementById("idSubBody").className = `
	media-body
	row align-content-start
	align-content-md-stretch
	align-content-lg-start
	align-content-xl-start
	w-100 m-0 px-lg-5 px-xl-5
`;

if (document.getElementById("idMain")) {
	document.getElementById("idMain").className += `
		col-lg-12
		col-md-8
		col-sm-12
	`;
}

if (document.getElementById("tituloSubCuerpo")) {
	document.getElementById("tituloSubCuerpo").className = `
		c-marron-2
		font-italic
		font-weight-bold
	`;
}