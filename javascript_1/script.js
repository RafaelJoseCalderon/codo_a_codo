ejercicio_1 = () => alert("Hello Word");

ejercicio_2 = () => printf("Hello World");

ejercicio_3 = () => printf(3 + 5);

function ejercicio_4() {
    let persona = prompt("Ingrese su nombre", "");
    if (persona != null) printf("Hola " + persona);
}

function ejercicio_5() {
    let unNumero = parseInt(prompt("Ingrese un número", ""));
    let otroNumero = parseInt(prompt("Ingrese otro número", ""));

    if (!isNaN(unNumero) && !isNaN(otroNumero)) {
        printf("La suma es " + (unNumero + otroNumero));
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_6() {
    let unNumero = parseInt(prompt("Ingrese un número", ""));
    let otroNumero = parseInt(prompt("Ingrese otro número", ""));

    if (!isNaN(unNumero) && !isNaN(otroNumero)) {
        printf("El maximo es " + Math.max(unNumero, otroNumero));
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_7() {
    let numeros = [];

    for (i = 1; i < 4; i++)
        numeros.push(parseInt(prompt("Ingrese un número (" + i + ")", "")));

    if (!numeros.every(isNaN)) {
        printf("El maximo es " + Math.max(...numeros));
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_8() {
    let numero = parseInt(prompt("Ingrese un numero", ""));

    if (!isNaN(numero)) {
        if (numero % 2 == 0) {
            printf("El número es divisible por 2");
        } else {
            printf("El número no es divisible por 2");
        }
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_9() {
    let cadena = prompt("Escriba una frase", "");

    if (cadena != null) {
        printf("La letra \"a\" aparece " + contar(cadena) + " veces");
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_10() {
    let cadena = prompt("Escriba una frase", "");

    if (cadena != null) {
        let respuesta = "Las vocales que aparecen son: ";
        const vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'];

        cadena = cadena.toLowerCase();
        for (let vocal of vocales)
            if (cadena.includes(vocal)) respuesta += vocal + " ";

        printf(respuesta);
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_11() {
    let cadena = prompt("Escriba una frase", "");

    if (cadena != null) {
        let contador = 0;
        const vocales = [
            'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú',
            'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'
        ];

        for (let caracter of cadena)
            if (vocales.includes(caracter)) contador++;

        printf("Hay " + contador + " vocales");
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_12() {
    let cadena = prompt("Escriba una frase", "");

    cadena = cadena.toLowerCase();
    if (cadena != null) {
        printf(
            "La letra \"a\" aparece " + (contar(cadena, "a") + contar(cadena, "á")) + " veces<br>" +
            "La letra \"e\" aparece " + (contar(cadena, "e") + contar(cadena, "é")) + " veces<br>" +
            "La letra \"i\" aparece " + (contar(cadena, "i") + contar(cadena, "í")) + " veces<br>" +
            "La letra \"o\" aparece " + (contar(cadena, "o") + contar(cadena, "ó")) + " veces<br>" +
            "La letra \"u\" aparece " + (contar(cadena, "u") + contar(cadena, "ú")) + " veces<br>"
        );
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_13() {
    let numero = parseInt(prompt("Ingrese un numero", ""));

    if (!isNaN(numero)) {
        const numeros = [2, 3, 5, 7];

        let i = 0;
        while (numero % numeros[i] != 0 && i < 4) i++;

        if (i != 4) {
            printf("Es divisiblo por 2, 3, 5 o 7");
        } else {
            printf("NO es divisiblo por 2, 3, 5 o 7");
        }
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_14() {
    let numero = parseInt(prompt("Ingrese un numero", ""));

    if (!isNaN(numero)) {
        let respuesta = "";
        const numeros = [2, 3, 5, 7];

        for (let n of numeros)
            if (numero % n == 0) respuesta += n + " ";

        if (respuesta.length != 0) {
            printf("El numero es divisible por " + respuesta);
        } else {
            printf("El numero NO es divisible por 2, 3, 5, 7");
        }
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_15() {
    let numero = parseInt(prompt("Ingrese un numero", ""));

    if (!isNaN(numero)) {
        let respuesta = "Los divisores de " + numero + " son: ";
        const mitad = parseInt(numero / 2);

        for (let i = 1; i < mitad + 1; i++)
            if (numero % i == 0) respuesta += i + " ";

        printf(respuesta);
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_16() {
    let numero_1 = parseInt(prompt("Ingrese un numero", ""));
    let numero_2 = parseInt(prompt("Ingrese un otro numero", ""));

    if (!isNaN(numero_1) && !isNaN(numero_2)) {
        let respuesta = "Los divisores comunes son ";
        const maximo = Math.max(numero_1, numero_2);

        for (let i = 1; i < maximo; i++)
            if (numero_1 % i == 0 && numero_2 % i == 0)
                respuesta += i + " ";

        printf(respuesta);
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_17() {
    let numero = Math.abs(parseInt(prompt("Ingrese un numero", "")));

    if (!isNaN(numero)) {
        let i = 2;
        const mitad = parseInt(numero / 2);

        while (numero % i != 0 && i < mitad) i++;

        if (i == mitad) {
            printf("El numero es primo");
        } else {
            printf("El numero NO es primo");
        }
    } else {
        printf("lo ingresado no es valido");
    }
}

function ejercicio_18() {
    let edad = parseInt(prompt("Ingrese su edad", ""));

    if (!isNaN(edad) && edad > 18) {
        printf("Ud. ya puede conducir");
    } else {
        printf("Ud. NO debe conducir (puede pero, no se lo diga a nadie)");
    }
}

function ejercicio_19() {
    let calificacion = parseFloat(prompt("Ingrese la calificación", ""));

    if (calificacion >= 0 && calificacion < 3) {
        printf("Su calificación es, muy deficiente");
    } else if (calificacion >= 3 && calificacion < 5) {
        printf("Su calificación es, insuficiente");
    } else if (calificacion >= 5 && calificacion < 6) {
        printf("Su calificación es, suficiente");
    } else if (calificacion >= 6 && calificacion < 7) {
        printf("Su calificación es, bien");
    } else if (calificacion >= 7 && calificacion < 9) {
        printf("Su calificación es, notable");
    } else if (calificacion >= 9 && calificacion < 10) {
        printf("Su calificación es, sobresaliente");
    } else {
        printf("valor incorrecto");
    }
}

function ejercicio_20() {
    let resultado = "";
    let lectura = prompt("Ingrese la cadena", "");

    while (lectura != "cancelar") {
        if (lectura != null) resultado += lectura;
        lectura = prompt("Ingrese la cadena", "");
    }

    printf(resultado);
}

function ejercicio_21() {
    let resultado = 0;
    let lectura = null;

    do {
        if (lectura != null) {
            lectura = parseInt(lectura);

            if (!isNaN(lectura)) {
                resultado += lectura;
            }
        }

        lectura = prompt("Ingrese la número", "");
    } while (lectura != "cancelar");

    printf("La sula de los números ingresados es " + resultado);
}

function ejercicio_22() {
    let lectura;
    let letras = [
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
        "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"
    ];

    while (lectura != "cancelar") {
        lectura = parseInt(prompt("Ingrese su DNI"));
        while (!isNaN(lectura) || (lectura < 0 && lectura > 99999999)) {
            alert("No es un numero, intente otra vez")
            lectura = parseInt(prompt("Ingrese su DNI"));
        }

        if (!isNaN(lectura))
            printf("La letra que corresponde es " + letras[lectura % 23]);
    }
}

ejercicio_23 = () => piramide(1, (i) => i < 31, (i) => i + 1);

ejercicio_24 = () => piramide(6, (i) => i > 0, (i) => i - 1);

function ejercicio_25() {
    let numero = parseInt(prompt("Ingrese el alto de la piramide", ""));

    if (!isNaN(numero)) {
        if (numero < 50) {
            piramide(1, (i) => i < numero + 1, (i) => i + 1);
        } else {
            printf("Numero fuera de rango")
        }
    } else {
        printf("NAN");
    }
}

function ejercicio_26() {
    let salida = ""
    for (let i = 1; i < 501; i++) {
        if (i % 4 == 0) {
            salida += i + " (Múltiplo de 4) <br>";
        } else if (i % 9 == 0) {
            salida += i + " (Múltiplo de 9) <br>"
        } else {
            salida += i + "<br>"
        }

        if (i % 5 == 0) {
            salida += "--------------------------- <br>";
        }
    }

    printf(salida);
}

/* #########################################################################################*/
/* funciones auxiliares */
function contar(cadena, letra = "a") {
    var contador = 0;
    for (let caracter of cadena)
        if (caracter == letra) contador++
    return contador;
}

function piramide(inicio, condicion, paso) {
    let salida = ""
    for (i = inicio; condicion(i); i = paso(i)) {
        let cadena = "";
        for (let j = 0; j < i; j++) {
            cadena += i;
        }
        salida += cadena + "<br>";
    }

    printf(salida);
}

function printf(salida, etiqueta = "resultado") {
    document.getElementById(etiqueta).innerHTML = salida;
}

limpiar = () => {
    printf("");
    printf("", "enunciado")
}

/* #########################################################################################*/
/* enunciados */
enunciado_1 = () => printf(
    "Escribe un programa de una sola línea que haga que aparezca en la pantalla un alert que diga \"Hello World\".",
    "enunciado"
);

enunciado_2 = () => printf(
    "Escribe un programa de una sola línea que escriba en la pantalla un texto que diga \"Hello World\" (document.write).",
    "enunciado"
);

enunciado_3 = () => printf(
    "Escribe un programa de una sola línea que escriba en la pantalla el resultado de sumar	3 + 5.",
    "enunciado"
);

enunciado_4 = () => printf(
    "Escribe un programa de dos líneas que pida el nombre del usuario con un prompt y escriba un texto que diga “Hola nombreUsuario”",
    "enunciado"
);

enunciado_5 = () => printf(
    "Escribe un programa de tres líneas que pida un número, pida otro número y escriba el resultado de sumar estos dos números.",
    "enunciado"
);

enunciado_6 = () => printf(
    "Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.",
    "enunciado"
);

enunciado_7 = () => printf(
    "Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.",
    "enunciado"
);

enunciado_8 = () => printf(
    "Escribe un programa que pida un número y diga si es divisible por 2",
    "enunciado"
);

enunciado_9 = () => printf(
    "Escribe un programa que pida una frase y escriba cuantas veces aparece la letra a",
    "enunciado"
);

enunciado_10 = () => printf(
    "Escribe un programa que pida una frase y escriba las vocales que aparecen",
    "enunciado"
);

enunciado_11 = () => printf(
    "Escribe un programa que pida una frase y escriba cuántas de las letras que tiene son vocales",
    "enunciado"
);

enunciado_12 = () => printf(
    "Escribe un programa que pida una frase y escriba cuántas veces aparecen cada una de las vocales",
    "enunciado"
);

enunciado_13 = () => printf(
    "Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)",
    "enunciado"
);

enunciado_14 = () => printf(
    "Añadir al ejercicio anterior que nos diga por cual de los cuatro es divisible (hay que decir todos por los que es divisible)",
    "enunciado"
);

enunciado_15 = () => printf(
    "Escribir un programa que escriba en pantalla los divisores de un número dado",
    "enunciado"
);

enunciado_16 = () => printf(
    "Escribir un programa que escriba en pantalla los divisores comunes de dos números dados",
    "enunciado"
);

enunciado_17 = () => printf(
    "Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)",
    "enunciado"
);

enunciado_18 = () => printf(
    "Pide la edad y si es mayor de 18 años indica que ya puede conducir",
    "enunciado"
);

enunciado_19 = () => printf(
    "Pide una nota (número). Muestra la calificación según la nota: <br>" +
    "# 0-3: Muy deficiente<br>" +
    "# 3-5: Insuficiente<br>" +
    "# 5-6: Suficiente<br>" +
    "# 6-7: Bien<br>" +
    "# 7-9: Notable<br>" +
    "# 9-10: Sobresaliente<br>",
    "enunciado"
);

enunciado_20 = () => printf(
    "Realiza un script que pida cadenas de texto hasta que se pulse “cancelar”. Al salir con" +
    "\"cancelar\" deben mostrarse todas las cadenas concatenadas con un guión",
    "enunciado"
);

enunciado_21 = () => printf(
    "Realiza un script que pida números hasta que se pulse “cancelar”. Si no es un número" +
    "deberá indicarse con un «alert» y seguir pidiendo. Al salir con “cancelar” deberá indicarse la" +
    "suma total de los números introducidos.",
    "enunciado"
);

enunciado_22 = () => printf(
    "Realizar una página con un script que calcule el valor de la letra de un número de DNI" +
    "(Documento nacional de indentidad)." +
    "El algoritmo para calcular la letra del dni es el siguiente :<br>" +
    "# El número debe ser entre 0 y 99999999<br>" +
    "# Debemos calcular el resto de la división entera entre el número y el número 23.<br>" +
    "# Según el resultado, de 0 a 22, le corresponderá una letra de las siguientes: (T, R, W,<br>" +
    "  A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E)<br>" +
    "# Si lo introducido no es un número deberá indicarse con un alert y volver a preguntar.<br>" +
    "# Deberá de repetirse el proceso hasta que el usuario pulse «cancelar».",
    "enunciado"
);

enunciado_23 = () => printf(
    "Realiza un script que escriba una pirámide del 1 al 30 de la siguiente forma :<br>" +
    "1<br>" +
    "22<br>" +
    "333<br>" +
    "4444<br>" +
    "55555<br>" +
    "666666<br>" +
    "........<br>",
    "enunciado"
);

enunciado_24 = () => printf(
    "Haz un script que escriba una pirámide inversa de los números del 1 al número que" +
    "indique el usuario de la siguiente forma : (suponiendo que indica 6)." +
    "666666<br>" +
    "55555<br>" +
    "4444<br>" +
    "333<br>" +
    "22<br>" +
    "1<br>",
    "enunciado"
);

enunciado_25 = () => printf(
    "Crea script para generar pirámide siguiente con los números del 1 al número que indique" +
    "el usuario (no mayor de 50) :",
    "enunciado"
);

enunciado_26 = () => printf(
    "Un script que escriba los números del 1 al 500, que indique cuales son múltiplos de 4 y de" +
    "9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo : <br>" +
    "1<br>" +
    "2<br>" +
    "3<br>" +
    "4 (Múltiplo de 4)<br>" +
    "5<br>" +
    "------------------------<br>" +
    "6<br>" +
    "7<br>" +
    "8 (Múltiplo de 4)<br>" +
    "9 (Múltiplo de 9)<br> " +
    "10<br>",
    "enunciado"
);