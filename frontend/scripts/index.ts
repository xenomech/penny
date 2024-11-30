import idSelector from "./helpers/idSelector";
import typewriter from "./animations/typewriter";
import "../styles/globals.scss";

window.addEventListener("load", () => {
  const helloElement = idSelector("typewriter");
  if (helloElement) {
    const text = helloElement.textContent;
    helloElement.style.display = "block";
    helloElement.innerHTML = "";
    typewriter(helloElement, text, 10);
  }
});
