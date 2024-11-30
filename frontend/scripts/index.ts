import idSelector from "./helpers/idSelector";
import typewriter from "./animations/typewriter";
import "../scss/globals.scss";

window.addEventListener("load", () => {
  const helloElement = idSelector("typewriter");
  if (helloElement) {
    const text = helloElement.textContent;
    helloElement.style.display = "block";
    helloElement.innerHTML = "";
    typewriter(helloElement, text, 10);
  }

  const switchThemeElement = idSelector("switch-theme");
  if (switchThemeElement) {
    switchThemeElement.addEventListener("click", () => {
      document.documentElement.classList.toggle("dark");
    });
  }
});
