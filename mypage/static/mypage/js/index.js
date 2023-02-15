const inputElem = document.getElementById('example'); // input要素
const currentValueElem = document.getElementById('current-value'); // 埋め込む先のspan要素

// 現在の値をspanに埋め込む関数
const setCurrentValue = (val) => {
    currentValueElem.innerText = val;
}

// inputイベント時に値をセットする関数
const rangeOnChange = (e) =>{
    setCurrentValue(e.target.value);
}

window.onload = () => {
  inputElem.addEventListener('input', rangeOnChange); // スライダー変化時にイベントを発火
  setCurrentValue(inputElem.value); // ページ読み込み時に値をセット
}
// スライダー値を取得する

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
