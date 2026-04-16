let currentDate = new Date().toLocaleDateString();
let date = document.querySelector("#date");

date.textContent = currentDate;

let currentYear = new Date().getFullYear();
let yearElement = document.getElementById("year");

yearElement.textContent = currentYear;
