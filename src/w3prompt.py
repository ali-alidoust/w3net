from IPython.terminal.prompts import Prompts, Token

class W3Prompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [(Token.Prompt, '>>>> ')]
    def out_prompt_tokens(self):
        return [(Token, " result: ")]