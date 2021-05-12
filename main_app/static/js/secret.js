document.addEventListener("keydown", function (event) {
  code = "1";
  if (event.key === code) {
    document.body.style = "background-color: pink";
  }
});

$(document).ready(function () {
  $(".modal").modal();
  $(".dropdown-trigger").dropdown({ hover: false });
});

console.log("Hello World");
