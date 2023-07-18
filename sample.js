//Обьявляем переменнные
let intNum = 3;
let floatNum = 5.5;
let bool = true;
let syr = "Основные цвета";

//Массив
let colors = ['Red', 'Green', 'Blue']

//Функции
function sayHello(name) {
    document.write('Вас зовут: ' + name)
}

//Идентификаторы
function changeColor(newColor, clicked_id) {
    let element = document.getElementById("text");
    let rBut = document.getElementById("r");
    let gBut = document.getElementById("g");
    let bBut = document.getElementById("b");

    element.style.color = newColor;

    if(clicked_id == "r") {
        rBut.style.backgroundColor = newColor;
        gBut.style.backgroundColor = '';
        bBut.style.backgroundColor = '';
    }
    else if(clicked_id == "g") {
        rBut.style.backgroundColor = '';
        gBut.style.backgroundColor = newColor;
        bBut.style.backgroundColor = '';
    }
    else {
        rBut.style.backgroundColor = '';
        gBut.style.backgroundColor = '';
        bBut.style.backgroundColor = newColor;
    }
}

let name = prompt("Ваше имя");
sayHello(name);