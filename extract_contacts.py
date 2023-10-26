import pyautogui as pui
import os

def csv_to_vcf(name_csv: str):
    path = r"C:\Users\91766\Contacts"
    path = os.path.realpath(path)
    os.startfile(path)

    pui.sleep(1)

    for i in range(4):
        pui.press('tab')
        pui.sleep(0.25)
    pui.sleep(1)
    pui.press('tab')

    for i in range(5):
        pui.press('right')
        pui.sleep(0.25)

    pui.hotkey('enter')
    pui.sleep(1)

    pui.press('c')
    pui.sleep(1)

    pui.hotkey('enter')
    pui.sleep(1)

    pui.click(948, 287)
    pui.sleep(1)

    pui.write(name_csv, interval=0.25)

    for i in range(2):
        pui.hotkey('enter')
        pui.sleep(0.25)

    pui.click(648, 340)
    pui.click(648, 340)

    for i in range(14):
        pui.press('down')

    for i in range(3):
        pui.hotkey('enter')
        pui.sleep(0.25)

    pui.sleep(5)

    pui.press('tab', 2)
    pui.hotkey('enter')
    pui.press('right')
    pui.hotkey('enter')
    pui.sleep(1)

    pui.press('down', 2)
    pui.hotkey('enter')
    pui.sleep(2)
    pui.press('m')
    pui.sleep(1)

    pui.write("contacts'vcf", interval=0.10)
    for i in range(3):
        pui.hotkey('enter')
        pui.sleep(0.25)


    for i in range(2):
        pui.press('tab')
        pui.sleep(0.25)

    pui.hotkey('enter')
    pui.sleep(1)

    dir_name = r"C:\Users\91766\Contacts"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".contact"):
            os.remove(os.path.join(dir_name, item))

    pui.sleep(2)

    os.system(r"cd C:\Users\91766\contacts'vcf && ls | wc -l && copy *.vcf merged_file.vcf")

    directory = r"C:\Users\91766\contacts'vcf"
    remove = os.listdir(directory)
    for item in remove:
        if item != "merged_file.vcf":
            os.remove(os.path.join(directory, item))

    path = r"C:\Users\91766\contacts'vcf"
    path = os.path.realpath(path)
    os.startfile(path)

if __name__ == '__main__':
    csv_to_vcf('name')