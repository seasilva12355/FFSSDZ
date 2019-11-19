var x;
x=$("#mostrarocultar"); //recuperamos selector
x.click(MostrarOcultar) //a través del método click invocamos la función.

function MostrarOcultar(){
    var x;
    x=$("#mostrarocultar");
    $("#mostrarocultar").click(Desvanecer());
}

function Desvanecer(){
    $("#mapa").toggle(1500);
}
function ConfirmarLimpiarContacto(){
    var x;
    x=$(document);
    var pregunta = confirm("¿Estás segura/o que deseas borrar todos los campos?")
	if (pregunta){
		document.forms["datosContacto"].reset();
    }
    else{
    }
}
function ConfirmarLimpiarEcoArauco(){
    var x;
    x=$(document);
    var pregunta = confirm("¿Estás segura/o que deseas borrar todos los campos?")
	if (pregunta){
		document.forms["datosEcoArauco"].reset();
    }
    else{
    }
}
function ConfirmarLimpiarCoLife(){
    var x;
    x=$(document);
    var pregunta = confirm("¿Estás segura/o que deseas borrar todos los campos?")
	if (pregunta){
		document.forms["datosCoLife"].reset();
    }
    else{
    }
}
function ConfirmarLimpiarEcoEncalada(){
    var x;
    x=$(document);
    var pregunta = confirm("¿Estás segura/o que deseas borrar todos los campos?")
	if (pregunta){
		document.forms["datosEcoEncalada"].reset();
    }
    else{
    }
}

function Saludar(){
    setTimeout(function(){ alert("Bienvenido a URBAN SA. Puedes obtener información de nuestros edificios más abajo."); }, 3000);
}

function Destacar(){
    $("#enviar").hover(function(){
		$("#enviar").css("background-color", "#FFE000");
		}, function(){
			$("#enviar").css("background-color", "#FFFFFF");
        });
    $("#limpiar").hover(function(){
        $("#limpiar").css("background-color", "#FFE000");
        }, function(){
            $("#limpiar").css("background-color", "#FFFFFF");
        });    
    $("#mostrarocultar").hover(function(){
        $("#mostrarocultar").css("background-color", "#FFE000");
        }, function(){
            $("#mostrarocultar").css("background-color", "#FFFFFF");
        }); 
}

function HoraMensaje(){
    var d = new Date();
    var h = d.getHours();
    if(h<10||h>=19){
        setTimeout(function(){ alert("Lo lamentamos, pero a esta hora ya no estamos trabajando. De todas formas puedes enviarnos un correo más abajo."); }, 3000);
    }
    else{
    }
}
