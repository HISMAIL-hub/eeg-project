import os, shutil, tempfile
from osfclient import OSF

PROJECT = os.environ["OSF_PROJECT"]
osf = OSF(token=os.environ["OSF_TOKEN"])
storage = osf.project(PROJECT).storage("osfstorage")

raw, done = {}, set()
for f in storage.files:
    p = f.path.lstrip("/")
    if p.startswith("raw/"):
        raw[os.path.basename(p)] = f
    elif p.startswith("processed/"):
        done.add(os.path.basename(p))

todo = [n for n in raw if n not in done]
print("A traiter :", todo)

def process(src, dst):
    shutil.copy(src, dst)  # placeholder : renvoie le même fichier

with tempfile.TemporaryDirectory() as tmp:
    for name in todo:
        src = os.path.join(tmp, "in_" + name)
        dst = os.path.join(tmp, "out_" + name)
        with open(src, "wb") as fp:
            raw[name].write_to(fp)
        process(src, dst)
        with open(dst, "rb") as fp:
            storage.create_file("processed/" + name, fp, update=True)
        print("OK :", name)