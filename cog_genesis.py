import cog
from pathlib import Path
import torch
import pixray
import yaml
import pathlib
import os
import yaml

from cogrun import create_temporary_copy

class GenesisPredictor(cog.Predictor):
    def setup(self):
        print("---> GenesisPredictor Setup")

    # Define the input types for a prediction
    @cog.input("title", type=str, default="")
    @cog.input("drawing_style", type=str, options=["image", "pixels"], default="image")
    @cog.input("quality", type=str, options=["draft", "mintable"], default="draft")
    @cog.input("optional_settings", type=str, default="\n")
    def predict(self, title, drawing_style, quality, optional_settings):
        """Run a single prediction on the model"""
        print("---> Pixray Genesis Init")

        pixray.reset_settings()

        if(quality=="draft"):
            pixray.add_settings(output="outputs/genesis_draft.png", quality="draft", scale=2.5, iterations=100)
        else:
            pixray.add_settings(output="outputs/genesis.png", quality="best", scale=4, iterations=300)

        # apply settings in order
        title = title.strip()
        if title == "" or title == "(untitled)":
            title = "Wow, that looks amazing!|Trending on Artstation"
            pixray.add_settings(custom_loss='saturation')

        if drawing_style == "pixels":
            pixray.add_settings(prompts=f"{title} #pixelart")
        else:
            pixray.add_settings(prompts=title)

        if drawing_style == "image":
            pixray.add_settings(drawer="vqgan")
        else:
            pixray.add_settings(drawer="pixel")

        optional_settings = optional_settings.strip()
        if optional_settings != "":
            ydict = yaml.safe_load(optional_settings)
            if ydict is not None:
                pixray.add_settings(**ydict)
                empty_settings = False

        pixray.add_settings(skip_args=True)
        settings = pixray.apply_settings()
        pixray.do_init(settings)
        run_complete = False
        while run_complete == False:
            run_complete = pixray.do_run(settings, return_display=True)
            temp_copy = create_temporary_copy(settings.output)
            yield pathlib.Path(os.path.realpath(temp_copy))