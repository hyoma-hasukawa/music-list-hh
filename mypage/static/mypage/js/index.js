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

