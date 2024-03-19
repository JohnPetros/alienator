module.exports = {
  content: [
    './src/templates/**/*.html',
    './src/static/src/**/*.js',
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {
      backgroundSize: {
        'mobile-size': '40rem 100%',
      },
    }
  },
  plugins: [
    require('flowbite/plugin'),
    require('tailwindcss-animated'),
  ],
}