var now = new Date();
var datestring = String(now.getTimezoneOffset());
document.getElementById("time").innerHTML = datestring;