class elpyza_script():
    def __init__(self, user_prompt, description):
        self.active = True
        self.user_prompt = user_prompt
        self.description = description

    def parse_input():
        pass

    def get_script_response():
        pass


class doctor(elpyza_script):
    def __init__(self):
        description = """This is an attempt at reproducing DOCTOR. 
The original was created by Joseph Weizenbaum and was supposed to simulate a Rogerian psychotherapist."""
        super().__init__(user_prompt="DOCTOR>", description=description)


scripts = {'doctor': doctor()}


def load_script(script_name) -> elpyza_script:
    return scripts[script_name]


def list_scripts() -> list:
    return list(scripts.keys())
