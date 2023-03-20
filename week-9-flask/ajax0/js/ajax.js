/* The following script code is a jQuery function that waits for the HTML document to be fully loaded before running */

$(document).ready(function () {
  /* The following code is executed when the button is clicked.
      It uses the jQuery selector "$("h3")" to select the <h2> element on the page, 
      and then calls the "text()" method to change its text to "Hello World!". */

  $("button").click(function () {
    $("h3").text("Hello World!");
  });
});
