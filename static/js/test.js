/*function changeGreenMode() {
      document.documentElement.setAttribute('theme', 'green');
    }
function changeBrownMode() {
      document.documentElement.setAttribute('theme', 'brown');
    }
function changeDarkMode(){
      document.documentElement.setAttribute('theme', 'dark');
    }
function changePinkMode() {
      document.documentElement.setAttribute('theme', 'pink');
    }
*/
//let col = String(document.getElementById('testtest').value);

window.onload = function changeThemeColor() {
let col = String(document.getElementById('testtest').textContent);

/*
let col = "BROWN";
alert("これは特に意味のないポップアップです");
*/

if(col === "BROWN"){
    document.documentElement.setAttribute('theme', 'brown');
}
else if(col === "BLACK"){
    document.documentElement.setAttribute('theme', 'dark');
}
else if(col === "PINK"){
    document.documentElement.setAttribute('theme', 'pink');
}
else {
    document.documentElement.setAttribute('theme', 'green');
   }

}