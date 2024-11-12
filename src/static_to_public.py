import os
import shutil
def clear_destination(path):
    if os.path.exists(path):
        print(path)
        shutil.rmtree(path, True)
    os.mkdir(path)


def static_to_public(source, dest):
    if not source:
        raise Exception("missing source")
    elif not dest:
        raise Exception("missing destination")
    path_list = os.listdir(source)
    print(path_list)
    for path in path_list:
        if os.path.isfile(os.path.join(source, path)):
            print(os.path.join(source, path))
            shutil.copy(os.path.join(source, path), dest)
        else:
            print(os.path.join(source, path))
            os.mkdir(os.path.join(dest, path))
            print(os.path.join(dest, path))
            static_to_public(os.path.join(source, path), os.path.join(dest, path))



