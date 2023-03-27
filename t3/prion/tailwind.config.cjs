/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    fontFamily: {
      // Note: This is @notapatch and not the docs
      //       I think what it is trying to say is that if you define
      //       a custom font here you are also removing the default
      //       font families sans, serif and mono.
      //
      'sans': ['ui-sans-serif', 'system-ui', ],
      'serif': ['ui-serif', 'Georgia',],
      'display': ['var(--font-poppins)',],
    }
  },
  plugins: [],
};
