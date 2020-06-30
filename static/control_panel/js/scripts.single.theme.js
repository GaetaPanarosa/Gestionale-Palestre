/* Dore Single Theme Initializer Script 

Table of Contents

01. Single Theme Initializer
*/

/* 01. Single Theme Initializer */

(function ($) {
  if ($().dropzone) {
    Dropzone.autoDiscover = false;
  }

  var direction = "ltr";
  var radius = "flat";

  if (typeof Storage !== "undefined") {
    if (localStorage.getItem("dore-direction")) {
      direction = localStorage.getItem("dore-direction");
    } else {
      localStorage.setItem("dore-direction", direction);
    }
    if (localStorage.getItem("dore-radius")) {
      radius = localStorage.getItem("dore-radius");
    } else {
      localStorage.setItem("dore-radius", radius);
    }
  }

  $("body").addClass(direction).addClass('flat').dore();
  $("html").attr("dir", direction);
})(jQuery);
