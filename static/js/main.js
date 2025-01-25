// tooltip
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

document.addEventListener("DOMContentLoaded", function () {
  const closeButtons = document.querySelectorAll(".alert .btn-close");
  
  closeButtons.forEach(button => {
    button.addEventListener("click", function () {
      // Rafraîchir la page après un court délai
      setTimeout(() => {
        location.reload();
      }, 500); // 500ms pour laisser le temps au message de disparaître
    });
  });
});
