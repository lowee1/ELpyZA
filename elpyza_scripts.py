class elpyza_script:
    def __init__(self, user_prompt, description, initial, script_prefix):
        self.active = True
        self.user_prompt = user_prompt
        self.description = description
        self.initial = initial
        self.script_prefix = script_prefix

    def get_script_response(self, user_input: str) -> str:
        raise NotImplementedError(
            "get_script_response has not been implemented by child class yet"
        )


class doctor(elpyza_script):
    def __init__(self):
        description = """\
This is an attempt at reproducing DOCTOR.\
 The original was created by Joseph Weizenbaum and was supposed to simulate a\
 Rogerian psychotherapist.\
"""
        initial = "Is something troubling you?"
        super().__init__(
            user_prompt="YOU: ",
            description=description,
            initial=initial,
            script_prefix="DOCTOR: ",
        )


class echo(elpyza_script):
    def __init__(self):
        description = (
            """This is a test script which just repeats the users last input"""
        )
        super().__init__(
            user_prompt="YOU: ",
            description=description,
            initial="echo test script",
            script_prefix="ECHO: ",
        )
        self.previous_input = ""

    def get_script_response(self, user_input: str) -> str:
        if user_input in ["quit", "exit", "stop", "go away"]:
            self.active = False
            return "ok bye"
        response = self.previous_input
        self.previous_input = user_input
        return response


scripts = {"doctor": doctor, "echo": echo}


def load_script(script_name) -> elpyza_script:
    selected = scripts[script_name]
    return selected()


def list_scripts() -> list:
    return list(scripts.keys())
