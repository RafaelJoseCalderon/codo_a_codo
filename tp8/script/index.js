/**############################################################################################################## */
document.getElementById("idHeader").outerHTML = `
	<header class="d-none d-md-block py-lg-1 py-xl-1 px-lg-5 px-xl-5">
		<h1 class="c-marron-2 font-italic font-weight-bold text-center align-middle py-2 padding bg-light m-0 border">
			Chocolates
		</h1>
	</header>
`;

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

const navBar = (prefijo = "") => {
	let referencias = [
		{referencia: prefijo + "index.html",etiqueta: "Inicio"},
		{referencia: prefijo + "about.html",etiqueta: "Acerca de"},
		{referencia: prefijo + "contact.html",etiqueta: "Contacto"},
		{referencia: prefijo + "form.html",etiqueta: "Registrese"},
		{referencia: prefijo + "location.html",etiqueta: "Sucursales"},
		{referencia: prefijo + "client.html",etiqueta: "Clientes"}
	];
	document.getElementById("idNav").outerHTML = cuerpoNavBar(referencias.map(botonNavBar).join(""));
}

/**############################################################################################################## */
document.getElementById("idFooter").outerHTML = `
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

document.getElementById("idMain").className += `
	col-lg-12
	col-md-8
	col-sm-12
`;
