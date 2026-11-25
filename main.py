import os
import shutil


def main():
    # The word itself lives in entry.txt, written long before this runs.
    # This function only carries it over to the output folder untouched,
    # so what the judge reads is exactly the word that was chosen.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
