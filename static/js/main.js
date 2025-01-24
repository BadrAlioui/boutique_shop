// tooltip
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

// to refresh the paeg
document.addEventListener("DOMContentLoaded", function () {
  const alertContainer = document.querySelector(".container.mt-3.text-white");
  if (alertContainer) {      
      setTimeout(function () {
          location.reload();
      }, 4000); 
  }
});