const inputElem = document.getElementById('example'); // input要素
const currentValueElem = document.getElementById('current-value'); // 埋め込む先のspan要素
let elements = document.getElementsByName('flexRadioDefault');
let len = elements.length;
let checkValue = '';
let slider = null;
let sliderValue = null;

// スライダー値を取得して表示
const setValue = ()=> {
    const value = slider.value;
    sliderValue.textContent = value;
}

// 起動時の処理
window.addEventListener("load", ()=>{
    // スライダー、スライダー値DOM
    slider = document.getElementById("slider");
    sliderValue = document.getElementById("sliderValue");
    // スライドさせたときの処理
    slider.addEventListener("input", setValue);
    // スライダー初期値を表示
    setValue();
});

// 有効・無効
function clickbtn() {
    let str = "";
    const f1 = document.getElementById("pop");		
    const popper = f1.popper;

    for (let i = 0; i < popper.length; i++) {
        if (popper[i].checked) {//(popper[i].checked === true)と同じ
            str = popper[i].value;
            break;
        }
    }
    document.getElementById("span2").textContent = str;
}

function addPlaylist(id,name,artists){
    const li = `<li class="user-music list-group-item bg-secondary text-white">
                    <div class="user-music-update d-flex justify-content-between">
                        <div class="d-flex flex-column">
                            <div class="text-truncate">Title : ${name}</div>
                            <div class="text-truncate">Artists : ${artists}</div>
                            <input type="hidden" name="music_id[]" value="${id}">
                        </div>
                        <button class="btn btn-secondary btn-sm mt-2 ms-1 close-icon" value="削除" onClick="getElement(event);">×</button>
                    </div>
                </li>`
        
    document.getElementById("myplaylist").insertAdjacentHTML('beforeend',li);
}

// buttonの箇所(event)の箇所を消すようにする。(JavaScriptでリストの上を削除してしまう→このときにclassnameが一緒のため、上から消してしまう。)
function getElement(e){
    // console.log(e.target.closest("li"));
    e.target.closest("li").remove();
    // let dtn = document.getElementById('add');
    // dtn.remove();
}

// function getElement(){
//     let dtn = document.getElementById('add');
//     dtn.remove();
// }

// function addPlaylist(id,name,artists){
//     const li = `<li class="user-music list-group-item bg-secondary text-white">
//                     <div class="user-music-update text-truncate">
//                             <p>${name}</p>
//                             <p>${artists}</p>
//                             <input type="hidden" name="music_id[]" value="${id}">
//                     </div>
//                 </li>`
//     document.getElementById("myplaylist").insertAdjacentHTML('beforeend',li);
// }
// 違うパターン
// document.getElementById("ranking").addEventListener("click", function(e){
//     if(!e.target.classList.contains("add_playlist")) {
//         return;
//     }
//     const [id, song, artist] = e.target.dataset.spItem.split(",");
//     console.log(id, song, artist)
//     let li = document.createElement("li");
//     li.classList.add("user-music", "list-group-item", "bg-secondary", "text-white");
//     // li.className = "user-music list-group-item bg-secondary text-white";
//     let div = document.createElement("div");
//     div.classList.add("user-music-update", "text-truncate");

//     let pName = document.createElement("p");
//     pName.textContent = song;

//     let pArtist = document.createElement("p");
//     pArtist.textContent = artist;

//     let input = document.createElement("input");
//     input.type = "hidden";
//     input.name = "music_id[]";
//     input.value = id;

//     let deleteButton = document.createElement("button");
//     deleteButton.textContent = "削除";
//     deleteButton.classList.add("btn", "btn-outline-secondary");
//     deleteButton.addEventListener("click", function(e){
//         li.remove();
//     })
//     div.appendChild(pName);
//     div.appendChild(pArtist);
//     div.appendChild(input);
//     div.appendChild(deleteButton);
//     li.appendChild(div);
//     document.getElementById("myplaylist").appendChild(li);
// })
// for (let j = 0; j < closeIcons.length; j++) {
//     closeIcons[j].addEventListener('click', () => {
//         items[j].remove();
//     });
// }

//   // ボタンをクリックしたときの処理
// btn.addEventListener('click', () => {
//     form.appendChild(createNewForm());
// });

// document.querySelector('#deleteBtn1').addEventListener('click', () => {
//     const element = document.getElementById('add');
//     element.remove();
// });
// }


// function clickBtn1(){
//     var lia = document.getElementById("user-music-update");
//     lia.remove();
// }
// 画像クリック
// const thub = document.getElementById("thumb_album").value;
// divElement.ondblclick = function() {
    
// }
// 画像クリック
// var imgElement = document.getElementById("thumb_album").value;
// imgElement.ondblclick = function() {
// 	// 処理内容
// }

// let popular = document.getElementById('pop');
// popular.elements[1].checked = true;
// popular.addEventListener('change', valueChange);

// const btn = document.getElementById('btn');

// btn.addEventListener('click', () => {
//     const form = document.forms.radio1;

//     result.textContent = '年齢は' + form.age.value + 'です。';
// })

// 現在の値をspanに埋め込む関数
// const setCurrentValue = (val) => {
//     currentValueElem.innerText = val;
// }

// inputイベント時に値をセットする関数
// const rangeOnChange = (e) =>{
//     setCurrentValue(e.target.value);
// }

// window.onload = () => {
//   inputElem.addEventListener('input', rangeOnChange); // スライダー変化時にイベントを発火
//   setCurrentValue(inputElem.value); // ページ読み込み時に値をセット
// }
// スライダー値を取得する

// 有効・無効
// for (let i = 0; i < len; i++){
//     if (elements.item(i).checked){
//         checkValue = elements.item(i).value;
//     }
// }
// function valueChange(event){
//     let checkValue = pop.elements['flexRadioDefault'].value;
//     console.log('選択されているのは ' + checkValue + ' です');
// }

