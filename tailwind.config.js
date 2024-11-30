/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./core/templates/**/*.{html,js,jsx,ts,tsx,scss}",
    "./frontend/**/*.{html,js,jsx,ts,tsx,scss}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "cupcake", "emerald", "autumn", "forest", "retro"],
  },
};
