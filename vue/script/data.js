/**############################################################################################################## */
/* Aqui ponder la conexion rest                                                                                   */
/**############################################################################################################## */

const carrusel = [
	"imagenes/keyframe/images_01.jpg",
	"imagenes/keyframe/images_02.jpg",
	"imagenes/keyframe/images_03.jpg",
	"imagenes/keyframe/images_04.jpg",
	"imagenes/keyframe/images_05.jpg"
];

const indexSeccion1 = [{
		id: 0,
		href: "producto",
		src: "imagenes/productos/caprichos.jpg",
		h4: "caprichos"
	},
	{
		id: 1,
		href: "producto",
		src: "imagenes/productos/lujuria-tropical.jpg",
		h4: "lujuria-tropical"
	},
	{
		id: 2,
		href: "producto",
		src: "imagenes/productos/patagonia.jpg",
		h4: "patagonia"
	}
];

const indexSeccion2 = [{
		id: 3,
		href: "producto",
		src: "imagenes/productos/trinidad-almendra.jpg",
		h4: "trinidad-almendras"
	},
	{
		id: 4,
		href: "producto",
		src: "imagenes/productos/trufas-golosa.jpg",
		h4: "trufas-golosas"
	},
	{
		id: 5,
		href: "producto",
		src: "imagenes/productos/volcan-de-chocolate.jpeg",
		h4: "volcan-chocolate"
	}
];

const listaDeSucursales = [{
		titulo: "Jorge Luis Hirschi",
		referencia: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3271.7851338604373!2d-57.941160585278055!3d-34.91184128038078!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a2e61621b73869%3A0x32c529fe42daaa5d!2sEstadio%20Jorge%20Luis%20Hirschi!5e0!3m2!1ses-419!2sar!4v1600817929348!5m2!1ses-419!2sar"
	},
	{
		titulo: "Marcelo Bielsa",
		referencia: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3347.810944161456!2d-60.663745985341365!3d-32.956000480918384!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95b7ab6f11537faf%3A0xa99bea6006b75b6a!2sEstadio%20Coloso%20Del%20Parque%20Marcelo%20Bielsa!5e0!3m2!1ses-419!2sar!4v1600817983797!5m2!1ses-419!2sar"
	},
	{
		titulo: "Monumental José Fierro",
		referencia: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3560.8532455828017!2d-65.20127438551866!3d-26.812801083170754!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94225c2456e5dad1%3A0xfb536657696dc88d!2sEstadio%20Monumental%20Jos%C3%A9%20Fierro!5e0!3m2!1ses-419!2sar!4v1600818035706!5m2!1ses-419!2sar"
	},
	{
		titulo: "Juan Carmelo Zerillo",
		referencia: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3271.8173909139928!2d-57.934655285278104!3d-34.911031880381024!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a2e61126c74ea3%3A0x7178349c562567f0!2sEstadio%20Juan%20Carmelo%20Zerillo!5e0!3m2!1ses-419!2sar!4v1600818072893!5m2!1ses-419!2sar"
	}
];

const listaDeClientes = [{
		id: 0,
		href: "client",
		src: "imagenes/clientes/images_01.jpeg",
		h4: " "
	},
	{
		id: 1,
		href: "client",
		src: "imagenes/clientes/images_02.jpeg",
		h4: ""
	},
	{
		id: 2,
		href: "client",
		src: "imagenes/clientes/images_03.jpeg",
		h4: ""
	},
	{
		id: 3,
		href: "client",
		src: "imagenes/clientes/images_04.jpeg",
		h4: ""
	},
	{
		id: 4,
		href: "client",
		src: "imagenes/clientes/images_05.jpeg",
		h4: ""
	},
	{
		id: 5,
		href: "client",
		src: "imagenes/clientes/images_06.jpeg",
		h4: ""
	},
	{
		id: 6,
		href: "client",
		src: "imagenes/clientes/images_07.jpeg",
		h4: ""
	},
	{
		id: 7,
		href: "client",
		src: "imagenes/clientes/images_08.jpeg",
		h4: ""
	}
]

const productos = [{
		titulo: "Capricho",
		imagen: "imagenes/productos/caprichos.jpg",
		descripcion: `
		Ganache con deliciosas pasas maceradas al rhum bañada en chocolate amargo
		y decorada con chocolate blanco.
	`,
		precio: "$ 2500 .- por Caja (20 Unidades)",
	},
	{
		titulo: "Lujuria Tropical",
		imagen: "imagenes/productos/lujuria-tropical.jpg",
		descripcion: `
		Con el aroma tropical del Maracuyá y el acorde del dulce de leche en un baño
		de irrestistible chocolate amargo o blanco.
	`,
		precio: "$ 1500 .- por Caja (10 Unidades)",
	},
	{
		titulo: "Patagonia",
		imagen: "imagenes/productos/patagonia.jpg",
		descripcion: `
		Armónica fusión de crema de frambuesas, frutillas, grosellas y cassis de la
		patagonia, con delicado baño de chocolate amargo.
	`,
		precio: "$ 1000 .- por Bolsa (8 Unidades)",
	},
	{
		titulo: "Trinidad de Almendras",
		imagen: "imagenes/productos/trinidad-almendra.jpg",
		descripcion: `
		Untuosa crema de almendras sobre crocante amaretti, bañada en chocolate leche
		y condecorada con una almendra tostada.
	`,
		precio: "$ 1000 .- por Caja (1 Unidad)",
	},
	{
		titulo: "Trufas Golosas",
		imagen: "imagenes/productos/trufas-golosa.jpg",
		descripcion: `
		En su interior, cuerpo de mousse de chocolate, corazón de dulce de leche, cabeza
		de nuez bañada en chocolate amargo
	`,
		precio: "$ 1500 .- por Caja (5 Unidades)",
	},
	{
		titulo: "Volcan de Chocolate",
		imagen: "imagenes/productos/volcan-de-chocolate.jpeg",
		descripcion: `
		Coulant, fondant o volcán es un conocido postre de chocolate patentado por el
		chef Francés Michel Bras en 1981 en su restaurante de Laguiole, en la meseta de
		l'Aubrac, al suroeste de Francia.
	`,
		precio: "$ 1500 .- por Caja (5 Unidades)",
	}
];