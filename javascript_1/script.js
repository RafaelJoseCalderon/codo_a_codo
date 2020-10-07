
// Ejercicio 1
/* Escribe un programa de una sola línea que haga que aparezca en la
   pantalla un alert que diga "Hello World". */
function ejercicio_1() {
	alert("Hello Word");
}

// Ejercicio 2
/* Escribe un programa de una sola línea que escriba en la pantalla
   un texto que diga "Hello World" (document.write). */
function ejercicio_2() {
	document.getElementById("ej2").innerHTML = "Hello World"
}

// Ejercicio 3
/* Escribe un programa de una sola línea que escriba en la pantalla
   el resultado de sumar 3 + 5.*/
function ejercicio_3() {
	let x = 3, y = 5;
	console.log(x + y)
}

// Ejercicio 4
/* Escribe un programa de dos líneas que pida el nombre del usuario
   con un prompt y escriba un texto que diga “Hola nombreUsuario”*/
function ejercicio_4() {
	let persona = prompt("Ingrese su nombre", "");

	if (persona != null) {
		document.getElementById("ej4").innerHTML = "Hola " + persona;
	}
}

// Ejercicio 5
/* Escribe un programa de tres líneas que pida un número, pida otro
   número y escriba el resultado de sumar estos dos números.*/
function ejercicio_5() {
	let unNumero = parseInt(prompt("Ingrese un número", ""));
	let otroNumero = parseInt(prompt("Ingrese otro número", ""));

	if (!isNaN(unNumero) && !isNaN(otroNumero)) {
		document.getElementById("ej5").innerHTML = "La suma es " + (unNumero + otroNumero);
	} else {
		document.getElementById("ej5").innerHTML = "lo ingresado no es valido";
	}
}

// Ejercicio 6
/* Escribe un programa que pida dos números y escriba en la pantalla
   cual es el mayor. */
function ejercicio_6() {
	let unNumero = parseInt(prompt("Ingrese un número", ""));
	let otroNumero = parseInt(prompt("Ingrese otro número", ""));

	if (!isNaN(unNumero) && !isNaN(otroNumero)) {
		document.getElementById("ej6").innerHTML = "El maximo es " + Math.max(unNumero, otroNumero);
	} else {
		document.getElementById("ej6").innerHTML = "lo ingresado no es valido";
	}
}

// Ejercicio 7
/* Escribe un programa que pida 3 números y escriba en la pantalla
   el mayor de los tres. */
function ejercicio_7() {
	let numeros = [];

	for (i = 1; i < 4; i++)
		numeros.push(parseInt(prompt("Ingrese un número (" + i + ")", "")));

	if (!numeros.every(isNaN)) {
		document.getElementById("ej7").innerHTML = "El maximo es " + Math.max(...numeros);
	} else {
		document.getElementById("ej7").innerHTML = "lo ingresado no es valido";
	}
}


// Ejercicio 8
/* Escribe un programa que pida un número y diga si es divisible
   por 2*/
function ejercicio_8() {
	let numero = parseInt(prompt("Ingrese un numero", ""));
	let id = "ej8";

	if (!isNaN(numero)) {
		if (numero % 2 == 0) {
			document.getElementById(id).innerHTML = "El número es divisible por 2";
		} else {
			document.getElementById(id).innerHTML = "El número no es divisible por 2";
		}
	} else {
		document.getElementById(id).innerHTML = "lo ingresado no es valido";
	}
}

// Ejercicio 9
/* Escribe un programa que pida una frase y escriba cuantas veces
   aparece la letra a */
function ejercicio_9() {
	let cadena = prompt("Ingrese un numero", "");
	let id = "ej9";

	if (cadena != null) {
		document.getElementById(id).innerHTML = "La letra \"a\" aparece " + contar(cadena) + " veces";
	} else {
		document.getElementById(id).innerHTML = "lo ingresado no es valido";
	}

}

// Ejercicio 9
/* Escribe un programa que pida una frase y escriba las vocales que
   aparecen*/
function ejercicio_10() {
	let cadena = prompt("Ingrese un numero", "");
	let id = "ej10";

	if (cadena != null) {
		document.getElementById(id).innerHTML =
			"<p>La letra \"a\" aparece " + contar(cadena, "a") + " veces</p>" +
			"<p>La letra \"e\" aparece " + contar(cadena, "e") + " veces</p>" +
			"<p>La letra \"i\" aparece " + contar(cadena, "i") + " veces</p>" +
			"<p>La letra \"o\" aparece " + contar(cadena, "o") + " veces</p>" +
			"<p>La letra \"u\" aparece " + contar(cadena, "u") + " veces</p>";
	} else {
		document.getElementById(id).innerHTML = "lo ingresado no es valido";
	}
}

/* funcion auxiliar */
function contar(cadena, letra = "a") {
	var contador = 0;
	for (let caracter of cadena) if (caracter == letra) contador++
	return contador;
}