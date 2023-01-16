import codecs
import json
import os

def is_target_folder(all_file_name):
    """
    :function: judge the target folder
    :parameter: fold path
    """
    for file in all_file_name:
        if '.info' in file:
            return True

    return False


def get_file_name(folder_name):
    """
    : function: get new name from info file of cell folder
    :param folder_name: cell folder path
    :return: new file name
    """
    all_file_name = os.listdir(folder_name)
    for file in all_file_name:
        if '.info' in file:
            info_file_path = os.path.join(folder_name, file)
            with codecs.open(info_file_path, 'r', 'utf-8') as f:
                content = json.loads(f.read())
                file_name = content["PartName"]
                if file_name is None:
                    return content["Title"]
                else:
                    return file_name.replace(' ', '')

        else:
            pass


def rename_cell_folder(folder_name):
    """
    :function: rename file in each cell folder
    :param folder_name: cell folder path
    :return: no
    """
    all_file_name = os.listdir(folder_name)
    if len(all_file_name) > 1 and is_target_folder(all_file_name):
        file_name = get_file_name(folder_name)
        # TODO: need a reg to match file_name start with number + "."
        prefix = os.path.basename(folder_name).zfill(3) + "."
        for i in range(len(all_file_name)):
            _file = all_file_name[i]
            if '.flv' in _file:
                old_file_path = os.path.join(folder_name, _file)
                decode_bili(old_file_path)
                suffix = _file[_file.rfind('_'):]  # _10.flv
                if len(suffix) <= 1:
                    new_file_path = os.path.join(folder_name, str(prefix + file_name + '.flv'))
                else:
                    new_file_path = os.path.join(folder_name, str(prefix + file_name + suffix))
                print("do rename: use " + new_file_path + " replace old name: " + new_file_path)
                os.rename(old_file_path, new_file_path.zfill(3))
            if '.mp4' in _file:
                old_file_path = os.path.join(folder_name, _file)
                decode_bili(old_file_path)
                suffix = _file[_file.rfind('_'):]  # _10.flv
                if len(suffix) <= 1:
                    new_file_path = os.path.join(folder_name, str(prefix + file_name + '.flv'))
                else:
                    new_file_path = os.path.join(folder_name, str(prefix + file_name + suffix))
                print("do rename: use " + new_file_path + " replace old name: " + new_file_path)
                os.rename(old_file_path, new_file_path)
            else:
                pass


def get_cell_folder(dir_name, cell_folders):
    """
    :function: get cell folder.
    :parameter: path
    :parameter: cell folder name list
    :return: all cell folder name list
    """
    all_dir = os.listdir(dir_name)
    dirs = [i for i in all_dir if os.path.isdir(os.path.join(dir_name, i))]

    if len(dirs) is 0:
        cell_folders.append(dir_name)
        print(dir_name)

    for _dir in dirs:
        get_cell_folder(os.path.join(dir_name, _dir), cell_folders)
    return cell_folders


def decode_bili(name):
    """
    just decode video for v2.14.79.0
    :param name: full video name
    :return:
    """
    with open(name, mode='rb+') as f:
        old = f.readlines()
        while old[0].startswith(b'\xff'):
            old[0] = old[0][1:]
        f.seek(0) # rewind
        f.writelines(old)

if __name__ == "__main__":
    try:
        # 自动获取目录
        current_path = os.path.dirname(os.path.abspath(__file__))
        # current_path = "C:\\Users\\zack\\336748125"
        cell_folders = []
        cell_folders = get_cell_folder(current_path, cell_folders)

        for cell_folder in cell_folders:
            rename_cell_folder(cell_folder)

        os.system("pause")
    except Exception as e:
        print(e)
        os.system("pause")
