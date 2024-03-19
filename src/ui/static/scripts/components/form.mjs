export class Form {
  #form
  trigger

  constructor(selector) {
    this.#form = document.querySelector(selector)

    this.#form.addEventListener('submit', (event) => this.#handleSubmit(event))

    this.trigger = this.#form.querySelector('[data-form="trigger"]')

    console.dir(this.trigger)
  }

  onSubmit() { }

  #handleSubmit(event) {
    event.preventDefault()
    this.onSubmit()
  }
}