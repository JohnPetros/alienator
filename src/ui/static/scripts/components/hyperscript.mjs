export class Hyperscript {
  precessElement(element) {
    const elementsToBeProcessed = element.querySelectorAll('[data-hyperscript="process"]')

    for (const element of elementsToBeProcessed) {
      _hyperscript.processNode(element)
    }
  }
}