//API = Application Programming Interfaces
//Asynchronus Javascript and XML

// PROMESAS
function muestra_perrito() {
    fetch("https://dog.ceo/api/breeds/image/random")
        .then(response => response.json())
        .then(data => {
            /*
            data = {
                message:"https://images.dog.ceo/x"
                status: "success"
            } 
             */
            let img_perrito = `<img alt="perrito" src="${data.message}">`;
            document.querySelector(".imagen-perrito").innerHTML = img_perrito;
        })
}

// ASYNC/AWAIT

async function muestra_perritoAsync() {
    let response = await fetch("https://dog.ceo/api/breeds/image/random");
    let data = await response.json();
                /*
            data = {
                message:"https://images.dog.ceo/x"
                status: "success"
            } 
             */
    let img_perrito = `<img alt="perrito" src="${data.message}">`;
    document.querySelector(".imagen-perrito").innerHTML = img_perrito;
}