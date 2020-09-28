function menuDesplegable() {
	var x = document.getElementById("navBar");
	if (x.className === "") {
		x.className = "visible-invisible";
	} else {
		x.className = "";
	}
}