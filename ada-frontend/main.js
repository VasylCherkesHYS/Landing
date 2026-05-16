import "./assets/css/tailus.css";
import Swiper from "swiper/bundle";
import { Pagination } from "swiper/modules";
import "swiper/css/bundle";
import "swiper/css/pagination";
import "swiper/css/effect-cards";

const mainHeader = document.querySelector("#header");
const menuBtn = document.querySelector("#menu-btn");

if (mainHeader && menuBtn) {
  menuBtn.addEventListener("click", () => {
    mainHeader.dataset.state = mainHeader.dataset.state === "active" ? "" : "active";
  });
}

function openContactModal(subject) {
  const modal = document.getElementById("contactModal");
  if (!modal) return;
  const subjectInput = modal.querySelector("#modal-subject");
  if (subjectInput) subjectInput.value = subject || "general";
  modal.classList.remove("hidden");
  modal.classList.add("flex");
  document.body.style.overflow = "hidden";
  const firstInput = modal.querySelector("input:not([type=hidden]), textarea");
  if (firstInput) firstInput.focus();
}

function closeContactModal() {
  const modal = document.getElementById("contactModal");
  if (!modal) return;
  modal.classList.add("hidden");
  modal.classList.remove("flex");
  document.body.style.overflow = "";
}

window.openContactModal = openContactModal;
window.closeContactModal = closeContactModal;

const contactModal = document.getElementById("contactModal");
if (contactModal) {
  contactModal.addEventListener("click", (event) => {
    if (event.target === contactModal) closeContactModal();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !contactModal.classList.contains("hidden")) {
      closeContactModal();
    }
  });
}

if (document.querySelector(".proofSlides")) {
  new Swiper(".proofSlides", {
    effect: "cube",
    cubeEffect: {
      slideShadows: false,
      shadow: false,
      shadowOffset: 20,
      shadowScale: 0.94,
    },
    loop: true,
    autoplay: { delay: 3000, duration: 500 },
    grabCursor: true,
    modules: [Pagination],
    centeredSlides: true,
    pagination: { el: ".swiper-pagination" },
  });
}
