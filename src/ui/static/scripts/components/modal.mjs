export class Modal {
  #modal

  constructor(id) {
    this.#modal = FlowbiteInstances.getInstance('Modal', id)
  }

  open() {
    this.#modal.show()
  }

  close() {
    this.#modal.hide()
  }
}
