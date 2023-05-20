#!/usr/bin/env python3
"""
    App GUI module
"""
import threading
import time
import tkinter as tk

import lettercaser.utils as utils


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.status = True
        self.xposition = None
        self.yposition = None
        self.master.resizable(False, False)
        self.master.attributes("-topmost", True)
        self.master.wm_withdraw()
        self.master.overrideredirect(True)
        self.master.bind("<Motion>", lambda *ignore: self.set_status(True))
        self.master.bind("<Leave>", lambda *ignore: self.set_status(False))
        self.create_buttons()
        self.start_thread()
        self.pack()

    def set_status(self, status: bool):
        self.status = status

    def hide(self):
        self.master.wm_withdraw()
        self.xposition = None
        self.yposition = None
        self.status = True
    
    def update_gui(self):
        cursor_position = utils.get_mouse_cursor_position()
        app_wsize = utils.Size(250, 35)
        x_pos, y_pos = utils.get_cursor_position_to_set(app_wsize, cursor_position)
        self.master.geometry(f"+{x_pos}+{y_pos}")
        self.xposition = x_pos
        self.yposition = y_pos
        self.master.wm_deiconify()

    def start_thread(self):
        """Start thread to check the clipboard content"""
        def to_check():
            while True:
                # to hide the app
                status = self.status
                if status is False:
                    time.sleep(1)
                    if status == self.status:
                        self.hide()

                if self.xposition and self.yposition:
                    cursor_position = utils.get_mouse_cursor_position()
                    xdifference = abs(cursor_position.x - self.xposition)
                    ydifference = abs(cursor_position.y - self.yposition)
                    if xdifference > 300 or ydifference > 250:
                        self.hide()

                # detect change of selected text
                if utils.detect_selected_text_changed():
                    self.update_gui()

        thread = threading.Thread(target=to_check, daemon=True)
        thread.start()

    def create_buttons(self):
        """Create buttons options"""
        common_options = dict(
            borderwidth=0,
            anchor="w",
            background="#4f6481",
            activebackground="#153158",
            foreground="white",
            activeforeground="white",
        )

        self.title_button = tk.Button(
            self,
            text="AbC",
            command=lambda: utils.concatenate_functions_calls(
                utils.title_converter(), utils.call_to_paste(), self.hide()
            ),
            **common_options,
        )
        self.after_period_capitalize_button = tk.Button(
            self,
            text="Ab.C",
            command=lambda: utils.concatenate_functions_calls(
                utils.capitalize_after_one_periodconverter(),
                utils.call_to_paste(),
                self.hide(),
            ),
            **common_options,
        )
        self.uppercase_button = tk.Button(
            self,
            text="A",
            command=lambda: utils.concatenate_functions_calls(
                utils.upper_converter(), utils.call_to_paste(), self.hide()
            ),
            **common_options,
        )
        self.lowercase_button = tk.Button(
            self,
            text="a",
            command=lambda: utils.concatenate_functions_calls(
                utils.lower_converter(), utils.call_to_paste(), self.hide()
            ),
            **common_options,
        )
        self.capitalize_button = tk.Button(
            self,
            text="Ab",
            command=lambda: utils.concatenate_functions_calls(
                utils.capitalizer_converter(), utils.call_to_paste(), self.hide()
            ),
            **common_options,
        )
        self.close_button = tk.Button(
            self,
            text="X",
            command=self.master.destroy,
            borderwidth=0,
            anchor="w",
            foreground="white",
            activebackground="#fd5454",
            background="#fd5454",
            activeforeground="white",
        )

        self.close_button.pack(side="right")
        self.after_period_capitalize_button.pack(side="right")
        self.title_button.pack(side="right")
        self.capitalize_button.pack(side="right")
        self.lowercase_button.pack(side="right")
        self.uppercase_button.pack(side="right")