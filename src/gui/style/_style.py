from .Option_block import Option_Style


class STYLE(Option_Style):
    def __init__(self):
        super().__init__()

    # Add All Style Variable/Attribute to Option Buttons
    def OptionButtonAddStyle(self, Button) -> None:
        Button.config(
            width=self.Option_Button["width"],
            bg=self.Option_Button["bg_color"],
            fg=self.Option_Button["font_color"],
            relief=self.Option_Button["relief"],
            activebackground=self.Option_Button["Active_bg_color"],
            activeforeground=self.Option_Button["Active_fg_color"],
            font="bold"
        )

        # Mouse In
        Button.bind(
            "<Enter>", lambda e: self.Option_Button_on_collision_in(Button))

        # Mouse Out
        Button.bind(
            "<Leave>", lambda e: self.Option_Button_on_collision_out(Button))

    # Add All Style Variable/Attribute to Option Frame/LabelFrame
    def OptionFrameAddStyle(self, Frame) -> None:
        Frame.config(
            bg=self.Option_Frame["bg_color"],
            relief=self.Option_Frame["relief"],
        )

    # Change bg on Mouse over Button
    # Bind Function  on : "<Enter>"
    def Option_Button_on_collision_in(self, Button):
        Button.config(
            bg=self.Option_Button["on_collision"]
        )

    # Change bg on Mouse leave Button
    # Bind Function on : "<Leave>"
    def Option_Button_on_collision_out(self, Button):
        Button.config(
            bg=self.Option_Button["bg_color"]
        )
