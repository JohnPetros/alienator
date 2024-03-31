import { Hyperscript } from '../components/hyperscript.mjs'

window.addEventListener('load', () => {
  const hyperscript = new Hyperscript()

  document.body.addEventListener('htmx:afterOnLoad', (event) => {
    hyperscript.precessElement(event.detail.elt)
  })
})
