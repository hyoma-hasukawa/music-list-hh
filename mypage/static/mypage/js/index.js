// document.getElementById("menu_btn").addEventListener("click", function(event){
//     document.getElementById("modal_menu").classList.toggle("hidden")
// });

// document.getElementById("modal_menu").addEventListener("click", function(event){
//     document.getElementById("modal_menu").classList.toggle("hidden")
// });
const MAX_LENGTH = 8;
for(let item of document.getElementsByClassName("limited_string")){
    if (item.textContent.length > MAX_LENGTH) {
        item.textContent = item.textContent.slice(0,MAX_LENGTH - 1) + "…";
    } else {
        item.textContent = item.textContent
    }
}

document.getElementById("initial_select").onclick = function(event){
    event.preventDefault();
    document.getElementById("initial_select_box").classList.toggle("hidden");
}

document.getElementById("counts_select").onclick = function(event){
    event.preventDefault();
    document.getElementById("counts_select_box").classList.toggle("hidden");
}

document.getElementById("genre_btn").addEventListener("click", function(event){
    document.getElementById("modal_menu").classList.toggle("hidden")
});

document.getElementById("modal_menu").addEventListener("click", function(event){
    document.getElementById("modal_menu").classList.toggle("hidden")
});