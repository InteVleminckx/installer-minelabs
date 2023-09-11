import subprocess
import sys

"""
This file will generate an executable, hallo mijn naam is inte
"""

if __name__ == '__main__':
    number_of_arguments = len(sys.argv)

    if number_of_arguments == 1:
        print("No arguments passed. Please pass which version of installer you want to generate [script/interface].")
        print("Example: python generate.py interface")
        sys.exit(1)

    elif number_of_arguments == 2:
        version = sys.argv[1]

        pyinstaller_command = "py -m PyInstaller --onefile --icon=resources/images/minelabs-logo.ico" \
                              " --add-data resources/*.json;resources "

        try:

            # Run PyInstaller as a subprocess
            if version == "interface":
                pyinstaller_command += "interface_version.py --name Minelabs-Setup --noconsole" \
                                       " --add-data resources/maps/vAlpha/*.zip;resources/maps/vAlpha\ " \
                                       "--add-data resources/maps/vLatest/*.zip;resources/maps/vLatest\\" \
                                      " --add-data resources/images/*;resources/images"
                subprocess.run(pyinstaller_command, check=True)
            elif version == "script":
                data_versions = {
                    "alpha": "resources/maps/vAlpha/*.zip;resources/maps/vAlpha\\",
                    "latest": "resources/maps/vLatest/*.zip;resources/maps/vLatest\\"
                }
                r_version = "alpha"
                pyinstaller_command += f"script_version.py --name Minelabs-installer-{r_version} --add-data " \
                                       f"{data_versions[version]}"
                subprocess.run(pyinstaller_command, check=True)

            else:
                print(
                    "Invalid version. Please pass which version of installer you want to generate [script/interface].")
                print("Example: python generate.py interface")
                sys.exit(1)

            print("PyInstaller operation completed successfully.")
        except subprocess.CalledProcessError as e:
            print("PyInstaller operation failed. Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

    else:
        print(
            "Too many arguments passed. Please pass which version of installer you want to generate [script/interface].")
        print("Example: python generate.py interface")
        sys.exit(1)
