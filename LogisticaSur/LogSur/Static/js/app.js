const tel = document.getElementById("tel");
const calle = document.getElementById("calle");
const altura = document.getElementById("altura");
const cp = document.getElementById("cp");
const editbtn = document.getElementById("editbtn");
const savebtn = document.getElementById("savebtn");

editbtn.addEventListener("click", function(){
    tel.contentEditable = true;
    tel.style.background = "yellow";
    calle.contentEditable = true;
    calle.style.background = "yellow";
    altura.contentEditable = true;
    altura.style.background = "yellow";
    cp.contentEditable = true;
    cp.style.background = "yellow";
});

savebtn.addEventListener("click", function(){
    tel.contentEditable = false;
    tel.style.background = "white";
    calle.contentEditable = false;
    calle.style.background = "white";
    altura.contentEditable = false;
    altura.style.background = "white";
    cp.contentEditable = false;
    cp.style.background = "white";
});

/*
tbody.addEventListener("click", (event) => {
    if (event.target.tagName === "BUTTON")
    {
        const button = event.target;

        if (button.textContent === "Editar")
        {   
            document.getElementsByTagName("tr")[1].style.backgroundColor = "yellow";
        }

        else if (button.textContent === "Guardar")
        {
            alert("Este es el boton para guardar sus datos!");
        }
    }
});
*/