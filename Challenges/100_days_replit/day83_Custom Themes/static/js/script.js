var date = new Date();
var year = date.getFullYear();
var month = date.getMonth() + 1;
var day = date.getDate();

// Update the content of the element with id "current_date"
document.getElementById("current_date").innerHTML =
  month + "/" + day + "/" + year;
