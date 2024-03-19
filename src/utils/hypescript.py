class Hyperscript:
    def create_element(self, content: str, script: str, element: str = "div") -> str:
        return (
            f'<{element} data-hyperscript="process" _="{script}">{content}</{element}>'
        )
