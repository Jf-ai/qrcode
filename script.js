const tiltCards = document.querySelectorAll(".tilt-card");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!reduceMotion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
  tiltCards.forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const bounds = card.getBoundingClientRect();
      const x = (event.clientX - bounds.left) / bounds.width;
      const y = (event.clientY - bounds.top) / bounds.height;
      const rotateY = (x - 0.5) * 10;
      const rotateX = (0.5 - y) * 10;

      card.style.transform = `perspective(850px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-3px)`;
    });

    card.addEventListener("pointerleave", () => {
      card.style.transform = "";
    });
  });
}
