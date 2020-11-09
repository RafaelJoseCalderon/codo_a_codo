/**############################################################################################################## */
Vue.component('header-vue', {
	template: `
		<header class="d-none d-md-block py-lg-1 py-xl-1 px-lg-5 px-xl-5">
			<h1 class="c-marron-2 font-italic font-weight-bold text-center align-middle py-2 padding bg-light m-0 border">
				Chocolates
			</h1>
		</header>
	`
});

/**############################################################################################################## */
Vue.component('nav-vue', {
	props: ['botones'],
	template: `
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
					<button-nav-vue
						v-for="boton in botones"
						:referencia=boton.referencia
						:etiqueta=boton.etiqueta>
					</button-nav-vue>
				</ul>
			</div>
		</nav>
	`
});

Vue.component('button-nav-vue', {
	props: ["referencia", 'etiqueta'],
	template: `
		<li class="nav-item col-xl-2 col-lg-2 col-md-12 text-center p-0">
		<a class="nav-link m-1 p-0 text-white border btn bc-marron-4 hbc-marron-1"
			@click="app.view=referencia; console.log(app.view);">{{etiqueta}}</a>
		</li>
	`
});

/**############################################################################################################## */
Vue.component('footer-vue', {
	template: `
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
	`
});

/**############################################################################################################## */
// varios
Vue.component('recuadro', {
	props: ['imagen'],
	template: `
		<a	class="m-2 text-decoration-none text-black-50"
			@click="app.id_producto=imagen.id; console.log(app.id_producto); app.view=imagen.href; console.log(app.view);"
		>
			<img class="rounded border shadow-lg bg-white" :src="imagen.src" alt="imagen no disponible">
			<h4 class="position-relative mt-n5 mb-5 text-center">{{imagen.h4}}</h4>
		</a>
	`
});

Vue.component('h4-vue', {
	props: ['titulo'],
	template: `
		<h4 class="c-marron-2 font-italic font-weight-bold">{{titulo}}</h4>
	`
});

/**############################################################################################################## */
// index
Vue.component('carousel', {
	props: ['imagenes'],
	methods: {
		activarPrimero: function(index) {
			return index == 0 ? "active" : ""
		}
	},
	template: `
		<div id="carousel" class="carousel slide mx-auto" data-ride="carousel">
			<ul class="carousel-indicators">
				<li
					data-target="#carousel"
					v-for="(item, index) in imagenes"
					:data-slide-to="index"
					:class=activarPrimero(index)>
				</li>
			</ul>
			<div class="carousel-inner">
				<div
					class="carousel-item"
					v-for="(item, index) in imagenes"
					:class=activarPrimero(index)>
					<img :src="item">
				</div>
			</div>
			<a class="carousel-control-prev" href="#carousel" data-slide="prev">
				<span class="carousel-control-prev-icon"></span>
			</a>
			<a class="carousel-control-next" href="#carousel" data-slide="next">
				<span class="carousel-control-next-icon"></span>
			</a>
		</div>
	`
});

Vue.component('seccion-vue', {
	props: ['titulo', 'imagenes'],
	template: `
		<section class="m-0">
			<h5 class="p-1 text-white bc-marron-2">{{titulo}}</h5>
			<div class="d-flex flex-wrap justify-content-around">
				<recuadro v-for="item in imagenes" :imagen="item"></recuadro>
			</div>
		</section>
	`
});

/**############################################################################################################## */
Vue.component('reg', {
	template: `
	<div>
		reg
	</div>
	`
});

/**############################################################################################################## */
// location
Vue.component('recuadroMap', {
	props: ['item'],
	template: `
		<div class="card m-2">
			<div class="card-header">{{item.titulo}}</div>
			<div class="card-body p-0">
				<iframe :src="item.referencia" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0" frameborder="0"></iframe>
			</div>
		</div>
	`
});

/**############################################################################################################## */
var app = new Vue({
	el: "#app",
	data: {
		view: "home",
		id_producto: 0,
		botones: [{
				referencia: "home",
				etiqueta: "Inicio"
			},
			{
				referencia: "about",
				etiqueta: "Acerca de"
			},
			{
				referencia: "contact",
				etiqueta: "Contacto"
			},
			{
				referencia: "reg",
				etiqueta: "Registrese"
			},
			{
				referencia: "location",
				etiqueta: "Sucursales"
			},
			{
				referencia: "client",
				etiqueta: "Clientes"
			}
		]
	},
	components: {
		home: {
			template: `
				<div> <br>
					<carousel :imagenes="carrusel"></carousel> <br>
					<seccion-vue titulo="Seccion 1" :imagenes="indexSeccion1"></seccion-vue>
					<seccion-vue titulo="Seccion 2" :imagenes="indexSeccion2"></seccion-vue>
				</div>
			`
		},
		about: {
			template: `
				<div>
					<h4-vue titulo="Acerca de nosostros"></h4-vue>
					<img class="d-flex my-1 mx-auto" src="imagenes/fabrica_chocolate.jpg" alt="Sopa Crema de Calabaza" />
					<p class="text-justify">
						En 1996, continuando con la antigua tradición Fermonsel y respetando y revalorando la
						calidad por sobre todas las cosas, inaugura ChocoStack, con un local de elaboración y
						venta en la calle Mitre al 202, una marca que encierra “la historia” de fidelidad y
						amor por el chocolate artesanal y la tradición familiar.

						Todo en ChocoStack está pensado para el deleite, incluida su bella cafetería con
						exquisitas tortas, ricos alfajores y la fuente de chocolate. En el año 2009 ChocoStack
						lanzó su nueva, original y exquisita línea de helados artesanales, demostrando
						nuevamente la dedicación y esmero de la familia Fermonsel. En el año 2010 ChocoStack
						abre las puertas de la Patisserie, un maravilloso lugar con encanto propio. En él se
						pueden degustar esponjosos y llamativos cupcakes, el gingerman cookie y finas masas
						entre muchas delicias.
					</p>
				</div>
			`
		},
		contact: {
			template: `
				<div>
					<h4-vue titulo="Contacto"></h4-vue>
					<p>
						<div class="c-marron-2 fa fa-2x fa-envelope"></div>
						Enviar sujerencias de recetas a mi correo:
						<a href="mailto:ejemplo@gmail.com">
							ejemplo@gmail.com
						</a>
					</p>
				</div>
			`
		},
		location: {
			template: `
				<div>
					<h4-vue titulo="Nuestras Sucursales"></h4-vue>
					<div class="d-flex flex-wrap justify-content-around">
						<recuadroMap v-for="item in listaDeSucursales" :item="item"></recuadroMap>
					</div>
				</div>
			`
		},
		client: {
			template: `
				<div>
					<h4-vue titulo="Clientes varios"></h4-vue>
					<div class="d-flex flex-wrap justify-content-around">
						<recuadro v-for="item in listaDeClientes" :imagen="item"></recuadro>
					</div>
				</div>
			`
		},
		producto: {
			data() {
				return {
					producto: productos[app.id_producto]
				}
			},
			template: `
				<div class="p-2 d-flex flex-column align-items-center justify-items-center"> <br>
					<h4 class="c-marron-2 font-italic font-weight-bold">{{producto.titulo}}</h4>
					<img class="m-2 rounded border shadow-lg bg-white" :src="producto.imagen">
					<p class="font-italic">{{producto.descripcion}}</p>
					<p class="font-italic font-weight-bold c-marron-3">{{producto.precio}}</p>
				</div>
			`
		}
	}
});