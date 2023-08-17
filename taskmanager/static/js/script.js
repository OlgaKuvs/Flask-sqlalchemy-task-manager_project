document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
});


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
  });

  // datepicker initialization
  document.addEventListener('DOMContentLoaded', function() {
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });
  });

  // select initialization
  var selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  // collabsible initialization
  var collabsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collabsibles);

 