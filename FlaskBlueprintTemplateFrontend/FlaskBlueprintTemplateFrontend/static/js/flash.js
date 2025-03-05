document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        document.querySelectorAll(".flash").forEach(flash => {
            flash.classList.add("hide");
            setTimeout(() => flash.remove(), 500);
        });
    }, 3000);
});
