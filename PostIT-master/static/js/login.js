var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("toogle-btn");

var submit_btn_register = document.getElementById("submit-btn-register");


function register() {
  x.style.left = "-400px";
  y.style.left = "50px";
  z.style.left = "140px";
  z.style.borderRadius = "0px 30px 30px 0px";
  submit_btn_register.style.marginTop = "30px";
  
}
function login() {
  x.style.left = "50px";
  y.style.left = "450px";
  z.style.left = "0px";
  z.style.borderRadius = "30px 0px 0px 30px";
}
