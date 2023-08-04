
import os
import platform
import shutil

from version import VERSION_WITHOUT_COMMIT

base_name = "GameCube File Tools"

import struct
bitness_suffix = "_x64" if struct.calcsize("P") == 8 else "_x86"
exe_ext = ""
if platform.system() == "Windows":
  exe_ext = ".exe"
  platform_name = "win"
if platform.system() == "Darwin":
  exe_ext = ".app"
  platform_name = "mac"
if platform.system() == "Linux":
  platform_name = "linux"

exe_path = os.path.join(".", "dist", base_name + exe_ext)
if not (os.path.isfile(exe_path) or os.path.isdir(exe_path)):
  raise Exception(f"Executable not found: {exe_path}")

release_archive_path = os.path.join(
    ".", "dist", f"release_archive_{VERSION_WITHOUT_COMMIT}{bitness_suffix}")
print(f"Writing build to path: {release_archive_path}")

if os.path.exists(release_archive_path) and os.path.isdir(release_archive_path):
  shutil.rmtree(release_archive_path)

os.mkdir(release_archive_path)
shutil.copyfile("README.md", os.path.join(release_archive_path, "README.txt"))

shutil.move(exe_path, os.path.join(release_archive_path, base_name + exe_ext))

if platform.system() == "Darwin":
  shutil.make_archive(release_archive_path, "zip", release_archive_path)
