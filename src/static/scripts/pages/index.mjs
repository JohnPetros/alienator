import { Form } from '../components/form.mjs'
import { Modal } from '../components/modal.mjs'

window.addEventListener('load', () => {
  const modal = new Modal('modal')

  const gameForm = new Form('[data-form="game-form"]')
  const modalGameForm = new Form('#modal [data-form="game-form"]')

  gameForm.onSubmit = () => modal.close()
  modalGameForm.onSubmit = () => modal.close()
})
