ejercicio_1 = (N) => console.log("Bienvenidos al curso Full Stack\n".repeat(N));

function ejercicio_2(numero_1, numero_2) {
	let resultado;
	if (numero_1 > numero_2) {
		resultado = numero_1;
	} else if (numero_1 < numero_2) {
		resultado = numero_2;
	} else {
		resultado = "son los dos iguales (" + numero_1 + ")";
	}

	return resultado;
}

function promedio(numero_1, numero_2, numero_3) {
	return (numero_1 + numero_2 + numero_3) / 3;
}

function ejercicio_4() {
	let cantidadDeNotas = 0;
	let notas = 0;

	let nota = Number(prompt("Ingrese una nota", ""));
	while (nota != -1) {
		cantidadDeNotas++;
		notas += nota;

		nota = Number(prompt("Ingrese una nota", ""));
	}

	return notas / cantidadDeNotas;
}

siguiente = (numero) => numero + 1;

doble = (numero) => numero * 2;

cuadrado = (numero) => numero ** 2;

function imprimirValores(numero) {
	console.log(siguiente(numero));
	console.log(doble(numero));
	console.log(cuadrado(numero));
}

function imprimirElDobleDelSiguiente(numero) {
	console.log(doble(siguiente(numero)));
}

function imprimirElDobleDelSiguienteAlCuadrado(numero) {
	console.log(cuadrado(doble(siguiente(numero))));
}

function perimetroCuadrado(longitudLado) {
	return 4 * longitudLado;
}

function superficieCuadrado(longitudLado) {
	return longitudLado ** 2;
}

function perimetroCirculo(radio) {
	return 2 * Math.PI * radio;
}

function superficieCirculo(radio) {
	return Math.PI * radio ** 2;
}

// Funciones Fecha:
function diasDeUnMes(mes) {
	let inicial = new Date(1970, mes - 1, 1).getTime();
	let final = new Date(1970, mes, 1).getTime();
	let msPerDay = 24 * 60 * 60 * 1000;

	return Math.round((final - inicial) / msPerDay);
}

function esBisiesto(anio) {
	return anio % 4 == 0 && (anio % 100 != 0 || anio % 400 == 0);
}

function diasDeUnMesYMD(anio, mes, dia) {
	let inicial = new Date(anio, mes - 1, 1).getTime();
	let final = new Date(anio, mes, dia).getTime();
	let msPerDay = 24 * 60 * 60 * 1000;

	return Math.round((final - inicial) / msPerDay);
}

function diaSiguiente(dia, mes, anio) {
	let fecha = new Date(anio, mes, dia);
	return "???"
}

function diaAnterior(dia, mes, anio) {
	return "???"
}

function ultimoDiaDelMes(dia, mes, anio) {
	return "???"
}