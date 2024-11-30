const typewriter = (element: HTMLElement, text: string, delay: number) => {
  let i = 0;
  const type = () => {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, delay);
    }
  };
  type();
};

export default typewriter;
