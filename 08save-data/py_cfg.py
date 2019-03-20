import configparser

cfg = configparser.ConfigParser()
cfg.read("settings.cfg")
print("Greeting in English: {}\nGreeting in French: {}".format(cfg["english"]["greeting"], cfg["french"]["greeting"]), end="\n\n")