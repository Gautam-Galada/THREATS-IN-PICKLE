# MALICIOUS PICKLE 

This repository contains a threat creation script that demonstrates an example of creating a threat using a machine learning model. The script uses the `webbrowser` module to open a malicious URL and then patches the save function of a pretrained model using the `patch_torch_save` library.

## Usage

1. Ensure that you have the necessary dependencies installed.
2. Run the `attack` function to open a malicious URL in the web browser and remove the `webbrowser` module from the `sys.modules`.
3. Instantiate the `CreateThreat` class with the desired `model_path` and `model_name`.
4. The `CreateThreat` class creates a threat by patching the save function of the pretrained model and saving it to the specified `model_path`.
